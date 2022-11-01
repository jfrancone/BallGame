from paddle import Paddle

class User_Paddle(Paddle):

    def __init__(Self, position, player_num):
        super().__init__(position, player_num)
        self.username = f"Player {player_num}"


class AI_Paddle(Paddle):

    def __init__(Self):
        super().__init__(position, player_num)
        self.username = "Player 2"