class Paddle():
    def __init__(self, x, y, width, height, speed, rect, is_vertical):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = rect
        self.is_vertical = self.is_vertical

    def get_rect_paddle(self):
        print('se a atividade permitisse usar pygame, o objeto tipo pygame.Rect do jogador seria gerado agora')

    def move_paddle(self, left = bool):
        movement_axis = 0
        movement_direction = 1
        if left:
            movement_direction = -1
        if self.is_vertical == True:
            self.y += self.speed * movement_direction
        else:
            self.x += self.speed * movement_direction

        print(f'se a atividade permitisse usar pygame, o objeto rect do jogador estaria na posição x:{self.x} y:{self.y}')
        
    
    def get_hit_area(self):
        print('não sei o que é pra essa parte fazer')

        

    def resize_paddle(self, factor, is_replacement_size = False):
        if is_replacement_size:
            self.width = factor
        else:
            self.width += factor

        print(f'se a atividade permitisse usar pygame, a largura do objeto rect do jogador agora seria {self.width}')
    
    
    def draw_paddle(self):
        print('se a atividade permitisse usar pygame, o objeto tipo pygame.Rect do jogador seria renderizado na tela agora')