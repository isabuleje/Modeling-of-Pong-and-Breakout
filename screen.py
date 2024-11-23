class Screen:
    def __init__(self, left_limit, right_limit, bottom_limit, up_limit):
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.bottom_limit = bottom_limit
        self.up_limit = up_limit

    def create_edges(self):