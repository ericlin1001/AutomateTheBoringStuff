import os
for cf, sb, files in os.walk('/home/ailab'):
    for file in files:
        file = os.path.join(cf, file)
        if not os.path.islink(file):
            if os.path.getsize(file)>100 * 1024 * 1024:
                print(os.path.abspath(file));
