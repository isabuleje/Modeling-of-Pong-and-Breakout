class Titles:
    def __init__(self, width, height, x, y, color, points, rows, rect):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.points = points
        self.rows = rows
        self.rect = rect

    def draw_bricks(self):
        print(f"Foram desenhados {self.rows} colunas com {self.rect} tilojos em cada um")
        
        
    def destroy_bricks(self):
        self.rect = None
        print("Todos os tijolos foram destruidos")
        
    def undestroy_bricks(self):
        print("Todos os tijolos foram restaurados")
        
        
    def check_collision(self,rect):
        