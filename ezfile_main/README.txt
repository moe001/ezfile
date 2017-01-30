python3 only,maybe.

r.txt:
    abc123

>>> from ezfile import read_in
>>> read_in(r'.\r.txt')
b'abc123'





-------------------------------





>>> from ezfile import write_out
>>> write_out(r'.\w.txt',b'ez')
True

w.txt:
    ez
