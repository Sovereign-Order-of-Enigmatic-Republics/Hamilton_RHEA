
---

# ============================================================
# 📓 **notebooks/03_Macrocycle_Statistics.md**
# ============================================================

```md
# Notebook 03 — Macrocycle Statistics

We measure:

- Lengths of reversible windows  
- Timing of irreversible commits  
- Correlation with Θ(t)

### Code

```python
from src.experiments.macrocycle_demo import run_macrocycle

run_macrocycle(steps=10000)
