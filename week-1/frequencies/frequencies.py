"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""




def frequencies(items):
    if not items:
        return {}

    frequencies = {}

    for idx, i in enumerate(items):
        if isinstance(i, int):
            items[idx] = str(i)

    # Your code goes here
    for i in items:
        frequencies[i] = frequencies.get(i, 0) + 1
    return frequencies



