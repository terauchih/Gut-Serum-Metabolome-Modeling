"""
Script to take taxonomy/relative abundance data and select for a specified level.
"""
# Hinako Terauchi
# Mar 2021


def extract_bacterial_taxa(my_taxa, level='all'):
    """
    Extracts bacterial taxa at the specified level

    input:
    cleaned up 16S rRNA sequencing result produced with
    Illumina amplicon sequencing and QIIME2

    keyword arguments:
    level -- desired taxonomy level to extract from 16S input (default 'all')
    """

    # read in the taxa section of my_taxa:
    taxa_fullname = my_taxa.index

    # separate at specified taxonomy level
    sep_at = level.lower()
    # splitty things

    # split using the script based on what I made for lab
    # import that script probably
    # then do the thing
    new_data = dothing(my_taxa, sep_at)

    # Possibly attatch the relative abundance value (maybe log2?)

    return "probably a new pandas dataframe with the selected taxa"
