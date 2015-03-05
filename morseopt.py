#!/usr/bin/env python3

import sys
from ucb import main
from mr import emit
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

def translate(engstring):
    engstring = engstring.lower()
    translated = ''
    for char in engstring:
        if char in tab:
            translated += tab[char]
    return translated

@main
def run():
    for line in sys.stdin:
        emit('line', len(translate(line)))


