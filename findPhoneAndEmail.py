import pyperclip,  re

phoneReg = re.compile(r'''(
        (\d{3})
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)?
        (\d{4})
        )
        ''', re.VERBOSE);

mailReg = re.compile(r'''
        (\w+?@\w+?(\.\w+) + )
        ''', re.VERBOSE);

s = pyperclip.paste();
#print(s)
p = phoneReg.findall(s);
r = [];

for i in p:
    r.append("-".join([i[1], i[3], i[5]]))

e = mailReg.findall(s);
for i in e:
    r.append(i[0]);

res = "\n".join(r);
#print(p);
#print(e);
print(res)
pyperclip.copy(res);

