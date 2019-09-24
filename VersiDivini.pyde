
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
        if (patchwork) :
            for i in range(100):
                #per 100 righe immagine
                for j in range(100):
                    #per 100 colonne immagine
                    img.pixels[pixel+j+(LarghezzaImg*i)]=color(data1,data2,data3)
            pixel=pixel+100
            if (pixel%LarghezzaImg==0):
                #se ho finito una riga di patchwork, il prossimo quadrato va posizionato sotto le 100 righe pixel
                pixel=pixel+LarghezzaImg*99
        else:
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
    
