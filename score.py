class Score:
    def __init__(self, score):
        self.score = score

    def show_score(self):
        print(f"Pontuação: {self.score}")

    def update_score(self, brick_color, points):
        self.score += points
        self.show_score()
        print(f"A pontuação aumentou em {points} pelo tijolo {brick_color}")

    def red_bricks(self):
        self.update_score("vermelho", 3)

    def green_bricks(self):
        self.update_score("verde", 5)

    def blue_bricks(self):
        self.update_score("azul", 7)

    def yellow_bricks(self):
        self.update_score("amarelo", 9)

    def reset_score(self):
        self.score = 0
        print(f"Pontuação zerada")
        self.show_score()