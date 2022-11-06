
LarghezzaImg=500
AltezzaImg=500
dimTessera=50

#Creo immagine vuote
img=createImage(LarghezzaImg,AltezzaImg,RGB)
#Carico pixel nell'array pixels
img.loadPixels()


def setup():
    size(LarghezzaImg,AltezzaImg)
    creaImg()
 
def creaImg():
    
    #Apro file di input
    input = createInput("Input");
    content = ""
    
    #Leggo il primo carattere (da saltare)
    data1 = input.read()
    pixel=0
    while (data1 != -1 and pixel<LarghezzaImg*AltezzaImg):    
        #Leggo il primo carattere
        data1 = input.read()     
        if data1 != -1:
            #Se l'input non è finito, Leggo il secondo carattere
            data2 = input.read()
            if data2 != -1:
                #Se l'input non è finito, Leggo il terzo carattere
                data3=input.read() 

        #Creo il pixel        
        #passo al lixel successivo
        img.pixels[pixel]=color(data1,data2,data3)
        pixel+=1
            
                
    #Aggiorno l'immagine con i pixel nuovi
    img.updatePixels()
    
    #Visualizzo l'immagine
    image(img,0,0)
    
    #Salvo l'immagine
    save("Out.tiff")
    print(pixel)
    
