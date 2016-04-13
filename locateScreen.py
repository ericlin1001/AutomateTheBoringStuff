import pyautogui
from PIL import Image;
import numpy as np;

def locate(file, sim = 0.999):
    tmp = '/tmp/tmp.png'
    src = pyautogui.screenshot(tmp);
    #src = Image.open(tmp);
    key = Image.open(file);

    #f = findImg(src, key, sim);
    f = searchMatrix(convertToMatrix(src), convertToMatrix(key), sim);
    print(f);
    src.close();
    key.close();
    return f;

def convertColor(c):
    r, g, b = c;
    return (r + g + b) / 3 / 255;

def convertToMatrix(img):
    w, h = img.size;
    m = np.zeros(w * h).reshape(w, h);
    for x in range(w):
        for y in range(h):
            m[x][y] = convertColor(img.getpixel((x, y)));
    return m

def searchMatrix(src, key, sim):
    w, h = key.shape;
    dw, dh = src.shape
    dw = dw - w;
    dh = dh - h
    diff = 1.0 - sim;
#    print("diff:%f"%diff);
    for x in range(dw):
        for y in range(dh):
#            if x%200 == 0:
 #               print("search in (%d, %d)"%(x, y));
            crop = src[x:x + w, y:y + h];
            d = crop - key;
            d = d * d;
            d
            dd = d.sum() / (w * h)
#            print("search in (%d, %d) dd:%f diff:%f"%(x, y, dd, diff));
            if dd<= diff:
                return x, y;
    return None;



def getColorDiff(a, b):
    diff = 0;
    for i in range(3):
        d = a[i] - b[i];
        diff = diff + d * d;
    diff = diff / 195075;
    #diff = diff / 3;
    #diff  = diff / 255 / 255;
    return diff;
        
def calDiff(src, key, dx, dy):
    w, h = key.size;
    diff = 0;
    count = 0;
    for x in range(0, w , int(w / 10)):
        for y in range(0, h , int(h / 10)):
            count = count + 1;
            diff  = diff + getColorDiff(src.getpixel((dx + x, dy + y)),
                    key.getpixel((x, y)));
    diff = diff/count;
    return diff;


def findImg(src, key, sim = 1):
    w, h = key.size;
    dw, dh = src.size
    dw = dw - w;
    dh = dh - h
    diff = 1 - sim;
    if dw<0 or dh<0 :
        return None

    for dx in range(dw + 1):
        for dy in range(dh + 1):
            if dx%10 == 0:
                print("search in (%d, %d)"%(dx, dy));
            if calDiff(src, key, dx, dy)<=diff:
                return dx, dy;
            #cal 
    return None;


#print(locate('firefox.png'));
