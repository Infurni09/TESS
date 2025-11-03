# Bayesian Knowledge Tracing implementation (simple)
MASTERY_THRESHOLD = 0.95

class BKT:
    def __init__(self, learn=0.15, slip=0.1, guess=0.2):
        self.learn = learn
        self.slip = slip
        self.guess = guess

    def update(self, prior, correct):
        p = float(prior)
        if correct:
            num = p * (1 - self.slip)
            den = num + (1 - p) * self.guess
            posterior = num / den if den > 0 else p
        else:
            num = p * self.slip
            den = num + (1 - p) * (1 - self.guess)
            posterior = num / den if den > 0 else p
        posterior = posterior + (1 - posterior) * self.learn
        return min(1.0, posterior)
