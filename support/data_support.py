

def fix_name(x):
    """
    Used to translate the 'Full Name' from the population file, into
    an index value for results files.

    :param x: 'Full Name' from population file, i.e. 'Dave Smith'
    :return: 'DaveSmith'
    """
    return x.replace(' ', '').split('.')[0]


def load_hexaco_data(loadings_file='hexaco_loadings.csv'):
    """
    Load the HEXACO data as presented in the 2004 paper.
    """
    import pandas as pd
    loadings = pd.read_csv(loadings_file)
    loadings.columns = ['Agreeableness', 'a-loadings',
                        'Extraversion', 'x-loadings',
                        'Conscientiousness', 'c-loadings',
                        'Emotionality', 'e-loadings',
                        'Openness', 'o-loadings',
                        'Honesty-Humility', 'h-loadings']

    labels = [x for x in loadings.columns if '-load' not in x]
    loading_labels = [x for x in loadings.columns if '-load' in x]

    data = {}
    index = []

    for idx, label in enumerate(labels):
        _weights = loadings[loading_labels[idx]].dropna()
        _adjs = [x.lower().strip() for x in loadings[labels[idx]].dropna()]
        _weights.index = [x.lower().strip() for x in _adjs]
        index += _weights.index.tolist()
        data[label] = _weights

    return pd.DataFrame(data, index=index)


def load_agent_data(file_path, factor_name_mapping=None):
    """
    Load agent (highest loaded) terms in same format as load_hexaco_data().
    """
    import pandas as pd

    df = pd.read_csv(file_path, index_col=0)
    loadings = {df.columns[i]: df.iloc[:, i].abs().nlargest(30) for i in range(df.shape[1])}

    data = {}
    index = []

    labels = [f'Factor{i+1}' for i in range(len(df.columns))]

    for idx, label in enumerate(df.columns):
        _weights = loadings[label].dropna()
        _adjs = [x.lower().strip() for x in loadings[label].dropna().index]
        _weights.index = [x.lower().strip() for x in _adjs]
        index += _weights.index.tolist()
        data[labels[idx]] = _weights

    return pd.DataFrame(data, index=index)
