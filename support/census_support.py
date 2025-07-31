top_levels_labels = {
    -1: 'Retired',
    0: 'Students, Job Seekers, Unpaid Carers',
    1: '(1)Managers, Directors and Senior Officials',
    2: '(2)Professional Occupations',
    3: '(3)Associate Professional and Technical Occupations',
    4: '(4)Administrative and Secretarial Occupations',
    5: '(5)Skilled Trades Occupations',
    6: '(6)Caring, Leisure and Other Service Occupations',
    7: '(7)Sales and Customer Service Occupations',
    8: '(8)Process, Plant and Machine Operatives',
    9: '(9)Elementary Occupations',
}

def oc_top_level(oc):
    """ 
    Utility function to return the top-level occupation code.
    or -1 for retired, 0 for students/job seekers/unpaid carers etc.
    """
    try:
        if oc == 0:
            return 0
        if oc < 0:
            return -1
        return int(str(oc)[0])
    except (ValueError):
        print(f"Error: {oc} at")
        return 0

def plot_against_ONS_top_level_percentages(df, colour=None):
    """
    Pretty looking plot of the top-level occupation codes against the ONS Census 2021 percentages.
    """
    import matplotlib.pyplot as plt
    import pandas as pd

    ocs = df['OC'].apply(oc_top_level)
    df_counts = pd.DataFrame(ocs.value_counts().rename('Count'))
    df_counts['Percentage'] = (df_counts['Count'] / df_counts['Count'].sum())*100

    for x in top_levels_labels.keys():
        if x not in df_counts.index:
            df_counts.loc[x] = 0

    df_counts.drop(df_counts.index[df_counts.index <= 0], axis=0, inplace=True)
    df_counts = df_counts.sort_index(ascending=False)

    colormap = plt.colormaps.get_cmap('tab20b')

    english_percent = [12.9, 20.3, 13.3, 9.3, 10.2, 9.3, 7.5, 6.9, 10.5]
    english_percent.reverse()
    welsh_percent = [10.5, 18.2, 11.8, 9.4, 12.2, 11.2, 8.4, 7.9, 10.5]
    welsh_percent.reverse()

    fig, ax = plt.subplots()
    if not colour:
        colour = colormap.colors[16]
    ax.barh(y=df_counts.index-0.3, height=0.3, width=df_counts['Percentage'], color=colour, alpha=0.7, label=f'Agent Population ({len(ocs)})')
    ax.barh(y=df_counts.index, height=0.3, width=english_percent, color=colormap.colors[2], alpha=0.7, label=f'Census, 2021, England')
    ax.barh(y=df_counts.index+0.3, height=0.3, width=welsh_percent, color=colormap.colors[3], alpha=0.7, label=f'Census, 2021, Wales')

    plt.xticks(fontsize=8)
    plt.xlabel('Percentage (%)')
    plt.yticks(df_counts.index, [top_levels_labels[x] for x in df_counts.index], fontsize=8)
    plt.ylabel('Occupation Code')
    ax.invert_yaxis()
    plt.legend(loc='lower right', fontsize=9)
    plt.show()
    
def plot(df_pop):
    """
    drop those without an occupation code, and plot against 2021 percentages.
    """
    df_employed = df_pop.copy()
    df_employed = df_employed.drop(df_employed[df_employed['OC'] <= 0].index)
    plot_against_ONS_top_level_percentages(df_employed, colour='skyblue')