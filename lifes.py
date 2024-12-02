class Life:
    def __init__(self, life):
        self.life = life
        self.full_life = 100

    def show_life(self):
        print("Vida: ",self.life)
    
    def lose_life(self):
        self.lost_life = 20
        self.life -= self.lost_life
        self.show_life()
        print(f"A vida diminuiu em {self.lost_life}")
        
    def reset_life(self):
        self.life = self.full_life
        self.show_life()
        print(f"A vida resetou para {self.full_life}")
