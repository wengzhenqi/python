import re
from collections import Counter

class countppatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        counter = Counter()
        cpatt = re.compile(patt)
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:   #如果匹配到内容，更新字典，None表示False
                     key = m.group()
                     counter.update([key])
        return counter



if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    cp = countppatt(fname)
    result = cp.count_patt(ip)
    print(result)
    print(result.most_common(3))