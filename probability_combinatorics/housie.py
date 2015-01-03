"""So the story goes,
that one night on NYE,
we were all 150,
Playing out a game of Housie.

Nice Poem. But what were the chances of us winning if we were a team of 9 out of 150?"""

def win_chance(num, den, game_type, ppl_win_prob = 1):
    """
    Successive wins not necessarily consecutive wins,
    in a game of Housie for Full Houses, Lines.

    num: Team strength
    den: Total crowd
    game_type: Full Houses, Lines, Corners, etc
    ppl_win_prob: Trials allowed = number of ppl to win the game in successive trials. Implies as many unique people allowed as many trials exist.

    Returns: Probability of the game type with given ppl_win_prob
    """
    div = 1
    game_type = game_type.lower()
    if num <= den:
        if game_type in ('full house', 'line') and 0 < ppl_win_prob <= num:
            for _ in xrange(ppl_win_prob):
                #print num, den,
                div *= float(num)/den
                num -= 1
                den -= 1
                #print i, div
        else:
            div = float(num)/den
        return div
    return 0

if __name__ == "__main__":

    ##Full House or lines
    #best case
    print win_chance(9,150,'full house', 1)

    #worst case
    print win_chance(9,150,'full house', 9)


    print win_chance(9,150,'corner', 9)

    print sum([win_chance(9,150, game, trials_num) for game in ('full house', 'corner', 'line') for trials_num in (1,9)])
