import shelve

sf = shelve.open('shelvedata');
sf.setdefault('a', 0);
sf.setdefault('b', 0);
a = sf['a'];
b = sf['b'];
print(a);
print(b);
a =a + 1;
b = b + 1;
sf['a'] = a
sf['b'] = b;
sf.close();
