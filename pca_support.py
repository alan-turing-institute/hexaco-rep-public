
def perform_pca(ipsatized_file, n_factors, cache_file_name=None):
    """
    Call out to R to perform PCA on the ipsatized file.

    :param ipsatized_file: File name of the ipsatized data.
    :param n_factors: How many factors to recover?
    :return: File name of the loadings file.
    """
    import subprocess
    from os.path import join, exists
    from _private import r_binary_folder, r_script_folder

    subprocess.call([r_binary_folder,
                     "--vanilla",
                     join(r_script_folder, "PCA.R"),
                     ipsatized_file,
                     str(n_factors),
                     "promax"])

    if exists('r_loadings.csv') and cache_file_name:
        from shutil import copy
        copy('r_loadings.csv', cache_file_name)
        return cache_file_name

    return 'r_loadings.csv'


def get_highest_loadings(top_n, loadings_df):
    """
    Get the {top_n} highest loadings for each factor.
    """
    import pandas as pd

    highest_loadings = {}
    for column in loadings_df.columns:
        top_absolute = loadings_df[column].abs().nlargest(top_n) 
        highest_loadings[column] = loadings_df.loc[top_absolute.index, column]    

    pp = pd.DataFrame()
    for factor in highest_loadings.keys():
        top_absolute = highest_loadings[factor]
        pp[factor] = [f"{x}({loadings_df[factor][x]:.2f})" for x in top_absolute.index]

    return highest_loadings, pp
