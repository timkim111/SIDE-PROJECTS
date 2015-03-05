#!/usr/bin/env python3

import sys
from ucb import main
from mr import emit

@main
def run():
    for line in sys.stdin:
        chars = {}
        for char in line:
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        for char in chars:
            emit(char, chars[char])


