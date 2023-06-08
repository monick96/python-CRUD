from tkinter import *
from tkinter import messagebox
import sqlite3 as sq3 
import matplotlib.pyplot as plt

'''
*********************************
    PARTE FUNCIONAL
*********************************
'''
# *********** FUNCIONES VARIAS **************
def buscar_escuelas(actualiza):
    con = sq3.connect('my-db.db')
    cur = con.cursor()
    if actualiza: 
        cur.execute('SELECT _id, localidad, provincia FROM escuelas WHERE nombre =?',(escuela.get(),)) #or ...WHERE nombre =' + escuela.get())
    else:#Acá configuro opción para llenar la lista de escuelas cuando abro CRUD
        cur.execute("SELECT nombre FROM escuelas")
    
    resultado = cur.fetchall() #RECIBO LISTA DE TUPLAS CON UN ELEMENTO "FANTASMA"
    #print(resultado)
    retorno = []
    for e in resultado:
        if actualiza:
            provincia.set(e[2])
            localidad.set(e[1])
        esc = e[0] #id
        retorno.append(esc)
        
    con.close()
    return retorno


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
def listar():
    class Table():
        def __init__(self,ubicacion):
            nombre_cols = ['Legajo', 'Apellido','Nombre','Promedio', 'Email', 
            'Escuela', 'Localidad', 'Provincia']
            for i in range(cant_cols):
                self.e = Entry(ubicacion)
                self.e.config(bg='black', fg='white')
                self.e.grid(row=0, column=i)
                self.e.insert(END,nombre_cols[i])

            for fila in range(cant_filas):
                for col in range(cant_cols):
                    self.e = Entry(ubicacion)
                    self.e.grid(row=fila+1, column=col)
                    self.e.insert(END, resultado[fila][col])
                    self.e.config(state='readonly')

    raiz2 = Tk()
    raiz2.title('Listado alumnos')
    frameppal = Frame(raiz2)    
    frameppal.pack(fill='both')
    framecerrar = Frame(raiz2)
    framecerrar.config(bg=color_texto_boton)
    framecerrar.pack(fill='both')

    boton_cerrar = Button(framecerrar,text="CERRAR", command=raiz2.destroy)
    boton_cerrar.config(bg=color_fondo_boton, fg=color_texto_boton, pady=10, padx=0)
    boton_cerrar.pack(fill='both')

    # obtengo los datos 
    con = sq3.connect('my-db.db')
    cur = con.cursor()
    query1 = '''
            SELECT alumnos.legajo, alumnos.apellido, alumnos.nombre, alumnos.nota, alumnos.email, 
            escuelas.nombre, escuelas.localidad, escuelas.provincia
            FROM alumnos INNER JOIN escuelas
            ON alumnos.id_escuela = escuelas._id LIMIT 30
            '''
    cur.execute(query1)
    resultado = cur.fetchall()
    cant_filas = len(resultado) # la cantidad de registros para saber cuántas filas
    cant_cols = len(resultado[0]) # obtengo la cantidad de columnas
    
    tabla = Table(frameppal)
    con.close()
    raiz2.mainloop()
'''----------------------------------------------------------------'''
#       Salir
def salir():
    resp = messagebox.askquestion("Confirme","Esta seguro que desea salir?")
    if resp == "yes":
        con.close()
        raiz.destroy()

#   GRÁFICAS
    #Alumnos por escuela
def alumnos_por_escuela():
    query_buscar = '''SELECT COUNT(alumnos.legajo) AS total, escuelas.nombre FROM
    alumnos INNER JOIN escuelas 
    ON alumnos.id_escuela=escuelas._id
    GROUP BY escuelas.nombre
    ORDER BY total DESC'''
    cur.execute(query_buscar)
    resultado = cur.fetchall()

    cantalu=[]
    escuelas=[]

    for i in resultado:
        cantalu.append(i[0])
        escuelas.append(i[1])

    plt.bar(escuelas,cantalu)
    plt.xticks(rotation=45)
    plt.show()

    #Promedio por escuela

def promedio_notas():
    query_buscar ='''SELECT AVG(alumnos.nota) AS "promedio", escuelas.nombre 
    FROM alumnos INNER JOIN escuelas
    ON alumnos.id_escuela = escuelas._id 
    GROUP BY escuelas.nombre 
    ORDER BY promedio'''
    cur.execute(query_buscar)
    resultado = cur.fetchall()
    
    promedio = []
    school = []
    for i in resultado:
        promedio.append(i[0])
        school.append(i[1])
    print(promedio)
    print(school)

    plt.barh(school,promedio,height=0.5)
    
    #Iterando los valores de promedio con función enumarate para mostrar en barras
    for index, value in enumerate(promedio):
        plt.text(value, index,
                    round(float(value),2))
    
    plt.show()


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
def crear():
    id_escuela=int(buscar_escuelas(True)[0])
    datos = id_escuela, legajo.get(),apellido.get(),nombre.get(),calificacion.get(),email.get()
    cur.execute("INSERT INTO alumnos (id_escuela, legajo, apellido,	nombre, nota, email) VALUES (?,?,?,?,?,?)",datos)
    con.commit()
    messagebox.showinfo("Status","Registro agregado")
    limpiar()
#       LEER
def buscar_legajo():
    query_buscar = '''SELECT a.legajo, a.apellido, a.nombre, a.email, a.nota, 
    e.nombre, e.localidad, e.provincia 
    FROM alumnos a INNER JOIN 
    escuelas e ON a.id_escuela=e._id 
    WHERE a.legajo='''
    cur.execute(query_buscar + legajo.get())
    
    resultado = cur.fetchall() #trae lista de tuplas
    if resultado == []:
        messagebox.showerror('No encontrado','No existe numero de legajo')
    else:
        for campo in resultado:
            legajo.set(campo[0])
            apellido.set(campo[1])  
            nombre.set(campo[2])
            email.set(campo[3])  
            calificacion.set(campo[4])  
            escuela.set(campo[5])  
            localidad.set(campo[6])  
            provincia.set(campo[7])
            legajo_input.config(state='disabled')
    
    
#       ACTUALIZAR
def actualizar():
    id_escuela=int(buscar_escuelas(True)[0])
    datos2 = id_escuela, apellido.get(),nombre.get(),calificacion.get(),email.get()
    cur.execute("UPDATE alumnos set id_escuela=?, apellido=?,nombre=?, nota=?, email=? WHERE legajo = " + legajo.get(),datos2)
    con.commit()
    messagebox.showinfo("Status","Registro actualizado")
    limpiar()
    
    
#       BORRAR
def borrar():
    resp = messagebox.askquestion("Confirme","¿Realmente querés borrar registro?")
    if resp == "yes":
        cur.execute("DELETE FROM alumnos WHERE legajo=" + legajo.get())
        con.commit()
        messagebox.showinfo("Status","Registro eliminado correctamente")
        limpiar()


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
bbddmenu.add_command(label="List of students",command=listar)
#exit button
bbddmenu.add_command(label="Exit",command=salir)


######SUB MENU Graficas######
statmenu= Menu(barramenu,tearoff=0) #objeto de clase barramenu
    #comandos SUB MENU Graficas
#students per school button to do grafica
statmenu.add_command(label="Students per school",command=alumnos_por_escuela)
#student score
statmenu.add_command(label="Score",command=promedio_notas)

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

#lista desplegable
escuelas = buscar_escuelas(False)
escuela.set('Seleccione')
escuela_option = OptionMenu(framefields, escuela,*escuelas)
escuela_option.grid(row=5, column=1, padx=10, pady=10, sticky='w', ipadx=50)


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

boton_crear = Button(framebotones, text='Crear',command=crear)
config_buttons(boton_crear, 0)

boton_buscar = Button(framebotones, text='Buscar',command=buscar_legajo)
config_buttons(boton_buscar, 1)

boton_actualizar =Button(framebotones, text='Actualizar',command=actualizar)
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
