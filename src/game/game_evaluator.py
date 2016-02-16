import src.game.settings as settings


def testFixed(fixedPlacements):
    # test vertical matches
    for col in range(0, settings.NUM_COLS):
        for player in (1, 2):
            winning = True
            for row in range(0, settings.NUM_ROWS):
                if (col, row) in fixedPlacements:
                    winning &= fixedPlacements[(col, row)] == player
                else:
                    winning = False
            if winning:
                return player

    # test horizontal matches
    for row in range(0, settings.NUM_ROWS):
        for player in (1, 2):
            winning = True
            for col in range(0, settings.NUM_COLS):
                if (col, row) in fixedPlacements:
                    winning &= fixedPlacements[(col, row)] == player
                else:
                    winning = False
            if winning:
                return player

    # test diagonals
    if not settings.NUM_COLS == settings.NUM_ROWS:  # if not a square playing field, then diagonals don't make sense
        return -1

    for player in (1, 2):
        winning = True
        for point in range(0, settings.NUM_COLS):
            if (point, point) in fixedPlacements:
                winning &= fixedPlacements[(point, point)] == player
            else:
                winning = False
        if winning:
            return player

    for player in (1, 2):
        winning = True
        for point in range(0, settings.NUM_COLS):
            if (point, settings.NUM_COLS - 1 - point) in fixedPlacements:
                winning &= fixedPlacements[(point, settings.NUM_COLS - 1 - point)] == player
            else:
                winning = False
        if winning:
            return player
    return -1


def evaluate(moves=[], fixedPlacements=None, recursive_step=0):
    if fixedPlacements is None:
        fixedPlacements = dict()

    scores = dict()
    scores[-1] = 0
    scores[1] = 0
    scores[2] = 0

    if len(moves) <= recursive_step:
        scores[testFixed(fixedPlacements)] = 1
        return scores

    current_move = moves[recursive_step]
    recursive_step += 1

    total_placed = 0  ##total placed controls for move attempts that cannot be done because an earlier step in the recursion chose it

    for key in current_move.distribution:
        if current_move.distribution[key] > 0:
            newFixedPlacements = fixedPlacements.copy()
            if not key in fixedPlacements:  ##if the move hasn't already been fixed
                total_placed += current_move.distribution[key]
                fixedPlacements[key] = current_move.player
                newscores = evaluate(moves, newFixedPlacements, recursive_step)
                for player in newscores:
                    scores[player] += current_move.distribution[key] * newscores[player]

    if total_placed == 0: ##we couldn't do ANY moves
        scores[-1]=1
        return scores

    for player in scores:
        scores[player]/=total_placed

    return scores