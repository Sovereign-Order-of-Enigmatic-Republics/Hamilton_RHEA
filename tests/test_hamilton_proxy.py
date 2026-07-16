from __future__ import annotations

import math
import random
import unittest

from macrocycle_demo import run_macrocycle
from rhea_hamiltonian.scheduler import choose_gate
from rhea_hamiltonian.symbolic_processor import SymbolicProcessor


class SymbolicProcessorTests(unittest.TestCase):
    def test_reversible_gate_is_an_involution_with_replayed_index(self) -> None:
        rng = random.Random(7)
        processor = SymbolicProcessor(alphabet_size=4, length=8, rng=rng)
        original = processor.state
        random_state = rng.getstate()
        processor.reversible_gate()
        rng.setstate(random_state)
        processor.reversible_gate()
        self.assertEqual(processor.state, original)

    def test_reset_erasure_matches_uniform_alphabet_information(self) -> None:
        processor = SymbolicProcessor(alphabet_size=4, length=4, rng=random.Random(1))
        self.assertEqual(processor.irreversible_gate(), 2.0)
        ternary = SymbolicProcessor(alphabet_size=3, length=4, rng=random.Random(1))
        self.assertAlmostEqual(ternary.irreversible_gate(), math.log2(3))

    def test_invalid_dimensions_rejected(self) -> None:
        with self.assertRaises(ValueError):
            SymbolicProcessor(alphabet_size=1)
        with self.assertRaises(ValueError):
            SymbolicProcessor(length=1)


class SchedulerTests(unittest.TestCase):
    def test_probability_bounds(self) -> None:
        with self.assertRaises(ValueError):
            choose_gate(-0.1, lambda: 0, lambda: 1)
        with self.assertRaises(ValueError):
            choose_gate(1.1, lambda: 0, lambda: 1)

    def test_endpoints_are_deterministic(self) -> None:
        self.assertEqual(choose_gate(1.0, lambda: "r", lambda: "i"), "r")
        self.assertEqual(choose_gate(0.0, lambda: "r", lambda: "i"), "i")


class MacrocycleTests(unittest.TestCase):
    def test_reproducible_and_accounted(self) -> None:
        first = run_macrocycle(steps=200, seed=123)
        second = run_macrocycle(steps=200, seed=123)
        self.assertEqual(first, second)
        self.assertEqual(first.erased_bits, 2.0 * first.irreversible_events)
        self.assertGreaterEqual(first.mean_theta, 0.0)
        self.assertLessEqual(first.mean_theta, 1.0)
        self.assertGreaterEqual(len(first.reversible_run_lengths), 1)


if __name__ == "__main__":
    unittest.main()
