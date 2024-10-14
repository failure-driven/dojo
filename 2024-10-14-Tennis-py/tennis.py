class Game:
    SCORES = {
            0: "love",
            1: "15",
            2: "30",
            3: "40",
            }

    def __init__(self):
        self.int_score = {
                "server": 0,
                "receiver": 0
                }

    def point(self, player):
        self.int_score[player] += 1

    def score(self):
        return self.deuce_score() or \
            self.advantage_score() or \
            self.winning_score() or \
            self.normal_score()

    def deuce_score(self):
        if min(self.int_score.values()) > 2 and \
                min(self.int_score.values()) == \
                max(self.int_score.values()):
            return "deuce"

    def advantage_score(self):
        if min(self.int_score.values()) > 2 \
                and max(self.int_score.values()) - \
                min(self.int_score.values()) == 1:
            return f"advantage {self.leading()}"

    def winning_score(self):
        if max(self.int_score.values()) > 3:
            return f"game {self.leading()}"

    def normal_score(self):
        output = [
            self.SCORES[self.int_score["server"]],
            self.SCORES[self.int_score["receiver"]]
        ]
        if len(set(output)) == 1:
            output[1] = "all"
        return ' '.join(output)

    def leading(self):
        return "server" if self.int_score["server"] > \
                self.int_score["receiver"] \
                else "receiver"
