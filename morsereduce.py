#!/usr/bin/env python3

import sys
from ucb import main
from mr import values_by_key, emit
from itertools import permutations

tab = {'a': '._ ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ',
        'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ',
        'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ',
        'n': '-, ', 'o': '--- ', 'p': '.--. ', 'q': '--.- ',
        'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ',
        'v': '...- ', 'w': '.-- ', 'x': '-..- ', 'y': '-.-- ',
        'z': '--.. ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-....', '7': '--...',
        '8': '---.. ', '9': '----. ', '0': '----- ', ' ': '/ ', '.': '.-.-.- ', ',': '--..-- ', ':': '---... ', '?': '..--.. ', '\'': '.----. ', '-': '-....- ', '/': '-..-. ', '(': '-.--.- ', ')': '-.--.- ', '\"': '.-..-. ', '!': '-.-.-- ', ';': '-.-.-. ' 
        }

tab_len = {}
for item in tab:
    tab_len[item] = len(tab[item])


def translate(engstring):
    engstring = engstring.lower()
    translated = ''
    for char in engstring:
        if char in tab:
            translated += tab[char]
    return translated

def randomize(dct):
    """returns an iterator and
    it is an example of a generator function"""
    perms = permutations(dct, len(dct)) #perm is an iterator that contains a different mix of the keys of dct
    old_values = list(dct.values())
    for perm in perms:
        new_dct = {}    
        for char in perm:
            index = perm.index(char)
            new_value = old_values[index]
            new_dct[char] = new_value
        yield new_dct

@main
def run():
    num_morse_chars = 0
    trash = 0
    for key, value_iterator in values_by_key(sys.stdin):
        if key in tab_len:
            num_instances_of_key = sum(value_iterator)
            num_morse_chars += num_instances_of_key * tab_len[key]
        else:
            trash = sum(value_iterator)
    emit('standard morse code', num_morse_chars)







