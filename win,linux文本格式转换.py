import sys

def unix2doc(fname):
    dst_fname = fname + '.txt'
    with open(fname) as src_fobj:
        with open(dst_fname, 'w') as dst_fname:
            for line in src_fobj:
                line = line.rstrip() + '\r\n'

                dst_fname.write()

        
if __name__ == '__main__':
    unix2doc(sys.argv[1])