class PlayerStats:
    def __init__(self):
        self.attempts = 0
        self.makes = 0

    def record_shot(self, success):
        self.attempts += 1
        if success:
            self.makes += 1

    def shooting_percentage(self):
        if self.attempts == 0:
            return 0
        return (self.makes / self.attempts) * 100
