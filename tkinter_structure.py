from tkinter import *

#framebotones colours
fondo_framebotones = 'gray20'
color_fondo_boton = 'gray10'
color_texto_boton = 'white'

#framecampos colours
color_fondo =  'snow2' # frame & labels
color_letra = fondo_framebotones # labels

#creacion de ventana
raiz = Tk()
raiz.title('GUI-C23222')

##BARRA MENU##
barramenu = Menu(raiz) #objeto de clase Menu() ubicado en raiz 
raiz.config(menu=barramenu)

######SUB MENU BBDD######
bbddmenu = Menu(barramenu,tearoff=0) #objeto de clase barramenu
    #comandos SUB MENU BBDD
#conect button
bbddmenu.add_command(label="Conect BBDD")
#student list button
bbddmenu.add_command(label="List of students")
#exit button
bbddmenu.add_command(label="Exit")


######SUB MENU Graficas######
statmenu= Menu(barramenu,tearoff=0) #objeto de clase barramenu
    #comandos SUB MENU Graficas
#students per school
statmenu.add_command(label="Students per school")
#student score
statmenu.add_command(label="Score")

######SUB MENU Limpiar######
clearmenu=Menu(barramenu,tearoff=0)
    #comandos SUB MENU Limpiar
clearmenu.add_command(label="Clear fields")

######SUB MENU Acerca de...######
infomenu = Menu(barramenu,tearoff=0)
    #comandos SUB MENU Acerca de...
#license
infomenu.add_command(label="License")

#about..
infomenu.add_command(label="About...")

#cascades from principal menu
barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Graficas",menu=statmenu)
barramenu.add_cascade(label="Limpiar",menu=clearmenu)
barramenu.add_cascade(label="Acerca de...",menu=infomenu)

######FRAME FIELDS######
framefields = Frame(raiz)
framefields.config(bg=color_fondo)
framefields.pack(fill="both")
def config_label(label,row):
    space_labels = {'column':0,'sticky':'e','padx':10, 'pady':10}
    colour_labels={'bg':color_fondo,'fg':color_letra}
    label.grid(row=row,**space_labels)
    label.config(**colour_labels)
'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''
legajo_label = Label(framefields,text= "Nº de legajo")
config_label(legajo_label,0)

apellido_label = Label(framefields,text= "Apellido")
config_label(apellido_label,1)

nombre_label = Label(framefields,text= "Nombre")
config_label(nombre_label,2)

email_label = Label(framefields,text= "Email")
config_label(email_label,3)

promedio_label = Label(framefields,text= "Promedio")
config_label(promedio_label,4)

escuela_label = Label(framefields,text= "Escuela")
config_label(escuela_label,5)

localidad_label = Label(framefields,text= "Localidad")
config_label(localidad_label,6)

provincia_label = Label(framefields,text= "Provincia")
config_label(provincia_label,7)













raiz.mainloop()
