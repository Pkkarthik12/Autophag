import unittest
from autophagx.kinematics import KinematicSolver

class TestKinematics(unittest.TestCase):
    def setUp(self):
        self.solver = KinematicSolver()

    def test_mobility_scores(self):
        # 4 legs should be full mobility
        self.assertEqual(self.solver.calculate_mobility(["L1", "L2", "L3", "L4"]), 1.0)
        
        # 0 legs should be zero mobility
        self.assertEqual(self.solver.calculate_mobility([]), 0.0)
        
        # 3 legs should be reduced
        self.assertLess(self.solver.calculate_mobility(["L1", "L2", "L3"]), 1.0)
        self.assertGreater(self.solver.calculate_mobility(["L1", "L2", "L3"]), 0.5)

    def test_movement_cost(self):
        full_mobility = self.solver.calculate_mobility(["L1", "L2", "L3", "L4"])
        low_mobility = self.solver.calculate_mobility(["L1"])
        
        cost_full = self.solver.get_movement_cost_multiplier(full_mobility)
        cost_low = self.solver.get_movement_cost_multiplier(low_mobility)
        
        self.assertGreater(cost_low, cost_full)

if __name__ == "__main__":
    unittest.main()
