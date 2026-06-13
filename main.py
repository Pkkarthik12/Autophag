import time
from autophagx.engine import AutophagXRobot
from autophagx.ai import AutophagicDecisionEngine

def run_simulation():
    bot = AutophagXRobot()
    ai = AutophagicDecisionEngine()
    
    print("=== AUTOPHAG-X: AUTOPHAGIC MISSION START ===")
    print("Objective: Survive as long as possible by strategic self-consumption.")
    print("-" * 50)

    ticks = 0
    while bot.active:
        ticks += 1
        
        # AI evaluates the state
        target = ai.decide(bot.energy_reserve, bot.components)
        
        if target:
            print(f"\n[DECISION] Energy critical ({bot.energy_reserve:.1f}J). AI recommends consuming {target.name}.")
            bot.consume_component(target.name)
            
        bot.tick()
        
        if ticks % 5 == 0:
            status = bot.get_status()
            active_legs = [c for c in status['components'] if "Leg" in c]
            print(f"Tick {ticks} | Energy: {bot.energy_reserve:.1f}J | Mass: {bot.current_mass:.1f}kg | Legs: {len(active_legs)}")

        if not any(c for c in bot.components if not c.is_consumed and c.criticality < 1.0) and bot.energy_reserve < 500:
            print("\n[FINAL STATE] No more consumable parts. Robot is entering hibernation/shutdown.")
            break
            
        time.sleep(0.1)

    print("-" * 50)
    print(f"Mission ended after {ticks} ticks.")
    print(f"Final Mass: {bot.current_mass}kg")

if __name__ == "__main__":
    run_simulation()
