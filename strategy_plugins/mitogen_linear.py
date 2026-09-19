"""Expose Mitogen's strategy plugin without hardcoding the venv's site-packages path in `ansible.cfg`."""

from ansible_mitogen.plugins.strategy.mitogen_linear import StrategyModule

__all__ = ["StrategyModule"]
