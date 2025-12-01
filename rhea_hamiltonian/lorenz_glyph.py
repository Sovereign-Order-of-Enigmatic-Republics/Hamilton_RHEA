# -*- coding: utf-8 -*-
"""
Lorenz entropy-glyph subsystem.
Implements a bounded chaotic signal S(t) and a scheduler weight Θ(t)=g(S(t)).
"""

import numpy as np

def lorenz_step(state, dt, sigma=10.0, rho=28.0, beta=8/3):
    x, y, z = state

    def f(x, y, z):
        return (
            sigma * (y - x),
            rho * x - y - x * z,
            x * y - beta * z
        )

    k1 = f(x, y, z)
    k2 = f(x + 0.5*dt*k1[0], y + 0.5*dt*k1[1], z + 0.5*dt*k1[2])
    k3 = f(x + 0.5*dt*k2[0], y + 0.5*dt*k2[1], z + 0.5*dt*k2[2])
    k4 = f(x + dt*k3[0], y + dt*k3[1], z + dt*k3[2])

    x_new = x + dt*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]) / 6
    y_new = y + dt*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]) / 6
    z_new = z + dt*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2]) / 6

    return np.array([x_new, y_new, z_new])


def theta_from_state(S, alpha=0.01):
    """Entropy scheduler weight Θ(t) = exp(-α||S||²)."""
    return np.exp(-alpha * np.linalg.norm(S)**2)