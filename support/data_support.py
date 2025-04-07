

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
    loadings.dropna(how='all', axis=1, inplace=True)
    loadings.dropna(how='all', axis=0, inplace=True)
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
