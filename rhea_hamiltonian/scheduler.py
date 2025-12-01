# -*- coding: utf-8 -*-
"""
Probabilistic entropy-aware scheduler.
Implements Equation (7.1')
"""

import random

def choose_gate(theta, reversible_fn, irreversible_fn):
    """
    theta in (0,1].
    With probability theta -> reversible, else irreversible.
    """
    if random.random() < theta:
        return reversible_fn()
    else:
        return irreversible_fn()