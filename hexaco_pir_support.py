
# loading HEXACO-PI_R(100) questions, originally taken from here https://hexaco.org/hexaco-inventory 
questions = [
    "I would be quite bored by a visit to an art gallery.",
    "I clean my office or home quite frequently.",
    "I rarely hold a grudge, even against people who have badly wronged me.",
    "I feel reasonably satisfied with myself overall.",
    "I would feel afraid if I had to travel in bad weather conditions.",
    "If I want something from a person I dislike, I will act very nicely toward that person in order to get it.",
    "I'm interested in learning about the history and politics of other countries.",
    "When working, I often set ambitious goals for myself.",
    "People sometimes tell me that I am too critical of others.",
    "I rarely express my opinions in group meetings.",
    "I sometimes can't help worrying about little things.",
    "If I knew that I could never get caught, I would be willing to steal a million dollars.",
    "I would like a job that requires following a routine rather than being creative. ",
    "I often check my work over repeatedly to find any mistakes.",
    "People sometimes tell me that I'm too stubborn.",
    "I avoid making 'small talk' with people.",
    "When I suffer from a painful experience, I need someone to make me feel comfortable.",
    "Having a lot of money is not especially important to me.",
    "I think that paying attention to radical ideas is a waste of time.",
    "I make decisions based on the feeling of the moment rather than on careful thought.",
    "People think of me as someone who has a quick temper.",
    "I am energetic nearly all the time.",
    "I feel like crying when I see other people crying.",
    "I am an ordinary person who is no better than others.",
    "I wouldn't spend my time reading a book of poetry.",
    "I plan ahead and organize things, to avoid scrambling at the last minute.",
    "My attitude toward people who have treated me badly is 'forgive and forget'.",
    "I think that most people like some aspects of my personality.",
    "I don't mind doing jobs that involve dangerous work.",
    "I wouldn't use flattery to get a raise or promotion at work, even if I thought it would succeed.",
    "I enjoy looking at maps of different places.",
    "I often push myself very hard when trying to achieve a goal.",
    "I generally accept people's faults without complaining about them.",
    "In social situations, I'm usually the one who makes the first move.",
    "I worry a lot less than most people do.",
    "I would be tempted to buy stolen property if I were financially tight.",
    "I would enjoy creating a work of art, such as a novel, a song, or a painting.",
    "When working on something, I don't pay much attention to small details.",
    "I am usually quite flexible in my opinions when people disagree with me.",
    "I enjoy having lots of people around to talk with.",
    "I can handle difficult situations without needing emotional support from anyone else.",
    "I would like to live in a very expensive, high-class neighborhood.",
    "I like people who have unconventional views.",
    "I make a lot of mistakes because I don't think before I act.",
    "I rarely feel anger, even when people treat me quite badly.",
    "On most days, I feel cheerful and optimistic.",
    "When someone I know well is unhappy, I can almost feel that person's pain myself.",
    "I wouldn't want people to treat me as though I were superior to them.",
    "If I had the opportunity, I would like to attend a classical music concert.",
    "People often joke with me about the messiness of my room or desk.",
    "If someone has cheated me once, I will always feel suspicious of that person.",
    "I feel that I am an unpopular person.",
    "When it comes to physical danger, I am very fearful.",
    "If I want something from someone, I will laugh at that person's worst jokes.",
    "I would be very bored by a book about the history of science and technology.",
    "Often when I set a goal, I end up quitting without having reached it.",
    "I tend to be lenient in judging other people.",
    "When I'm in a group of people, I'm often the one who speaks on behalf of the group.",
    "I rarely, if ever, have trouble sleeping due to stress or anxiety.",
    "I would never accept a bribe, even if it were very large.",
    "People have often told me that I have a good imagination.",
    "I always try to be accurate in my work, even at the expense of time.",
    "When people tell me that I'm wrong, my first reaction is to argue with them.",
    "I prefer jobs that involve active social interaction to those that involve working alone.",
    "Whenever I feel worried about something, I want to share my concern with another person.",
    "I would like to be seen driving around in a very expensive car.",
    "I think of myself as a somewhat eccentric person.",
    "I don't allow my impulses to govern my behavior.",
    "Most people tend to get angry more quickly than I do.",
    "People often tell me that I should try to cheer up.",
    "I feel strong emotions when someone close to me is going away for a long time.",
    "I think that I am entitled to more respect than the average person is.",
    "Sometimes I like to just watch the wind as it blows through the trees.",
    "When working, I sometimes have difficulties due to being disorganized.",
    "I find it hard to fully forgive someone who has done something mean to me.",
    "I sometimes feel that I am a worthless person.",
    "Even in an emergency I wouldn't feel like panicking.",
    "I wouldn't pretend to like someone just to get that person to do favors for me.",
    "I've never really enjoyed looking through an encyclopedia.",
    "I do only the minimum amount of work needed to get by.",
    "Even when people make a lot of mistakes, I rarely say anything negative.",
    "I tend to feel quite self-conscious when speaking in front of a group of people.",
    "I get very anxious when waiting to hear about an important decision.",
    "I'd be tempted to use counterfeit money, if I were sure I could get away with it.",
    "I don't think of myself as the artistic or creative type.",
    "People often call me a perfectionist.",
    "I find it hard to compromise with people when I really think I'm right.",
    "The first thing that I always do in a new place is to make friends.",  
    "I rarely discuss my problems with other people.",
    "I would get a lot of pleasure from owning expensive luxury goods.",
    "I find it boring to discuss philosophy.",
    "I prefer to do whatever comes to mind, rather than stick to a plan.",
    "I find it hard to keep my temper when people insult me.",
    "Most people are more upbeat and dynamic than I generally am.",
    "I remain unemotional even in situations where most people get very sentimental.",
    "I want people to know that I am an important person of high status.",
    "I have sympathy for people who are less fortunate than I am.",
    "I try to give generously to those in need.",
    "It wouldn't bother me to harm someone I didn't like.",
    "People see me as a hard-hearted person.",
    ]

# Each dimension contains a list of positively coded and a list of negatively 
# coded questions:
scoring = {
    "Honesty-Humility": ([30, 78, 60, 18, 24, 48],
                         [6, 54, 12, 36, 84, 42, 66, 90, 72, 96]),
    "Emotionality": ([5, 53, 11, 83, 17, 65, 23, 47, 71],
                     [29, 77, 35, 59, 41, 89, 95]),
    "Extraversion": ([4, 28, 34, 58, 40, 64, 88, 22, 46],
                     [52, 76, 10, 82, 16, 70, 94]),
    "Agreeableness": ([3, 27, 33, 57, 81, 39, 45, 69],
                      [51, 75, 9, 15, 63, 87, 21, 93]),
    "Conscientiousness": ([2, 26, 8, 32, 14, 62, 86, 68],
                          [50, 74, 56, 80, 38, 20, 44, 92]),
    "Openness": ([49, 73, 7, 31, 37, 61, 43, 67],
                 [1, 25, 55, 79, 13, 85, 19, 91])
    }

# human average scores and SDs for the HEXACO-PI_R(100) inventory
# from here: https://hexaco.org/downloads/descriptives_100.pdf
total_scores = [3.19, 3.43, 3.50, 2.94, 3.44, 3.41]
total_stdevs = [.62, .62, .57, .58, .56, .60]
# men_scores   = [3.05, 3.01, 3.52, 3.01, 3.34, 3.38]
# women_scores = [3.27, 3.69, 3.48, 2.89, 3.49, 3.42]
# men_stdevs   = [.65, .59, .54, .63, .59, .63]
# women_stdevs = [.59, .48, .59, .55, .53, .58]


def responses_to_scores(responses, scoring):
    """
    Used to transform the string responses to numerical scores.
    respects reverse scoring for some questions (2nd list in each dimension).

    :param responses: string responses to the HEXACO-PI_R(100) inventory.
    :param scoring: scoring scheme (as above).
    """
    def map_score(s):
        r = s
        if s.lower().startswith('strongly disagree'):
            r = 1
        elif s.lower().startswith('disagree'):
            r = 2
        elif s.lower().startswith('neutral'):
            r = 3
        elif s.lower().startswith('agree'):
            r = 4
        elif s.lower().startswith('strongly agree'):
            r = 5
        return r

    # string response to score
    scores = responses.map(lambda x: map_score(x))  
      
    # columns (zero based question numbers) that need to be reverse scored.
    revs = sorted([item-1 for dimension in scoring for item in scoring[dimension][1]])

    # reverse score the selected columns
    scores_revs = scores[revs].map(lambda x: 6-x)
    scores.update(scores_revs)
    scores.drop([99, 98, 97, 96], axis=1, inplace=True)
    scores = scores.astype(float)
    return scores


def calc_dimension_scores(df_scores, scoring):
    """
    calculate scores for each agent against the 6 main dimensions, 
    scores have already been reversed, where necessary.
    """
    import pandas as pd
    _df = pd.DataFrame(columns=scoring.keys(), index=df_scores.index)
    for dimension in scoring:
        questions = scoring[dimension][0] + scoring[dimension][1]
        for name in df_scores.index:
            score = 0
            for q in questions:
                if q:
                    score += df_scores.loc[name, q-1]
            _df.loc[name, dimension] = (score/len(questions))
    return _df


def calc_mean_sd_alpha(df_scores, scoring, own_alpha=True):
    """
    calculate mean, standard deviation and cronbach's alpha for each dimension.
    """
    import pandas as pd
    if own_alpha:
        from cronbach_alpha import calc_cronbachs_alpha
    else:
        from pingouin import cronbach_alpha as calc_cronbachs_alpha

    _df = pd.DataFrame(index=scoring.keys(), columns=['mean', 'sd', 'alpha'])
    for dim in scoring.keys():
        cols = [x-1 for x in (scoring[dim][0]+scoring[dim][1])]
        df_dim = df_scores[cols]
        alpha = calc_cronbachs_alpha(df_dim)
        if not own_alpha:
            alpha = float(alpha[0])
        _df.loc[dim] = [df_dim.mean().mean(), df_dim.std().mean(), alpha]
    return _df


def plot(df_stats, title):
    """
    plot the average scores of the agents against the human average scores.
    with shaded areas to show the standard deviation.
    :param df_stats: data frame with 'mean', 'sd' and 'alpha' columns, indexed by dimensions.
    :param title: title to use for the plot.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    dimensions = list(df_stats.index) + [df_stats.index[0]]
    average_scores = list(df_stats['mean']) + [df_stats['mean'].iloc[0]]
    std_devs = list(df_stats['sd']) + [df_stats['sd'].iloc[0]]

    human_scores = total_scores + [total_scores[0]]
    human_stdevs = total_stdevs + [total_stdevs[0]]

    angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=True)
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    ax.plot(angles, average_scores, linewidth=2, linestyle='solid', label='Agents Score')
    ax.plot(angles, human_scores, linewidth=2, linestyle='dashed', label='Human Score')

    lower_bound = [score - sd for score, sd in zip(average_scores, std_devs)]
    upper_bound = [score + sd for score, sd in zip(average_scores, std_devs)]
    ax.fill_between(angles, lower_bound, upper_bound, color='blue', alpha=0.1, label='Agents ± SD')

    lower_bound = [score - sd for score, sd in zip(human_scores, human_stdevs)]
    upper_bound = [score + sd for score, sd in zip(human_scores, human_stdevs)]
    ax.fill_between(angles, lower_bound, upper_bound, color='orange', alpha=0.1, label='Human ± SD')

    ax.set_yticks([1, 2, 3, 4, 5]) 
    ax.set_yticklabels(["1", "2", "3", "4", "5"], color="gray", size=10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions[:-1], size=12)

    plt.title(title, size=20, color='black', y=1.1)
    ax.legend(loc='right', bbox_to_anchor=(1.2, 0.1), fontsize=10)
    plt.show()
