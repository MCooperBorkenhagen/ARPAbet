def getreps(PATH):
    """Binary phonological reps from CSV
    Parameters
    ----------
    PATH : str
        Path to the csv containing phonological representations.
    Returns
    -------
    dict
        A dictionary of phonemes and their binary representations
    """
    df = pd.read_csv(PATH)
    df = df[df['phone'].notna()]
    df = df.rename(columns={'phone': 'phoneme'})
    df = df.set_index('phoneme')
    feature_cols = [column for column in df if column.startswith('#')]
    df = df[feature_cols]
    df.columns = df.columns.str[1:]
    dict = {}
    for index, row in df.iterrows():
        dict[index] = row.tolist()
    return(dict)