# -*- coding: utf-8 -*-
"""Macrocycle demonstration for the RHEA-UCM symbolic scheduler."""

from __future__ import annotations

import random
from dataclasses import dataclass
import numpy as np

from rhea_hamiltonian.lorenz_glyph import lorenz_step, theta_from_state
from rhea_hamiltonian.scheduler import choose_gate
from rhea_hamiltonian.symbolic_processor import SymbolicProcessor


@dataclass(frozen=True)
class MacrocycleResult:
    reversible_run_lengths: tuple[int, ...]
    irreversible_events: int
    erased_bits: float
    mean_theta: float
    final_state: tuple[int, ...]


def run_macrocycle(steps: int = 5000, dt: float = 1e-3, *, seed: int = 42, theta_alpha: float = 0.01) -> MacrocycleResult:
    if steps < 0:
        raise ValueError("steps must be non-negative")
    if dt <= 0:
        raise ValueError("dt must be positive")
    if theta_alpha < 0:
        raise ValueError("theta_alpha must be non-negative")

    rng = random.Random(seed)
    state = np.array([1.0, 1.0, 1.0], dtype=float)
    proc = SymbolicProcessor(rng=rng)
    runs: list[int] = []
    current_run = 0
    irreversible_events = 0
    erased_bits = 0.0
    theta_sum = 0.0

    for _ in range(steps):
        state = lorenz_step(state, dt)
        theta = float(theta_from_state(state, alpha=theta_alpha))
        theta_sum += theta
        erased = float(choose_gate(theta, proc.reversible_gate, proc.irreversible_gate, rng=rng))
        if erased == 0.0:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 0
            irreversible_events += 1
            erased_bits += erased

    runs.append(current_run)
    return MacrocycleResult(tuple(runs), irreversible_events, erased_bits, theta_sum / steps if steps else 0.0, proc.state)


if __name__ == "__main__":
    result = run_macrocycle()
    print("Reversible run lengths:", list(result.reversible_run_lengths[:10]))
    print("Total irreversible events:", result.irreversible_events)
    print("Total bits erased (uniform prior):", result.erased_bits)
    print("Mean reversible scheduling weight:", result.mean_theta)
