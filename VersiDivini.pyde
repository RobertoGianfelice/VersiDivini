size(400,500)

LarghezzaImg=400
AltezzaImg=500

#Creo immagine vuote
img=createImage(LarghezzaImg,AltezzaImg,RGB)
#Carico pixel nell'array pixels
img.loadPixels()

#Apro file di input
input = createInput("DivinaCommedia");
content = ""

#Leggo il primo carattere (da saltare)
data1 = input.read()
c=0
while (data1 != -1):    
    #Leggo il primo carattere
    data1 = input.read() 
    
    if data1 != -1:
        #Se l'input non è finito, Leggo il secondo carattere
        data2 = input.read()
        
        if data2 != -1:
            #Se l'input non è finito, Leggo il terzo carattere
            data3=input.read() 
    #Creo il pixel
    img.pixels[c]=color(data1,data2,data3)
    c+=1
    
#Aggiorno l'immagine con i pixel nuovi
img.updatePixels()

#Visualizzo l'immagine
image(img,0,0)

#Salvo l'immagine
save("DivinaCommedia.jpg")
print(c)
