import pyautogui, time
import webbrowser
import locateScreen

mousePos = {
"1" : [(756, 348),(255, 255, 255)],
"2" : [(719, 854),(157, 162, 246)],
"3" : [(822, 252),(255, 255, 255)],
}
formData = [
        {'name':'Alic', 'fear':'fuck', 'source':1, 'robocop':1,
            'comments':'say hi'}];

pyautogui.PAUSE = 0.5
webbrowser.open('https://docs.google.com/forms/d/1A39NpQYMN8OOG-_lqDLFQb2h1SiHhCxPh0udtDEy2rU/viewform');
p = locateScreen.locate('firefox.png');
if not p is None:
    pyautogui.doubleClick(p[0], p[1]);
for j in range(3):
    for person in formData:
        submit = mousePos["2"];
        while not pyautogui.pixelMatchesColor(submit[0][0], submit[0][1], submit[1]):
            time.sleep(0.5);
        nameFile = mousePos["1"];
        pyautogui.click(nameFile[0][0], nameFile[0][1]);
        pyautogui.typewrite(person['name'] + '\t');
        pyautogui.typewrite(person['fear'] + '\t');
        pyautogui.typewrite(['down'] * person['source'] + ['\t']);
        pyautogui.typewrite(['right'] * person['robocop'] + ['\t']);
        pyautogui.typewrite(person['comments'] + '\t');
        pyautogui.press('enter');
        time.sleep(3);
        otherLink = mousePos["3"];
        pyautogui.click(otherLink[0][0], otherLink[0][1]);
