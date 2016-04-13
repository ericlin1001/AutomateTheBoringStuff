import os, re

def usage():
    print("""\
Usage: findInAlltxt.py [OPTION]... PATTERN [FILE]...
Try 'findInAlltxt.py --help' for more information.
""");
if len(os.sys.argv) == 1:
    usage()
else:
    reg = re.compile(os.sys.argv[1]);
    isFind = False;
    for cf, sub, f in os.walk('.'):
        for file in f:
            file = os.path.join(cf, file);
            if file.endswith(".txt"):
                f = open(file, 'r');
                fx = f.read();
                m = reg.search(fx);
                if m is not None:
                    isFind = True;
                    print(file + ":");
                    print("\t" + m.group());
                f.close();

    if not isFind:
        print("Not Found.");
