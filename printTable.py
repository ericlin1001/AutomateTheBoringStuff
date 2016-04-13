def formatT(t, w, type):
    if type == "left":
        return t + (' ' * (w - len(t)))

    elif type == "center":
        return t.center(w);
    else:
       # return  (' ' * (w - len(t))) + t;
       return t.rjust(w);

def flip(mylist):
    ns = list(range(len(mylist[0])))
    for j in range(len(mylist[0])):
        ns[j] = list(range(len(mylist)))
        for i in range(len(mylist)):
            ns[j][i] = mylist[i][j]
    mylist = ns
    return ns

def printTab(mylist):
    mylist = flip(mylist)
    cmax = [0 for x in range(len(mylist[0]))];
    for r in range(len(mylist)):
        for c in range(len(mylist[0])):
                cmax[c] = max(cmax[c], len(mylist[r][c]));
    ns = 1;
    for r in range(len(mylist)):
        for c in range(len(mylist[0])):
            print(formatT(mylist[r][c], cmax[c], "right"), end = (' ' * ns));
        print()


def test():
    tableData  =  [['apples',  'oranges',  'cherries',  'banana'], 
            ['Alice',  'Bob',  'Carol',  'David'], 
            ['dogs',  'cats',  'moose',  'goose']]
    printTab(tableData);

if __name__  ==  '__main__':
    test()
