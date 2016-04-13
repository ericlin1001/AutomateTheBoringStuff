from PIL import Image, ImageDraw, ImageFont
import ShowImg;

def show(i):
    i.save('tmp.png');
    ShowImg.showImg('tmp.png');

img = Image.new('RGBA', (300, 300), 'blue');
draw = ImageDraw.Draw(img);
#font = ImageFont.truetype(os.path.jogin(
draw.text((20, 20), 'hello world')
show(img);



