import re

def strip(s, r = ' '):
    rg = re.compile(r'^' + r  + r"*(.+?)" + r + r'*$', re.DOTALL);
    res = rg.search(s).group(1);
    print(res);
    print(rg.search(s).groups());
    print(s.strip(r) == res);
    return res;

strip('123123 12 31 412 3321');
