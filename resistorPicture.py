from PIL import Image, ImageDraw, ImageFont


resistorValue = ["1K","brown","black","red","none", "gold"]
resistorSymbol = Image.open("resistorSymbol.png")
band0 = (0,0), (0, 100), (100,100), (100,0)
band1 = (0,100), (0, 200), (100,200), (100,100)
band2 = (0,200), (0, 300), (100,300), (100,200)
band3 = (0,300), (0, 400), (100,400), (100,300)
band4 = (0,400), (0, 5000), (100,500), (100,400)

black = (0,0,0)
brown = (142, 40, 0)
red = (243, 1, 0)
orange = (235, 138, 57)
yellow = (243, 244, 2)
green = (0, 166, 66)
blue = (0, 101, 181)
violet = (141, 90, 243)
grey = (115, 115, 115)
white = (243, 243, 243)
gold = (207, 181, 60)
silver = (192, 192, 192)
background = (234,234,234)
none = background

im = Image.new('RGB', (500, 500), (255,255,255))
draw = ImageDraw.Draw(im)
im.paste(resistorSymbol, (0,0))
# draw = ImageDraw.Draw(resistorSymbol)
for i in range(5):
    pass
draw.polygon(band0, fill=(172,30,124)) # outline='red', fill='blue'
draw.polygon(band1)
draw.polygon(band2)
draw.polygon(band3)
draw.polygon(band4)
im.save('resistor.jpg')
