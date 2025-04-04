
from IPython.display import display, Markdown, HTML
import pandas as pd
import numpy as np


def setup(n_factors, data_file, intermediate_file):
    from support.pca_support import perform_pca
    ipsatised_data = pd.read_csv(data_file, index_col=0)
    results_file = intermediate_file
    results_file = perform_pca(data_file, n_factors, intermediate_file)
    loadings = pd.read_csv(results_file, index_col=0)
    loadings.columns = [f'Factor{x}' for x in range(1, n_factors+1)]
    print(f"Loadings shape = {loadings.shape}")
    return ipsatised_data, loadings


def report_variance_explained(loadings):
    explained_variance = np.sum(loadings**2, axis=0)
    variances = [x/len(loadings)*100 for x in explained_variance]
    print("variances: "+", ".join([f"{x:.2f}%" for x in variances])+ f", cumulative: {sum(variances):.2f}%")


def display_highest_loadings(loadings, labels):
    from support.pca_support import get_highest_loadings
    highest_loadings, pp = get_highest_loadings(30, loadings)
    agent_loadings_df = pd.DataFrame(highest_loadings)
    pp.columns = [pp.columns[x]+'('+labels[x]+')' for x in range(len(pp.columns))]
    display(HTML(pp.to_html()))
    return highest_loadings, agent_loadings_df


def report_cronbach_alphas(highest_loadings, ipsatised_data):
    from support.cronbach_alpha import calc_cronbachs_alpha as cronbach_alpha
    alphas = []
    for dim in highest_loadings:
        cols = highest_loadings[dim]
        df_ = ipsatised_data[cols.index]
        alpha = cronbach_alpha(df_)
        alphas.append(alpha)
    print("Cronbach's Alpha: "+", ".join([f"{x:.2f}" for x in alphas]))
    return alphas


def report_jaccards(agent_loadings_df, hexaco_data):
    from support.jaccard import calc_jaccard_with_hexaco
    js = calc_jaccard_with_hexaco(agent_loadings_df, hexaco_data)
    highest = list(zip(js.index, js.idxmax(axis=1), js.max(axis=1)))
    print("Highest Jaccard Similarities:")
    [print(f" * {a} -> {b}, ({c:.3f})") for a, b, c in list(highest)]
    return js


def report_internal_semantic_similarity(hldgs, labels, model):
    from support.semantic_similarity import compute_similarity
    scores = pd.DataFrame(columns='means stds'.split(), index=hldgs.keys())
    for i, m in enumerate(hldgs.keys()):
        ats = [x for x in hldgs[m].index if x in model]
        sim, _ = compute_similarity(ats, model)
        print(f"Average similarity for {m}({labels[i]}): {sim:.3f}")
        scores.loc[m, 'means'] = sim
        scores.loc[m, 'stds'] = 0
    return scores


def report_semantic_similarity_with_hexaco(hexaco_data, hldgs, model):
    from support.semantic_similarity import compute_similarity_between_sets
    results = pd.DataFrame(columns=hexaco_data.keys(), index=hldgs.keys())
    for factor in hldgs:
        factor_terms = [x for x in hldgs[factor].index]
        for dim in hexaco_data:
            dim_terms = [x for x in hexaco_data[dim].dropna().index]
            sim = compute_similarity_between_sets(factor_terms, dim_terms, model)
            results.loc[factor, dim] = sim
        print(f"Max similarity for {factor} = {results.loc[factor].max():.3f} ({results.loc[factor].idxmax()})")
    return results


def generate_results(n_factors,
                     population_name,
                     data_file,
                     intermediate_file,
                     factor_labels):
    from support.plots import plot_jaccards, plot_internal_sims, plot_hexaco_sims
    from support.data_support import load_hexaco_data
    from support.semantic_similarity import load_embedding_model

    display(Markdown(f"## PC & Results for {population_name}'s {n_factors} Solution."))

    ipsatised_data, ldgs = setup(n_factors, data_file, intermediate_file)
    hldgs, agent_data = display_highest_loadings(ldgs, factor_labels)
    report_variance_explained(ldgs)

    display(Markdown("### Cronbach's Alphas:"))
    report_cronbach_alphas(hldgs, ipsatised_data)

    display(Markdown("### Weighted Jaccards Similarity:"))
    hexaco_data = load_hexaco_data()
    jaccards = report_jaccards(agent_data, hexaco_data)
    solution_name = 'Promax 5 factors for PopCensus'
    plot_jaccards(solution_name, jaccards)

    display(Markdown("### Semantic Similarity (between terms within factors):"))
    model = load_embedding_model()
    int_sims = report_internal_semantic_similarity(hldgs, factor_labels, model)

    # add mean and stdev for random adjectives
    # (see random_similarity.ipynb)
    int_sims.loc['Random'] = [0.377694, 0.021589]

    # add mean and stdev(always 0) for hexaco dimensions
    # (see hexaco_similarity.ipynb)
    int_sims.loc['Agreeableness'] = [0.545, 0]
    int_sims.loc['Extraversion'] = [0.462, 0]
    int_sims.loc['Conscientiousness'] = [0.474, 0]
    int_sims.loc['Emotionality'] = [0.523, 0]
    int_sims.loc['Openness'] = [0.489, 0]
    int_sims.loc['Honesty-Humility'] = [0.492, 0]

    plot_internal_sims(int_sims, n_factors)

    display(Markdown("### Semantic Similarity with Hexaco dimensions:"))
    hexaco_sims = report_semantic_similarity_with_hexaco(hexaco_data, hldgs, model)
    display(HTML(hexaco_sims.to_html()))
    plot_hexaco_sims(hexaco_sims)
