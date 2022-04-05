class Player:

    def __init__(self, name, car):
        self.name = name
        self.car = car
        self.boost = 100
        self.shots = 0
        self.goals = 0
        self.saves = 0

    def shoot(self):
        self.shots += 1
        
    def save(self): 
        self.saves += 1 
        
