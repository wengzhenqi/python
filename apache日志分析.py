import re

def count_patt(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:   #如果匹配到内容，更新字典，None表示False
                 key = m.group()
                 patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict



if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
    
    
    
    # awk '{ip[$1]++} END{for(i in ip) {print i,ip[i]}}' /var/log/httpd/access_log | sort -nr | head -5
