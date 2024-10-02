# This file contains a function that helps me to looking for a synonyms of a words, and
# make more easy to search and answer in the knoloedge base...

from synonyms_base import synonyms_base as sb
from utils.singular import plural_to_singular_string as pss

#
def find_key_or_synonyms(str):
    input_str = str.lower()

    # Change from plural to singular words...clear
    singiular_string_words = pss(input_str)

    # we go throught the synomys dictionari...
    for key, synonyms in sb.items():
        # check if any word o key word is in the str...
        if key in singiular_string_words:
            return key
        for synonym in synonyms:
            if synonym in singiular_string_words:
                return key

    # if there is nothing, return none
    return None
