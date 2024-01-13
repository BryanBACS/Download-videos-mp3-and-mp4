from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image #importar imagen o gif


#Función para descargar los videos al seleccionar el boton
def accion():

    #ver ruta actual
    ruta_actual = os.getcwd()

    #verificar que no exista
    if not os.path.exists(ruta_actual + "/descarga"):
        os.makedirs(ruta_actual + "/descarga")

    #obtener ruta de destino
    ruta_destino= ruta_actual + "/descarga"

    done  = Label(root, text="Descargando...." , fg="blue")
    done.grid(row=5, column=1, columnspan=2, sticky="we")
    #loading= Image.open("loading.gif")
    #framesgif = loading.n_frames
    #loading= loading.thumbnail((60,60), Image.Resampling.LANCZOS)
    #gifImage = [PhotoImage(file="loading.gif", format=f"gif -index {i}") for i in range(framesgif)]
    #newimage = gifImage[5]
    #gif = Label(root,image=newimage) #se agrega a la ventana
    #gif.grid(row=5, column=1) #se ajusta a la ubicación
    enlace = videos.get() #obtiene el enlace de viedos
    if enlace ==  "":
        done  = Label(root, text="SIN ENLACE." , fg="red")
        done.grid(row=5, column=1, columnspan=2, sticky="we")
    try:
        done  = Label(root, text="Descargando...." , fg="blue")
        done.grid(row=5, column=1, columnspan=2, sticky="we")
        video = YouTube(enlace)
        
    except:
        error = Label(root, text="Error de conexión" , fg="red")
        error.grid(row=5, column=1, columnspan=2, sticky="we")
        return

    
    #descarga = video.streams.get_by_resolution("720p") #descargar video en la máxima resolución
    descarga = video.streams.get_highest_resolution() #descargar video en la máxima resolución

    try: 
        descarga.download(ruta_destino) #descargar
    except:
        error = Label(root, text="Error al decargar video" , fg="red")
        error.grid(row=5, column=1, columnspan=2, sticky="we")
        return
    
    done  = Label(root, text="Descarga realizada" , fg="green")
    done.grid(row=5, column=1, columnspan=2, sticky="we")
    
    

def mp3():
    #ver ruta actual
    ruta_actual = os.getcwd()

    #verificar que no exista
    if not os.path.exists(ruta_actual + "/descarga"):
        os.makedirs(ruta_actual + "/descarga")

    #obtener ruta de destino
    ruta_destino= ruta_actual + "/descarga"
        
    done  = Label(root, text="Descargando...." , fg="blue")
    done.grid(row=5, column=1, columnspan=2, sticky="we")
    enlace = videos.get()
    try:
        musica = YouTube(enlace)
    except:
        error = Label(root, text="Error de conexión" , fg="red")
        error.grid(row=5, column=1, columnspan=2, sticky="we")
        return
    
    done  = Label(root, text="Descargando...." , fg="blue")
    done.grid(row=5, column=1, columnspan=2, sticky="we")
    descarga = musica.streams.filter(only_audio = True).first()
    
    try:
        downloadfile= descarga.download(ruta_destino)
    except:
        error = Label(root, text="Error al decargar musica", fg="red")
        error.grid(row=5, column=1, columnspan=2, sticky="we")
        return

    base, ext = os.path.splitext(downloadfile) #obtener el nombre del archivo en texto
    new_file = base + '.mp3'
    os.rename(downloadfile, new_file)
    
    

    done  = Label(root, text="Descarga realizada",  fg="green")
    done.grid(row=5, column=1, columnspan=2, sticky="we")


#esto es para crear la ventana del programa
root = Tk() #objeto tkinter
root.config(bd=15) #ventana con margen de 15
root.title("Script descargar videos. Creado por BACS")

#imagen = PhotoImage(file="youtube.png") #esto es para agregar una imagen en la venta
#foto = Label(root, image=imagen,bd=0) #se agrega a la ventana
#foto.grid(row=0, column=0) #se ajusta a la ubicación

menubar = Menu(root)
root.config(menu=menubar) #se agrega un menu


menubar.add_command(label="Salir", command=root.destroy) #aqui en cas de salir la ventan se destruye

#texto del titulo
titulo  = Label(root, text="Programa para descargar videos y musica de youtube.\n")
titulo.grid(row=0, column=1, columnspan=2, sticky="we") #ubicación

#texto del titulo
titulo  = Label(root, text="Creado por BACS.\n" ,fg="red")
titulo.grid(row=2, column=1, columnspan=2, sticky="we") #ubicación
#el columnspan 2 y el we sirven para que tomen las 2 columnas que hay, al estar en 2 columnas los botones
#By adding parameter columnspan you can "merge" multiple columns. Output will be centered button in merged columns. And by adding sticky parameter you can expand button to sides.
#columnspan=3 - merge 3 columns (starting with selected)
#sticky="we" - expand button to the left and right sides (west, east)

#entrada formulario
videos = Entry(root)
videos.grid(row=3, column=1, columnspan=2, sticky="we") #abajo, en la fila 1


#se crea el boton para descargar
boton = Button(root,text="Descargar .mp4", command=accion) #se ejecuta la función acción de descargar
boton.grid(row=4,column=1)

#se crea boton para mp3
boton2 = Button(root, text="Descargar .mp3", command= mp3)
boton2.grid(row=4, column=2)


root.mainloop() #que se ejecute en un loop