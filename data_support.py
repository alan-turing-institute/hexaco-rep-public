

def fix_name(x):
    """
    Used to translate the 'Full Name' from the population file, into
    an index value for results files.

    :param x: 'Full Name' from population file, i.e. 'Dave Smith'
    :return: 'DaveSmith'
    """
    return x.replace(' ', '').split('.')[0]
