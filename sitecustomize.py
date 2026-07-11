"""Local Python startup tweaks for this research workspace.

Pytest can auto-load globally installed plugins from ROS/other system stacks.
Those plugins are unrelated to this project and may import incompatible
dependencies before our tests even start. Disabling plugin autoload keeps tests
reproducible inside the active environment.
"""

from __future__ import annotations

import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")
