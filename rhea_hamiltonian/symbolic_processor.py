# -*- coding: utf-8 -*-
"""Discrete symbolic processor with explicit logical-erasure accounting."""

from __future__ import annotations

import math
import random
from typing import Optional


class SymbolicProcessor:
    """Finite symbolic register supporting reversible and reset operations."""

    def __init__(self, alphabet_size: int = 4, length: int = 12, *, rng: Optional[random.Random] = None) -> None:
        if alphabet_size < 2:
            raise ValueError("alphabet_size must be at least 2")
        if length < 2:
            raise ValueError("length must be at least 2")
        self.alphabet = tuple(range(alphabet_size))
        self.n = int(length)
        self.rng = rng or random.Random()
        self.state = tuple(self.rng.choice(self.alphabet) for _ in range(self.n))

    @property
    def alphabet_size(self) -> int:
        return len(self.alphabet)

    def reversible_gate(self) -> float:
        idx = self.rng.randrange(self.n - 1)
        values = list(self.state)
        values[idx], values[idx + 1] = values[idx + 1], values[idx]
        self.state = tuple(values)
        return 0.0

    def irreversible_gate(self) -> float:
        idx = self.rng.randrange(self.n)
        values = list(self.state)
        values[idx] = 0
        self.state = tuple(values)
        return math.log2(self.alphabet_size)
