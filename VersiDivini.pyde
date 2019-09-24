
LarghezzaImg=400
AltezzaImg=500

#Creo immagine vuote
img=createImage(LarghezzaImg,AltezzaImg,RGB)
#Carico pixel nell'array pixels
img.loadPixels()


def setup():
    size(LarghezzaImg,AltezzaImg)
    creaImg()
 
def creaImg():
    
    patchwork=True
    #Apro file di input
    input = createInput("Input");
    content = ""
    
    #Leggo il primo carattere (da saltare)
    data1 = input.read()
    c=0
    while (data1 != -1 and c<LarghezzaImg*AltezzaImg):    
        #Leggo il primo carattere
        data1 = input.read()     
        if data1 != -1:
            #Se l'input non è finito, Leggo il secondo carattere
            data2 = input.read()
            if data2 != -1:
                #Se l'input non è finito, Leggo il terzo carattere
                data3=input.read() 

        #Creo il pixel        
        if (patchwork) :
            for i in range(100):
                for j in range(100):
                      img.pixels[c+j+LarghezzaImg*i]=color(data1,data2,data3)
            c=c+100
            if (c%LarghezzaImg==0):
                c=c+LarghezzaImg*99
        else:
            img.pixels[c]=color(data1,data2,data3)
            c+=1
            
    #Aggiorno l'immagine con i pixel nuovi
    img.updatePixels()
    
    #Visualizzo l'immagine
    image(img,0,0)
    
    #Salvo l'immagine
    save("DivinaCommedia.tiff")
    print(c)
    
