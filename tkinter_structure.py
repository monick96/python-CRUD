from tkinter import *

#creacion de ventana
raiz = Tk()
raiz.title('GUI-C23222')

##BARRA MENU##
barramenu = Menu(raiz) #objeto de clase Menu() ubicado en raiz 
raiz.config(menu=barramenu)

######SUB MENU ######
barramenu.add_cascade(label="BBDD")
barramenu.add_cascade(label="Graficas")
barramenu.add_cascade(label="Limpiar")
barramenu.add_cascade(label="Acerca de...")







raiz.mainloop()
