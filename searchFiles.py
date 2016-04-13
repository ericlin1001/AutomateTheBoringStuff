import os, re
ts = os.sys.argv[1:];
print("Search files containing %s in %s"%(','.join(ts), os.getcwd()));
for cf, sub, files in os.walk(os.getcwd()):
    for file in files:
        for t in ts:
            if not file.find(t) ==  - 1:
                f = os.path.join(cf, file);
                print(f);

