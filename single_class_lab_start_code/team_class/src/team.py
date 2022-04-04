class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        for person in self.players:
            if person == player:
                return True
        return False


    def play_game(self, win):
        if win:
            self.points += 3
