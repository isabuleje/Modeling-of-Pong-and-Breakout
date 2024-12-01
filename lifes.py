class Life:
    def __init__(self, life):
        self.life = life
        self.full_life = self.life

    def show_life(self):
        print("Vida: ",self.life)

    def lose_life(self):
        self.life -= 20
        print("A vida diminuiu")
        
    def reset_life(self):
        self.life = self.full_life
        print("A vida resetou para 100")
        print("")