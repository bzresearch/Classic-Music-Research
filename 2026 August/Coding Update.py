from music21 import corpus

def find_composer_works(composer_name):
    """
    Search the music21 built-in corpus for works by a composer.
    Returns raw search hits; every hit must be manually opened and
    verified for genre and content before use, since full-text
    search over-matches on unrelated metadata fields.
    """
    return corpus.search(composer_name)  # no field= restriction
