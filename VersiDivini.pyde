
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
            for i in range(50):
                #per dimTessera righe immagine
                for j in range(dimTessera):
                    #per dimTessera colonne immagine
                    img.pixels[pixel+j+(LarghezzaImg*i)]=color(data1,data2,data3)
            pixel=pixel+dimTessera
            if (pixel%LarghezzaImg==0):
                #se ho finito una riga di patchwork, il prossimo quadrato va posizionato sotto le dimTessera righe pixel
                pixel=pixel+LarghezzaImg*(dimTessera-1)
        else:
            #passo al lixel successivo
            img.pixels[pixel]=color(data1,data2,data3)
            pixel+=1
            
    if (patchwork) :
        # Completo l'ultima linea con quadrati neri
        while ((pixel/dimTessera)%LarghezzaImg):
            for i in range(50):
                #per dimTessera righe immagine
                for j in range(dimTessera):
                    #per dimTessera colonne immagine
                    img.pixels[pixel+j+(LarghezzaImg*i)]=color(0,0,0)
            pixel=pixel+dimTessera
            if (pixel%LarghezzaImg==0):
                #se ho finito una riga di patchwork, il prossimo quadrato va posizionato sotto le dimTessera righe pixel
                pixel=pixel+LarghezzaImg*(dimTessera-1)

                
    #Aggiorno l'immagine con i pixel nuovi
    img.updatePixels()
    
    #Visualizzo l'immagine
    image(img,0,0)
    
    #Salvo l'immagine
    save("Out.tiff")
    print(pixel)
    
