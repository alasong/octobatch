"""
Octobatch TUI - Terminal User Interface for batch processing runs.

A Textual-based TUI for monitoring and inspecting Octobatch runs.
"""

import sys
from pathlib import Path
# Add scripts/ to sys.path so bare imports work
_scripts_dir = str(Path(__file__).resolve().parent.parent)
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)

from version import __version__  # noqa: F401
