"""
Desafio PUG-PE
ID: 1
Semana: 11/02/2011
PUG: Henrique Menezes
"""


def pack(iterable):
    """
    >>> x = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
    >>> ret = pack(x)
    >>> ret
    [['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a'], ['d'], ['e', \
'e', 'e', 'e']]
    >>> x = ['a', 'b', 'c']
    >>> ret = pack(x)
    >>> ret
    [['a'], ['b'], ['c']]
    >>> x = []
    >>> ret = pack(x)
    >>> ret
    []
    """
    import itertools
    return [list(g) for k, g in itertools.groupby(iterable)]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
