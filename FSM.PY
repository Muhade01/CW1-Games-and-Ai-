class EnemyFSM:
    def __init__(self):
        self.state = "idle"

    def update(self, player_detected):
        if self.state == "idle" and player_detected:
            self.state = "chase"
        elif self.state == "chase" and not player_detected:
            self.state = "idle"

    def get_state(self):
        return self.state

# Test the FSM
enemy = EnemyFSM()
print("Initial State:", enemy.get_state())  # Expected: idle

enemy.update(player_detected=True)
print("State after detecting player:", enemy.get_state())  # Expected: chase

enemy.update(player_detected=False)
print("State after losing player:", enemy.get_state())  # Expected: idle
