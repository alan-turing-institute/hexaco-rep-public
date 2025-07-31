def get_antonym_pairs(adjs):
    """
    Get pairs of antonyms from a list of adjectives.
    """
    _pairs = []

    for a in adjs:
        if 'un'+a in adjs:
            _pairs.append((a, 'un'+a))
        if 'in'+a in adjs:
            _pairs.append((a, 'in'+a))
        if 'dis'+a in adjs:
            _pairs.append((a, 'dis'+a))        
        if 'im'+a in adjs:
            _pairs.append((a, 'im'+a))
        if 'ir'+a in adjs:
            _pairs.append((a, 'ir'+a))        
        if 'non'+a in adjs:
            _pairs.append((a, 'non'+a))  
        if 'il'+a in adjs:
            _pairs.append((a, 'il'+a))  
        if 'a'+a in adjs:
            _pairs.append((a, 'a'+a))
        if 'de'+a in adjs:
            _pairs.append((a, 'de'+a))
            
    return _pairs


# ratings are on a scale from 1 to 9, inclusive.
min_rating = 1
max_rating = 9

def calc_consistency_score(responses_df, adj1, adj2):
    """
    Used to provide a value for consistency in an agents responses to a pair of antonyms.
    Basically a standardised distance from the center, for both adjectives, which when 
    added together *should* result in 0 if the responses are consistent.

    Consistent means both values have same distance from '5': 'Neither Agree nor Disagree'.

    A threshold of 0.75 allows the answers to be two 'ratings' out, 0.875 allows the 
    answers to be only on 'rating' out.

    Return values:
     - a float between 0 and 1.
     - 1 means fully consistent i.e. 1:9, 2:8, 7:3, etc.
     - 0 means fully inconsistent i.e. 7:7, 4:4, etc.
    """
    standardized_adj1 = 2 * (responses_df[adj1] - min_rating) / (max_rating - min_rating) - 1
    standardized_adj2 = 2 * (responses_df[adj2] - min_rating) / (max_rating - min_rating) - 1

    diff = abs(standardized_adj1 + standardized_adj2)
    return 1 - (diff / 2)


def get_consistency_scores(responses_df, pairs):
    """
    Returns a dictionary of consistency scores for each pair of antonyms.
    """
    import pandas as pd
    consistency_df = pd.DataFrame(index=responses_df.index, columns=[f"{adj1}-{adj2}" for adj1, adj2 in pairs])
    for adj1, adj2 in pairs:
        if adj1 in responses_df.columns and adj2 in responses_df.columns:
            consistency_df[f"{adj1}-{adj2}"] = responses_df.apply(lambda x: calc_consistency_score(x, adj1, adj2), axis=1)
    return consistency_df


def calc_biography_lengths(pop):
    """
    Calculate the lengths of biographies in a population set.
    """
    results = {}
    for n in pop:
        name = n['Full Name'].replace(' ','') if '.' not in n['Full Name'] else "".join(n['Full Name'].split('.')[:-1]).replace(' ','')
        length = len("".join(n['Hobbies/Interests']))
        if type(n['Personality Facts']) == list:
            length += len("".join(n['Personality Facts']))
        elif type(n['Personality Facts']) == dict:
            length += len("".join(n['Personality Facts'].values()))
        results[name] = length
    return results


def plot_consistency_vs_biography_length(df):
    """
    plot the biography lengths against the consistency scores.
    """
    import matplotlib.pyplot as plt
    df.plot(kind='scatter', x='total', y='consistency', color='skyblue', edgecolor='navy', alpha=0.5, figsize=(5, 4))
    plt.title('Consistency Scores vs Biography Length (in characters)', fontsize=10)
    plt.xlabel('\nBiography length in characters', fontsize=10)
    plt.ylabel('Agent consistency score\n', fontsize=10)
    plt.gca().yaxis.set_tick_params(labelsize=10)
    plt.gca().xaxis.set_tick_params(labelsize=10)
    plt.show()
    
    
def plot(population, responses):
    """
    Calculates and plots the consistency scores against the biography lengths.
    """
    import pandas as pd
    pairs = get_antonym_pairs(responses.columns.tolist())
    consistencies = get_consistency_scores(responses, pairs).mean(axis=1).sort_values()
    lengths = calc_biography_lengths(population)
    df = pd.concat([consistencies, pd.DataFrame.from_dict(lengths, orient='index')], axis=1)
    df.columns = ['consistency', 'total']
    plot_consistency_vs_biography_length(df)
