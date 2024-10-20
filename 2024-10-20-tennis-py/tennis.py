SERVER = "server"
RECEIVER = "receiver"
ADVANTAGE_DIFF = 1
NORMAL_SCORE = {
        0: "love",
        1: "15",
        2: "30",
        3: "40"
        }


def tennis(points=[]):
    score = setup_score(points)
    return advantage_score(score) or \
        winning_score(score) or \
        normal_score(score)


def setup_score(points):
    score = {SERVER: 0, RECEIVER: 0}
    for point in points:
        score[point] += 1
    return score


def leading(score):
    return max([p for p in score.keys()], key=lambda x: score[x])


def advantage_score(score):
    if score_abs_eq_one(score) and above_normal_score(score):
        return f"advantage {leading(score)}"


def winning_score(score):
    if score_abs_gte_two(score) and above_normal_score(score):
        return f"game {leading(score)}"


def normal_score(score):
    scores = [
            NORMAL_SCORE[score[SERVER] or 0],
            NORMAL_SCORE[score[RECEIVER] or 0]
            ]
    if max(score.values()) == min(score.values()):
        scores = [scores[0], "all"]
    return " ".join(scores)


def above_normal_score(score):
    return max(score.values()) > max(NORMAL_SCORE.keys())


def score_abs_gte_two(score):
    return (max(score.values()) - min(score.values())) > ADVANTAGE_DIFF


def score_abs_eq_one(score):
    return (max(score.values()) - min(score.values())) == ADVANTAGE_DIFF
