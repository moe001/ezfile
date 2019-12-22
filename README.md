# A one-line file-IO package
[deprecated]Use `pathlib.Path` in Python 3.5 or later.https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_bytes
---
python3 only,maybe.

    '''
    r.txt:
        abc123
    '''
    >>> from ezfile import read_in
    >>> read_in(r'.\r.txt')
    b'abc123'

-------------------------------

    >>> from ezfile import write_out
    >>> write_out(r'.\w.txt',b'ez')
    True
    '''
    w.txt:
        ez
    '''
