
def jaccard_similarity(list1, list2):
    """
    Simple Jaccard Similarity.
    """
    s1 = set(list1)
    s2 = set(x.lower() for x in list2)
    itersection = len(s1.intersection(s2))
    union = (len(list1) + len(list2)) - itersection
    return itersection / union


def weighted_jaccard_similarity(factor_details, dimension_details):
    """
    weighted Jaccard Similarity, aligns the signs of the factors and
    dimensions.
    """
    new_pos = [x for x in factor_details.index if factor_details[x] > 0]
    new_neg = [x for x in factor_details.index if factor_details[x] < 0]

    orig_pos = [x for x in dimension_details.index if dimension_details[x] > 0]
    orig_neg = [x for x in dimension_details.index if dimension_details[x] < 0]

    j_pospos = jaccard_similarity(new_pos, orig_pos)
    j_negneg = jaccard_similarity(new_neg, orig_neg)
    aligned_sum = j_pospos + j_negneg
    j_posneg = jaccard_similarity(new_pos, orig_neg)
    j_negpos = jaccard_similarity(new_neg, orig_pos)
    unaligned_sum = j_posneg + j_negpos

    j_sum = sum([j_pospos, j_negneg, j_posneg, j_negpos]) / 2

    if aligned_sum != 0 and unaligned_sum != 0:
        # this happens for popProfessional's Factor 5, a term appears in both
        # factor and dimension, but with different signs.
        j_sum = max(aligned_sum, unaligned_sum) / 2

    return j_sum


def calc_jaccard_with_hexaco(agent_df, hexaco_df):
    """
    Calculate Jaccard Similarity between agent_df and hexaco_df.
    """
    import pandas as pd
    values = pd.DataFrame(columns=hexaco_df.columns, index=agent_df.columns)
    for factor in agent_df:
        factor_terms = agent_df[factor].dropna()
        for dim in hexaco_df:
            dim_terms = hexaco_df[dim].dropna()
            jaccard = weighted_jaccard_similarity(factor_terms, dim_terms)
            values.loc[factor, dim] = jaccard
    return values
