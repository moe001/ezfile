import os

import unittest
from ezfile import read_in, write_out

class Test_test1(unittest.TestCase):

    def test_read_in(self):
        t = read_in(r'.\testdata\r.txt')
        self.assertEqual(t,b"abc123")

        t = read_in(r'.\testdata\noex.txt')
        self.assertEqual(t,b"")

    def test_write_out(self):
        path = r'.\testdata\w.txt'

        try:
            os.remove(path)
        except:pass

        t = write_out(path,"123abc")
        self.assertEqual(t,True)
        with open(path) as f:
            self.assertEqual(f.read(),"123abc")

        t = write_out(path,b"abc123abc")
        self.assertEqual(t,True)
        with open(path,'rb') as f:
            self.assertEqual(f.read(),b"abc123abc")

        t = write_out(path,"加减乘除asmd")
        self.assertEqual(t,True)
        with open(path,encoding="utf-8") as f:
            self.assertEqual(f.read(),"加减乘除asmd")

        os.remove(path)

if __name__ == '__main__':
    unittest.main()
