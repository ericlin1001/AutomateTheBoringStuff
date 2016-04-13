def swap(a,l, r):
    t = a[l];
    a[l] = a[r];
    a[r] = t;

def heapsort(a, key = None):
    if key is None:
        key = lambda x:x
    quicksort(a, 0, len(a), key);
    return a;
    

def heapsort(a, size, key):
    if(l + 1 >= r):
        return;
    mid = partition(a, l, r, key)
    quicksort(a, l, mid, key);
    quicksort(a, mid + 1, r, key);

def quicksortk(a, ldef test():
    b = [[4,  1],  [2,  1],  [1,  3],  [1,  100]];
    a = b[:];
    print(a);
    print(b);
    qsort(a);
    print("after qsort(a).");
    print(a);
    print(b);
    for i in range(len(b)):
        print("getk(b, " , str(i) , ") = ",getk(b, i));


