import re

def afunction():
    print("This is the installed function")
    
def my_name():
    print("Hi my name is Carol Moore and my UVA ID is cm6ag.")

def clean_string(str_word):
    """
    INPUTS:
    str_word     string string contining several words to clean
    RETURNS:
    string       the string after removal of extra spaces, punctuation and lowercasing
    """
    str_word = re.sub(r'\W+', ' ', str_word)
    assert isinstance(str_word, str), "String expected but recieved type {} instead".format(type(str_word))

    return str_word.strip()

import re
def space_compress(stocomp):
    assert isinstance(stocomp, str), "Expected str but got {} instead".format(type(stocomp))
    comp = re.sub(r'\s+', ' ', stocomp)
    return comp.strip()

def new_func():
    pass
