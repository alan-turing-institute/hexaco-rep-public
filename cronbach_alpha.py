
def calc_cronbachs_alpha(df):
    """
    Calculate the Cronbach's alpha for a given DataFrame.
    :param df: DataFrame
    :return: float
    """
    import pandas as pd

    k = len(df.columns)
    totals = []
    for i in df.index:
        totals.append(df.sum(axis=1)[i])

    variance_total_score = pd.Series(totals).var()
    s2 = df.var(axis=0)
    summation_item_vars = s2.sum()
    alpha = (k / (k - 1)) * (1 - (summation_item_vars / variance_total_score))
    return alpha
