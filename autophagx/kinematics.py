class KinematicSolver:
    def __init__(self, total_legs=4):
        self.total_legs = total_legs
        
    def calculate_mobility(self, active_legs):
        """
        Returns a mobility score from 0.0 to 1.0.
        4 legs: 1.0 (Stable, Fast)
        3 legs: 0.6 (Limping, Slow)
        2 legs: 0.2 (Dragging, Barely functional)
        1 leg: 0.05 (Static, pivot only)
        0 legs: 0.0 (Dead)
        """
        count = len(active_legs)
        if count == 4:
            return 1.0
        elif count == 3:
            return 0.6
        elif count == 2:
            return 0.2
        elif count == 1:
            return 0.05
        else:
            return 0.0

    def get_movement_cost_multiplier(self, mobility_score):
        """Lower mobility = higher energy cost to move a certain distance."""
        if mobility_score >= 1.0:
            return 1.0
        elif mobility_score > 0:
            return 1.0 / (mobility_score + 0.1) # Inverse relationship
        return float('inf')
