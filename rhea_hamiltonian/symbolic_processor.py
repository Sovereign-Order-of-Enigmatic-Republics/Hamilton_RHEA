# -*- coding: utf-8 -*-
"""
Discrete symbolic processor implementing reversible and irreversible gates.
"""

import random

class SymbolicProcessor:
    def __init__(self, alphabet_size=4, length=12):
        self.alphabet = list(range(alphabet_size))
        self.n = length

        # Random initial symbolic state
        self.state = tuple(random.choice(self.alphabet) for _ in range(self.n))

    # --------------------------------------------------------
    # Reversible operations
    # --------------------------------------------------------
    def reversible_gate(self):
        """A reversible local permutation (bijective)."""
        idx = random.randrange(self.n - 1)
        lst = list(self.state)
        lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
        self.state = tuple(lst)
        return 0  # erased bits = 0

    # --------------------------------------------------------
    # Irreversible operation
    # --------------------------------------------------------
    def irreversible_gate(self):
        """A 1-bit erasure: merges two equally likely states."""
        idx = random.randrange(self.n)
        lst = list(self.state)
        lst[idx] = 0   # collapse two symbols → one
        self.state = tuple(lst)
        return 1  # erased bits = 1

