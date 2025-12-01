
---

# ============================================================
# 📓 **notebooks/04_Sobolev_Bounds_Demo.md**
# ============================================================

```md
# Notebook 04 — Sobolev Bounds Demo

This notebook illustrates why the Lorenz modulation:

\[
T(t) = g(S(t))
\]

does **not** break:

- energy estimates  
- coercivity  
- Sobolev well-posedness  

### Toy PDE demonstration

Consider:

\[
u_{t+1} = u_t + T(t) F(u_t,S(t)).
\]

Where `F` is artificial but smooth.

### Code

```python
import numpy as np
from src.lorenz_glyph import lorenz_step, theta_from_state

def F(u, S):
    return -0.01*u + 0.001*np.linalg.norm(S)

u = 1.0
S = np.array([1.0,1.0,1.0])

for _ in range(5000):
    S = lorenz_step(S, 1e-3)
    T = theta_from_state(S)
    u = u + T * F(u,S)
