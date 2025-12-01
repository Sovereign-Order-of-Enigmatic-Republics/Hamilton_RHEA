# -*- coding: utf-8 -*-
"""
Macrocycle demonstration for the RHEA-UCM Hamiltonian model.
"""

import numpy as np
from rhea_hamiltonian.lorenz_glyph import lorenz_step, theta_from_state
from rhea_hamiltonian.symbolic_processor import SymbolicProcessor
from rhea_hamiltonian.scheduler import choose_gate

def run_macrocycle(steps=5000, dt=1e-3):
    S = np.array([1.0, 1.0, 1.0])
    proc = SymbolicProcessor()

    reversible_runs = []
    current_run = 0

    erased_bits = []

    for _ in range(steps):
        S = lorenz_step(S, dt)
        theta = theta_from_state(S)

        erased = choose_gate(
            theta,
            proc.reversible_gate,
            proc.irreversible_gate
        )

        if erased == 0:
            current_run += 1
        else:
            reversible_runs.append(current_run)
            erased_bits.append(erased)
            current_run = 0

    print("Reversible run lengths:", reversible_runs[:10])
    print("Total irreversible events:", len(erased_bits))
    print("Total bits erased:", sum(erased_bits))

if __name__ == "__main__":
    run_macrocycle()