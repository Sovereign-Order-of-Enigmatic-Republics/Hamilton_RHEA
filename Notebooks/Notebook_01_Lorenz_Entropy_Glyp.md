# Notebook 01 — Lorenz Entropy Glyph

This notebook explains:

- The Lorenz system  
- Bounded entropy glyph \(S(t)\)  
- Entropy-weight mapping \(\Theta(t)=g(S(t))\)

## Lorenz System

We integrate:

\[
\dot S_1 = \sigma(S_2 - S_1),\;
\dot S_2 = \rho S_1 - S_2 - S_1 S_3,\;
\dot S_3 = S_1 S_2 - \beta S_3.
\]

### Code

```python
from src.lorenz_glyph import lorenz_step, theta_from_state
import numpy as np

S = np.array([1.0,1.0,1.0])
trajectory = []
theta_vals = []

for _ in range(20000):
    S = lorenz_step(S, 1e-3)
    trajectory.append(S)
    theta_vals.append(theta_from_state(S))
