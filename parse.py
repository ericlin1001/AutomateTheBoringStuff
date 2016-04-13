import urllib3
import random
def modify(s, key, v):
    v = str(v);
    v = v.replace('"', '');
    key = key.replace('"', '');
    key = '"' + key + '"';
    l = s.find('"', s.find(':', s.find(key)  + len(key)))
    r = s.find('"', l + 1);
    #print("left:", s[0:l]); 
    #print("right:", s[r:]);
    s = s[0:l + 1] + v + s[r:];
  #  print("sssss:", s);
    return s;

def dosth(s):
    mid = 14585825718840192
    mid  = mid  + random.randint(0, 1000);
    s = modify(s, "Content", "This IS my New Content send by a Agent.");
    s = modify(s, "LocalID", mid);
    s = modify(s, "ClientMsgId", mid);

    return s;

#def parse(method,url, fields, headers):
def parse():
    f = open("requestData");
    fx = f.read();
    fx = fx.replace("  ", " ");
    fx = fx.replace("  ", " ");
    fx = dosth(fx);
    #print(fx);
    ffx = fx.split("\n\n");
    #print(ffx);
    sx = ffx[0].split(" ");
    url = sx[1];
    method = sx[0];
    #
    hx = ffx[1].split("\n");
    headers = {};
    for i in hx:
        si = i.split(": ");
        headers[si[0]] = si[1];

    fields = ffx[2];
    return (url, method, fields, headers);

def request():
    http = urllib3.PoolManager();

    #url =""
    #method = "";
    #fields = {}
    #headers = {};
    #parse(url, method, fields, headers);
    parse();
    url, method, fields, headers = parse();
    print("url:", url,"\nmethod:",  method,"\nfields:",  fields,"\nheaders:",  headers);
    res = http.urlopen(method, url, body = fields, headers = headers);
    print(res.status, res.data);

random.seed();
request();
