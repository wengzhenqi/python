import re


class countppatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        patt_dict = {}
        cpatt = re.compile(patt)
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:   #如果匹配到内容，更新字典，None表示False
                     key = m.group()
                     patt_dict[key] = patt_dict.get(key, 0) + 1
        return patt_dict



if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    cp = countppatt(fname)
    xx = '(Chrome|Firefox|MSIE)'
    print(cp.count_patt(ip))
    print(cp.count_patt(xx))