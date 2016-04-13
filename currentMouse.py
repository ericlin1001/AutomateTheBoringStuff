import pyautogui, threading, subprocess
import GetCh
class ShowCurrentMouse(threading.Thread):
    x = 0;
    y = 0;
    color = ();
    isStop = False;
    def __init__(self):
        super(ShowCurrentMouse,  self).__init__();
        self.isStop = False;

    def getXY(self):
        return self.x, self.y;

    def getColor(self):
        return self.color;

    def stop(self):
        self.isStop = True;

    def run(self):
        mlen = 0;
        while not self.isStop:
            self.x, self.y = pyautogui.position();
            self.color = pyautogui.pixel(self.x, self.y);
            r, g, b = self.color;
            mess = 'Current Mouse: (%d, %d) color:(%d, %d, %d)'%(self.x,
                    self.y,r, g, b);
            print('\b'*mlen, end='');
            print(mess, end='', flush = True);
            mlen = len(mess);


getch = GetCh.getch;
mythread = ShowCurrentMouse();
print("Ctrl - C or e to end.");
try:
    mythread.start();
    f = open('saveMousePosition.txt', 'w');
    f.write("mousePos = {\n");
    while True:
        a = getch();
        if ord(a) == 3 or a  == 'e':#ord(Ctrl - C) = 3.
            raise KeyboardInterrupt;
            break;
        x, y = mythread.getXY();
        r, g, b= mythread.getColor();

        mess ='"' + str(a) + "\" : [(%d, %d),(%d, %d, %d)],"%(x, y, r, g, b);
        print("\n" + str(ord(a)) + mess);
        f.write(mess + "\n");


except KeyboardInterrupt:
    mythread.stop();
    mythread.join();
    f.write("\b\b}");
    f.close();
    subprocess.Popen(['cat', 'saveMousePosition.txt']);
    print('\nexiting...');

