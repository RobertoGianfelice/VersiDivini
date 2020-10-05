size(400,500)

LarghezzaImg=400
AltezzaImg=500
img=createImage(LarghezzaImg,AltezzaImg,RGB)
img.loadPixels()

input = createInput("DivinaCommedia");
content = ""
data1 = input.read()
c=0
while (data1 != -1):

    data1 = input.read();
    if data1 != -1:
        data2 = input.read();
        if data2 != -1    :
            data3=input.read();
    img.pixels[c]=color(data1,data2,data3)
    c+=1

img.updatePixels()
image(img,0,0)
save("DivinaCommedia.tiff")
print(c)
