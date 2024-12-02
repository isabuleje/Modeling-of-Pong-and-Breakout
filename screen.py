class Screen:
    def __init__(self):
        self.screen_size = (720,720)

    def create_edges(self):
        '''Creates the white strip at the corner of the screen'''
        self.border_size = 20
        self.white_color_left = (0,0, self.screen_size[0], self.screen_size[1])
        self.white_color_right = (0,0, self.screen_size[0], self.screen_size[1])
        self.white_color_up = (0,0, self.screen_size[0], self.screen_size[1])
        print("As paredes brancas foram criadas")


    def screen_info(self):
        print(f"Tamanho da tela: {self.screen_size}")

    def change_sreen_size(self, new_screen_size):
        self.screen_size = new_screen_size
        print("O tamanho da tela foi mudado ")
