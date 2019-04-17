import sys
import hashlib

def a(fname):
    with open(fname, 'rb') as ll:
        kk = ll.read()
        aa = hashlib.md5(kk)
    p = aa.hexdigest()
    print(p)

if __name__ == '__main__':
    a(sys.argv[1])