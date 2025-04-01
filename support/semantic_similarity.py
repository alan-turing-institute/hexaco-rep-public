
def load_embedding_model():
    """
    Load FastText
    """
    from gensim.models import KeyedVectors

    def load_model_fasttext():
        fasttext_path = "model_data/cc.en.300.vec"
        model = KeyedVectors.load_word2vec_format(fasttext_path, binary=False)
        return model

    return load_model_fasttext()


def compute_similarity(my_terms, model):
    """
    Compute the similarity between terms in a group.
    """
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    similarity_matrix = np.zeros((len(my_terms), len(my_terms)))

    # compute the pairwise similarities
    for i, term1 in enumerate(my_terms):
        for j, term2 in enumerate(my_terms):
            if i == j:
                continue
            similarity_matrix[i, j] = cosine_similarity([model[term1]], [model[term2]])[0][0]

    # remove the lower triangle
    similarity_matrix = np.triu(similarity_matrix)
    max_sim_A_to_B = similarity_matrix.max(axis=1).mean()
    max_sim_B_to_A = similarity_matrix.max(axis=0).mean()
    average_similarity = (max_sim_A_to_B + max_sim_B_to_A) / 2
    return average_similarity, similarity_matrix


def compute_similarity_between_sets(my_terms, original_terms, model):
    """
    Computer the similarity between two sets of terms.
    """
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    matrix = np.zeros((len(my_terms), len(original_terms)))

    # compute the pairwise similarities
    for i, term1 in enumerate(my_terms):
        for j, term2 in enumerate(original_terms):
            if term1 in model and term2 in model:
                matrix[i, j] = cosine_similarity([model[term1]], [model[term2]])[0][0]
            else:
                # handle out-of-vocabulary terms ...!
                matrix[i, j] = 0

    max_sim_A_to_B = matrix.max(axis=1).mean()
    max_sim_B_to_A = matrix.max(axis=0).mean()

    average_similarity = (max_sim_A_to_B + max_sim_B_to_A) / 2
    return average_similarity
