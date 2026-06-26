from __future__ import annotations

import os
import traceback
from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import QObject, QThread, Signal

LOG = os.path.join(os.path.expanduser("~"), "mitd_log.txt")


def _log(msg):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


@dataclass
class ConversionResult:
    source: str
    title: Optional[str]
    markdown: str
    success: bool
    error: str = ""


class ConversionRunner(QObject):
    result_ready = Signal(ConversionResult)
    finished_all = Signal()

    def __init__(self):
        super().__init__()
        self._running = False
        self._thread = None

    def convert(self, source: str, is_url: bool = False):
        if self._running:
            return
        self._running = True
        self._thread = QThread()
        self._worker_obj = _SingleWorker(source)
        self._worker_obj.moveToThread(self._thread)
        self._worker_obj.done.connect(self._on_done)
        self._thread.started.connect(self._worker_obj.run)
        self._thread.start()

    def _on_done(self, result):
        self.result_ready.emit(result)
        self._running = False
        self.finished_all.emit()
        self._thread.quit()
        self._thread.wait()
        self._thread.deleteLater()
        self._worker_obj.deleteLater()

    @property
    def is_running(self):
        return self._running

    def cancel(self):
        self._running = False


class _SingleWorker(QObject):
    done = Signal(object)

    def __init__(self, source):
        super().__init__()
        self._source = source

    def run(self):
        try:
            from markitdown import MarkItDown
            md = MarkItDown()
            result = md.convert(self._source)
            self.done.emit(ConversionResult(
                source=self._source, title=result.title,
                markdown=result.markdown, success=True
            ))
        except Exception as e:
            self.done.emit(ConversionResult(
                source=self._source, title=None,
                markdown="", success=False, error=str(e)
            ))


class _BatchWorker(QObject):
    done = Signal(list)

    def __init__(self, sources):
        super().__init__()
        self._sources = sources
        self._cancelled = False

    def cancel(self):
        self._cancelled = True

    def run(self):
        _log("Worker run start")
        results = []
        try:
            from markitdown import MarkItDown
            _log("Import OK")
            md = MarkItDown()
            _log("MarkItDown created")
        except Exception as e:
            _log(f"Import FAIL: {e}")
            self.done.emit(results)
            return

        total = len(self._sources)
        for i, source in enumerate(self._sources):
            if self._cancelled:
                _log("Cancelled")
                break
            try:
                _log(f"[{i+1}/{total}] Converting: {source}")
                _log(f"  File exists: {os.path.exists(source)}")
                result = md.convert(source)
                cr = ConversionResult(
                    source=source, title=result.title,
                    markdown=result.markdown, success=True
                )
                _log(f"  OK, len={len(result.markdown)}")
            except Exception as e:
                cr = ConversionResult(
                    source=source, title=None,
                    markdown="", success=False,
                    error=f"{type(e).__name__}: {e}"
                )
                _log(f"  FAIL: {type(e).__name__}: {e}")
            results.append(cr)

        _log(f"Worker done: {len(results)} results")
        self.done.emit(results)


class BatchConversionRunner(QObject):
    progress = Signal(int, int, ConversionResult)
    finished_all = Signal(list)
    stats_updated = Signal(int, int, int)

    def __init__(self, max_workers: int = 4):
        super().__init__()
        self._max_workers = max_workers
        self._running = False
        self._thread = None
        self._worker = None

    def convert_all(self, sources):
        if self._running:
            return
        _log(f"convert_all called with {len(sources)} sources")
        _log(f"First: {sources[0] if sources else 'EMPTY'}")
        self._running = True

        self._thread = QThread()
        self._worker = _BatchWorker(sources)
        self._worker.moveToThread(self._thread)
        self._worker.done.connect(self._on_done)
        self._thread.started.connect(self._worker.run)
        self._thread.start()

    def _on_done(self, results):
        _log(f"_on_done called with {len(results)} results")
        self._running = False
        self.finished_all.emit(results)
        self._thread.quit()
        self._thread.wait()
        self._thread.deleteLater()
        self._worker.deleteLater()

    def cancel(self):
        if self._worker:
            self._worker.cancel()

    @property
    def is_running(self):
        return self._running
