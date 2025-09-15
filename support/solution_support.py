

def load_or_generate_solutions(pop_label, sol_range):
    """
    Load or generate PCA solutions for the PopCensus dataset.
    """
    from os.path import exists
    import pandas as pd
    from results_template import setup
    
    solutions = {}
    for s in sol_range:
        if exists(f'intermediate/loadings_pop{pop_label}_{s}.csv'):
            solutions[s] = pd.read_csv(f'intermediate/loadings_pop{pop_label}_{s}.csv', index_col=0)
        else:
            solutions[s] = setup(s, f'data/pop{pop_label}_ipsatised_results.csv', 
                                f'intermediate/loadings_pop{pop_label}_{s}.csv')
    return solutions


def calc_cronbachs_across_solutions(solutions, ipsatised_data):
    """
    Calculate Cronbach's alpha across different solutions.
    """
    from statistics import mean
    from support.cronbach_alpha import calc_cronbachs_alpha
    results = {}
    mean_alphas = []

    for n_factors, ldgs in solutions.items():

        top_loadings = {ldgs.columns[i]: ldgs.iloc[:, i].abs().nlargest(30).index for i in range(ldgs.shape[1])}

        alphas = []
        for dim in top_loadings:
            cols = top_loadings[dim]
            df_ = ipsatised_data[cols]
            alpha = calc_cronbachs_alpha(df_)
            alphas.append(alpha)

        results[n_factors] = alphas
        mean_alphas.append(mean(alphas))
        
    max_length = 12
    results = {k: v + [None] * (max_length - len(v)) for k, v in results.items()}
    return results, mean_alphas


def plot(df, xlabel, ylabel):
    import matplotlib.pyplot as plt
    import seaborn as sns
   
    plt.figure(figsize=(5, 3.4))
    plt.rc('font', family='Times New Roman')

    textsize = 9
    
    sns.heatmap(
        df,
        annot=True,
        fmt=".2f",
        cmap=plt.cm.RdBu,
        alpha=0.6,
        linewidths=0.7,
        annot_kws={"fontsize": textsize-1},
        vmin=-1.5,
        vmax=1.5,
        cbar=False
    )

    plt.xlabel(xlabel, fontsize=textsize)
    plt.xticks(rotation=0, fontsize=textsize)
    plt.ylabel(ylabel, fontsize=textsize)
    plt.yticks(rotation=0, fontsize=textsize)

    plt.tight_layout()
    plt.show()


def plot_cronbachs_for_population(population='c'):
    """ 
    Prepare DataFrame for plotting Cronbach's alpha across PCA solutions.
    Support for Fig3.
    """
    import pandas as pd
    from IPython.display import display
    
    solutions = load_or_generate_solutions(population, range(5, 13))
    ipsatised_data = pd.read_csv(f'data/pop{population}_ipsatised_results.csv', index_col=0)                
    results, mean_alphas = calc_cronbachs_across_solutions(solutions, ipsatised_data)

    df = pd.DataFrame.from_dict(results, orient='index').T
    df.index = [f"{i+1}" for i in range(df.shape[0])]
    df.columns = [f"{x} ({mean_alphas[i]:.2f})" for i, x in enumerate(df.columns)]
    
    plot(df, "Solutions (mean alpha) - Pop" + ("Census" if population == 'c' else "Professional"), "Factors")
    return df
