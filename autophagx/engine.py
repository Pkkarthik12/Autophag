import time
import random

class RobotComponent:
    def __init__(self, name, mass, energy_value, criticality):
        self.name = name
        self.mass = mass  # kg
        self.energy_value = energy_value  # Joules
        self.criticality = criticality  # 0 to 1 (1 is essential)
        self.is_consumed = False

    def __repr__(self):
        return f"[{self.name} (Mass: {self.mass}kg, Energy: {self.energy_value}J, Criticality: {self.criticality})]"

class AutophagXRobot:
    def __init__(self):
        self.energy_reserve = 5000  # Initial chemical/battery storage
        self.components = [
            RobotComponent("Chassis Core", 10.0, 50000, 1.0),
            RobotComponent("Leg FL", 2.0, 10000, 0.7),
            RobotComponent("Leg FR", 2.0, 10000, 0.7),
            RobotComponent("Leg RL", 2.0, 10000, 0.7),
            RobotComponent("Leg RR", 2.0, 10000, 0.7),
            RobotComponent("Sensor Array", 0.5, 2000, 0.4),
            RobotComponent("Outer Shell L1", 1.0, 5000, 0.2),
            RobotComponent("Outer Shell L2", 1.0, 5000, 0.2),
        ]
        self.current_mass = sum(c.mass for c in self.components)
        self.active = True

    def get_status(self):
        remaining = [c.name for c in self.components if not c.is_consumed]
        return {
            "energy": self.energy_reserve,
            "mass": self.current_mass,
            "components_count": len(remaining),
            "components": remaining
        }

    def consume_component(self, component_name):
        for c in self.components:
            if c.name == component_name and not c.is_consumed:
                if c.criticality >= 1.0:
                    print(f"CRITICAL ERROR: Cannot consume core component {c.name}!")
                    return False
                
                print(f"AUTOPHAGY INITIATED: Consuming {c.name}...")
                c.is_consumed = True
                self.energy_reserve += c.energy_value
                self.current_mass -= c.mass
                print(f"RECOVERY: Gained {c.energy_value}J. New Energy: {self.energy_reserve}J. Mass reduced to {self.current_mass}kg.")
                return True
        return False

    def tick(self):
        """Simulate energy drain over time."""
        drain = 100 * (self.current_mass / 20.0) # Base drain scaled by mass
        self.energy_reserve -= drain
        if self.energy_reserve <= 0:
            self.active = False
            print("MISSION FAILURE: Energy depleted.")

if __name__ == "__main__":
    bot = AutophagXRobot()
    print("Autophag-X Alpha Online.")
    while bot.active:
        status = bot.get_status()
        print(f"Energy: {status['energy']:.2f}J | Mass: {status['mass']:.2f}kg")
        
        if bot.energy_reserve < 2000:
            # Simple heuristic: consume least critical component
            available = [c for c in bot.components if not c.is_consumed and c.criticality < 1.0]
            if available:
                target = min(available, key=lambda x: x.criticality)
                bot.consume_component(target.name)
            else:
                print("No sacrificial components left!")
                break
        
        bot.tick()
        time.sleep(0.5)
