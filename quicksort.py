def swap(a,l, r):
    if l == r:
        return;
    t = a[l];
    a[l] = a[r];
    a[r] = t;

def partition(a, l, r, key):
    pivot = a[l];
    kp = key(pivot)
    r = r - 1;
    swap(a,  l, r);
    left = l;#pointing next biggerOrEqual than pivot.
    while l < r:
        if(key(a[l])<kp):
            swap(a, l, left);
            left = left + 1;
        l = l + 1;
    swap(a,r, left);
    return left;

def qsort(a, key = None):
    if key is None:
        key = lambda x:x
    quicksort(a, 0, len(a), key);
    return a;
    

def quicksort(a, l, r, key):
    if(l + 1 >= r):
        return;
    mid = partition(a, l, r, key)
    quicksort(a, l, mid, key);
    quicksort(a, mid + 1, r, key);

def quicksortk(a, l, r, k, key):
    """This is the unstable version of quicksort."""
    if(l + 1 >= r):
        return a[k];
    mid = partition(a, l, r, key)
    if(mid == k):
        return a[k];
    if(k<mid):
        return quicksortk(a, l, mid ,k, key);
    else:
        return quicksortk(a, mid + 1, r, k, key);

def getk(a, k, key = None):
    if key is None:
        key = lambda x:x
    if(k<0 or k >= len(a)):
        return None;
    return quicksortk(a, 0, len(a), k,  key);

def test():
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


