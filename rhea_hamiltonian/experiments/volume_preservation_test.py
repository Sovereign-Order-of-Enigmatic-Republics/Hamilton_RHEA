# -*- coding: utf-8 -*-
"""
Checks that reversible_gate does not change symbolic volume proxy.
"""

from rhea_hamiltonian.symbolic_processor import SymbolicProcessor
from rhea_hamiltonian.hamiltonian_embedding import VolumeTracker

def test_volume():
    vt = VolumeTracker()
    proc = SymbolicProcessor()

    vt.register_state(proc.state)
    old = proc.state

    proc.reversible_gate()
    new = proc.state

    vt.apply_reversible(old, new)

    print("Volume(old) =", vt.volume[old])
    print("Volume(new) =", vt.volume[new])

if __name__ == "__main__":
    test_volume()