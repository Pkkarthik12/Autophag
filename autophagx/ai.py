from .kinematics import KinematicSolver

class AutophagicDecisionEngine:
    def __init__(self):
        self.kinematics = KinematicSolver()

    def evaluate_options(self, current_energy, components):
        """
        Rank components for potential consumption based on Utility.
        Utility = Energy_Value / (Criticality * Mobility_Impact)
        """
        active_legs = [c for c in components if "Leg" in c.name and not c.is_consumed]
        current_mobility = self.kinematics.calculate_mobility(active_legs)
        
        candidates = []
        for c in components:
            if c.is_consumed or c.criticality >= 1.0:
                continue
                
            # Calculate what mobility would be if we consume this component
            potential_legs = active_legs.copy()
            if "Leg" in c.name:
                potential_legs = [l for l in potential_legs if l.name != c.name]
            
            new_mobility = self.kinematics.calculate_mobility(potential_legs)
            mobility_impact = max(0.01, (current_mobility - new_mobility))
            
            # Simple utility: High energy, low criticality, low mobility impact is better
            utility = c.energy_value / (c.criticality * 10 + mobility_impact * 100 + 1)
            candidates.append((utility, c))
            
        # Sort by highest utility
        candidates.sort(key=lambda x: x[0], reverse=True)
        return candidates

    def decide(self, current_energy, components):
        if current_energy > 3000:
            return None # No need to eat yet
            
        candidates = self.evaluate_options(current_energy, components)
        if candidates:
            return candidates[0][1] # Return the best component to consume
        return None
