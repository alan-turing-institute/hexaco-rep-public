

def plot_jaccards(solution_name, data, color='Blues'):
    import seaborn as sns
    import matplotlib.pyplot as plt

    df_data = data.astype(float)
    df_data = df_data[['Honesty-Humility', 'Emotionality', 'Extraversion', 
                       'Agreeableness', 'Conscientiousness', 'Openness']]
    df_data.columns = ['H', 'E', 'X', 'A', 'C', 'O']
    df_data = df_data.T
    width = len(df_data.index) * 0.75
    plt.figure(figsize=(width, 4))
    ax = sns.heatmap(df_data,
                     cmap=sns.color_palette(color, as_cmap=True),
                     linewidths=0.5,
                     annot=True,
                     vmin=0, vmax=0.10) 
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.set_ylabel('Hexaco Dimensions\n')
    ax.set_xlabel(f'\n{solution_name}')
    ax.set_title(f'Weighted Jaccard Similarity for {solution_name} solution\n', fontsize=10)
    plt.show()


def plot_internal_sims(data, n_factors):
    import matplotlib.pyplot as plt
    import numpy as np
    
    all_means = data['means']
    all_errors = data['stds']
    all_labels = data.index
    
    import seaborn as sns
    # sns.set_theme(style='white', font='Times New Roman')
    palette = sns.color_palette("colorblind", n_colors=3)
    bar_colors = ([palette[0]]*n_factors) + ([palette[2]]*1) + ([palette[1]]*6)

    import matplotlib.patches as mpatches
    p1 = mpatches.Patch(color=palette[0], alpha=0.5, label='Recovered Factors')
    p2 = mpatches.Patch(color=palette[1], alpha=0.5, label='HEXACO Dimensions')
    p3 = mpatches.Patch(color=palette[2], alpha=0.5, label='Random Baseline')

    # plot it!
    pos = np.arange(len(all_means)) 
    fig = plt.figure(figsize=(7, 4))
    plt.barh(pos, all_means, xerr=all_errors, capsize=5, alpha=0.5, color=bar_colors)
    plt.yticks(pos, all_labels, rotation=0, ha='right')
    fig.gca().invert_yaxis()
    plt.xlabel("Semantic Similarity Score")
    plt.title("Similarity of terms found in Recovered Factors, HEXACO and Random Baseline")
    plt.legend(handles=[p1, p3, p2], bbox_to_anchor=(1.04, 1))
    plt.tight_layout()
    plt.show()


def plot_hexaco_sims(df):
    import matplotlib.pyplot as plt
    import numpy as np
    colors = plt.colormaps['tab10'](np.linspace(0, 1, 6))
    
    import seaborn as sns
    # sns.set_theme(style='white', font='Times New Roman')
    colors = sns.color_palette("colorblind", n_colors=12)
    colors = [colors[x] for x in range(0, 12, 2)]
    
    # plt.rcParams['font.family'] = 'Times New Roman'
    df.plot(kind='bar', figsize=(7, 4), color=colors, legend=True)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
