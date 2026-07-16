# -*- coding: utf-8 -*-
"""Probabilistic entropy-aware scheduler."""

from __future__ import annotations

import random
from collections.abc import Callable
from typing import Optional, TypeVar

T = TypeVar("T")


def choose_gate(theta: float, reversible_fn: Callable[[], T], irreversible_fn: Callable[[], T], *, rng: Optional[random.Random] = None) -> T:
    if not 0.0 <= theta <= 1.0:
        raise ValueError("theta must lie in [0, 1]")
    source = rng or random
    return reversible_fn() if source.random() < theta else irreversible_fn()
