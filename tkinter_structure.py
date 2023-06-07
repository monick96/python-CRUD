from tkinter import *
from tkinter import messagebox
import sqlite3 as sq3 


'''
*********************************
    PARTE FUNCIONAL
*********************************
'''
# *********** FUNCIONES VARIAS **************


# *********** MENU **************

#   BBDD

#       Conectar
def conectar():
    global con
    global cur
    con = sq3.connect('my-db.db')
    cur = con.cursor()
    messagebox.showinfo("STATUS","Conectado con exito")
#       Listar
'''----------------------------------------------------------------'''
#       Salir
def salir():
    resp = messagebox.askquestion("Confirme","Esta seguro que desea salir?")
    if resp == "yes":
        con.close()
        raiz.destroy()

#   GRÁFICAS

#   LIMPIAR
def limpiar():
    legajo.set("")
    apellido.set("")  
    nombre.set("")  
    email.set("")  
    calificacion.set("")  
    escuela.set("Seleccione")  
    localidad.set("")  
    provincia.set("")  
    legajo_input.config(state='normal')

#   ACERCA DE
    #Licencia
def mostrar_licencia():
    msg = '''
    Sistema CRUD en Python
    Copyright (C) 2023 - xxxxx xxxx
    Email: xxxx@xxx.xx\n=======================================
    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public 
    License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any 
    later version.
    This program is distributed in the hope that it will be 
    useful, but WITHOUT ANY WARRANTY; without even the 
    implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE.  See the GNU General Public License 
    for more details.
    You should have received a copy of the GNU General Public 
    License along with this program.  
    If not, see <https://www.gnu.org/licenses/>.'''
    messagebox.showinfo("LICENCIA",msg)
    #Acerca de
def mostrar_acercade():
    messagebox.showinfo("Acerca de","Created by Monica Melgarejo for BIG DATA course \n June 2023")

# *********** MENU CRUD (CREATE-READ-UPDATE-DELETE**************

#       CREAR
#       LEER
#       ACTUALIZAR
#       BORRAR


'''
*********************************
    INTERFAZ GRÁFICA
*********************************
'''
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
bbddmenu.add_command(label="Conect BBDD",command=conectar)
#student list button
bbddmenu.add_command(label="List of students")
#exit button
bbddmenu.add_command(label="Exit",command=salir)


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
clearmenu.add_command(label="Clear fields",command=limpiar)

######SUB MENU Acerca de...######
infomenu = Menu(barramenu,tearoff=0)
    #comandos SUB MENU Acerca de...
#license
infomenu.add_command(label="License",command=mostrar_licencia)

#about..
infomenu.add_command(label="About...",command=mostrar_acercade)

#cascades from principal menu
barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Graficas",menu=statmenu)
barramenu.add_cascade(label="Limpiar",menu=clearmenu)
barramenu.add_cascade(label="Acerca de...",menu=infomenu)

######FRAME FIELDS######
framefields = Frame(raiz)
framefields.config(bg=color_fondo)
framefields.pack(fill="both")
    
#LABEL
'''
"STICKY"
    n
  nw   ne
w         e
  sw   se
    s
'''
#config front labels function
def config_label(label,row):
    space_labels = {'column':0,'sticky':'e','padx':10, 'pady':10}
    colour_labels={'bg':color_fondo,'fg':color_letra}
    label.grid(row=row,**space_labels)
    label.config(**colour_labels)
    
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

#ENTRY

'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana

'''
# Crea variables de control de los campos de entrada
legajo = StringVar()
apellido = StringVar()
nombre = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

#entry function
def config_input(mi_input, fila):
    espaciado_inputs = {'column':1, 'padx':10, 'pady':10, 'ipadx':50}
    mi_input.grid(row = fila, **espaciado_inputs)

legajo_input = Entry(framefields, textvariable=legajo)
apellido_input = Entry(framefields, textvariable=apellido)
nombre_input = Entry(framefields, textvariable=nombre)
email_input=Entry(framefields, textvariable=email)
calificacion_input=Entry(framefields, textvariable=calificacion)
'''
escuelas = buscar_escuelas(False)
escuela.set('Seleccione')
escuela_option = OptionMenu(framefields, escuela,*escuelas)
escuela_option.grid(row=5, column=1, padx=10, pady=10, sticky='w', ipadx=50)
'''

localidad_input=Entry(framefields, textvariable=localidad)
localidad_input.config(state='readonly')
provincia_input = Entry(framefields, textvariable=provincia)
provincia_input.config(state='readonly')

entries = [legajo_input,apellido_input,nombre_input,email_input,calificacion_input,"escuela_option",localidad_input,provincia_input]

for e in range(len(entries)):
    if entries[e]=="escuela_option":
        continue
    else:
        config_input(entries[e],e)

#--------FRAMEBOTONES-------- FUNCIONES CRUD 

framebotones = Frame(raiz)
framebotones.config(bg=fondo_framebotones)
framebotones.pack(fill='both')

def config_buttons(mi_button, columna):
    espaciado_buttons = {'row':0, 'padx':5, 'pady':10, 'ipadx':12}
    mi_button.config(bg=color_fondo_boton, fg=color_texto_boton)
    mi_button.grid(column = columna, **espaciado_buttons)

boton_crear = Button(framebotones, text='Crear')
config_buttons(boton_crear, 0)

boton_buscar = Button(framebotones, text='Buscar')
config_buttons(boton_buscar, 1)

boton_actualizar =Button(framebotones, text='Actualizar')
config_buttons(boton_actualizar, 2)

boton_borrar = Button(framebotones, text='Eliminar')
config_buttons(boton_borrar, 3)

#--------FRAMECOPY--------

framecopy = Frame(raiz)
framecopy.config(bg='black')
framecopy.pack(fill='both')

copylabel = Label(framecopy, text="(2023) by Monica Melgarejo")
copylabel.config(bg='black',fg='white')
copylabel.grid(row=0, column=0, padx=10, pady=10)













raiz.mainloop()
