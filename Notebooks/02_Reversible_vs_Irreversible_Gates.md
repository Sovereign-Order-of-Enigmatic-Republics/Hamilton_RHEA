
---

# ============================================================
# 📓 **notebooks/02_Reversible_vs_Irreversible_Gates.md**
# ============================================================

```md
# Notebook 02 — Reversible vs Irreversible Gates

Reversible gates behave as permutations:

\[
\mu(C_s) = \mu(C_{G(s)}).
\]

Irreversible gates merge states:

\[
C_{s_1}, C_{s_2} \to C_{s_*}.
\]

### Code

```python
from src.symbolic_processor import SymbolicProcessor
from src.hamiltonian_embedding import VolumeTracker

proc = SymbolicProcessor()
vt = VolumeTracker()

vt.register_state(proc.state)
old_state = proc.state

proc.reversible_gate()
new_state = proc.state

vt.apply_reversible(old_state, new_state)
