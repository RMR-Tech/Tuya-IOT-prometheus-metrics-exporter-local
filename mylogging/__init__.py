"""Logging configuration for Tuya Metrics Exporter using loguru."""

import os
import sys
from pathlib import Path

from loguru import logger

# Remove default handler
logger.remove()

# Create logs directory if it doesn't exist
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Determine console log level based on environment variable
log_verbose = os.getenv("LOG_VERBOSE", "").lower()
console_level = "DEBUG" if log_verbose == "debug" else "INFO"

# Add console handler with dynamic level
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level=console_level,
    colorize=True,
)

# Add rotating file handler
logger.add(
    logs_dir / "tuya_metrics.log",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    level=console_level,
    rotation=5 * 1024 * 1024,  # Rotate when file reaches 5MB (in bytes)
    retention=20,  # Keep 20 rotated files (approximately 100MB total)
    enqueue=True,  # Thread-safe logging
    backtrace=True,  # Better error traces
    diagnose=True,  # Better error diagnostics
)

# Export logger for use in other modules
__all__ = ["logger"]
