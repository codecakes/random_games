def prob_conditional(outcome_condition):
    """
    p(outcome1 | condition1)
    p(outcome2 | condition2)
    """
    return [k[0] * k[1] for k in outcome_condition]
