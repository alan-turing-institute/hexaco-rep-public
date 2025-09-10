

def read_in_lexical_scores(file='data/popc_results.csv', verbose=False):
    """
    Return the lexical scores (1..9) from the lexical survey (1702x310) 
    as a DataFrame.
    """
    import pandas as pd
    scores = pd.read_csv(file, index_col=0)
    to_fix = [x for x in scores.index if "'" in x]
    if verbose:
        print(f'Fixing names: {", ".join(to_fix)}.')
    for n in to_fix:
        scores.rename(index={n:n.replace("'", '')}, inplace=True)
    if verbose:
        print(f"Read in {len(scores)} responses from {file}")
    return scores


def read_in_loadings(file='intermediate/loadings_popc_10.csv', factor_labels=None):
    """
    Return the PCA loadings - terms(adjectives) and weights for each factor, 
    as loaded from file. 
    """
    import pandas as pd
    loadings = pd.read_csv(file, index_col=0)
    if factor_labels:
        loadings.columns = factor_labels
    return loadings


def calculate_agent_scores(lexical_scores, factor_loadings):
    """
    Calculate scores for each agent, based on the recovered factors' loadings.
    Returns a DataFrame with the scores for each factor.
    """
    import numpy as np
    import pandas as pd

    df = pd.DataFrame(index=lexical_scores.index)
    for factor in factor_loadings.columns:
        terms = list(factor_loadings[factor].dropna().index)
        weights = factor_loadings[factor].dropna()
        scores = [x-5 for x in lexical_scores[terms].values]
        scores = np.array(scores)
        scores = scores * weights.values
        df[factor] = scores.sum(axis=1)

    return df


def calc_pearsons_matching_factors(df1, df2):
    """
    Calculate Pearson's r between the columns of df1 and df2.
    It does expect each dataframe to have the same column names.
    """
    import pandas as pd
    from scipy.stats import pearsonr

    results_df = pd.DataFrame(index=df1.columns)
    for dim in df1.columns:
        r, p_value = pearsonr(df1[dim], df2[dim])
        results_df.loc[dim, 'r'] = r
        results_df.loc[dim, 'p_value'] = p_value

    results_df = results_df.round(3)
    results_df.columns = ['r', 'p']
    return results_df
