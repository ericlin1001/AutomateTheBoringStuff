import urllib3
import re

def doQ(i, an):
    l, r = getQ(i)
    print("Test Example" + str(i) + ":");
    print(l);
    print(r);
    #reg = re.compile('[A-Z]\w* Nakamoto');
    reg = an[i];
    print("Should pass Cases:");
    for i in l:
        m = reg.search(i);
        if m is None:
            print("fails");
        else:
            print(m.group());

    print("Should fail Cases:");
    for i in r:
        m = reg.search(i);
        if m is None:
            print("fails");
        else:
            print(m.group());
    print();

def getQ(i):
    url='https://automatetheboringstuff.com/chapter7/'
    http = urllib3.PoolManager()
    data = http.request('GET', url).data;
    res = ""
#    r = re.compile(r'Q.*?' + str(i) + "(. * ?)"  + r'(Q.*?' + str(i +1) + ')|(Practice)');
    r = re.compile(r'Q.+?(' + str(i) + "\. (.+?))"  + r'((Q.*?' + str(i +1) +
            ')|(Practice))');
   # r = re.compile(r'src', re.UNICODE)
   # print(str(data));
    res = r.search(str(data)).group(1);
    res = res.replace('\\', '');
    r1 = re.compile(r'match the following:(.*?)not the following:(.*)'
            );
    m = r1.search(res);
    r2 = re.compile(r"'.*?'");
    l = m.group(1);
    r = m.group(2);
    la = r2.findall(l);
    ra = r2.findall(r);
    la = '|'.join(la).replace('\'', '').split('|');
    ra = '|'.join(ra).replace('\'', '').split('|');
    return (la, ra);

#print(data);
an = [0] * 50;
an[20] = re.compile(r'^(\d{1,3}(,\d{3})*)$');
an[21] = re.compile(r'([A-Z]\w* Nakamoto)');
an[22] = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.', re.IGNORECASE);
for i in range(20, 23):
    doQ(i, an);

#print(q);

