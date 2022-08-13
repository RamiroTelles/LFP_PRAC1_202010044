
#from curses.textpad import Textbox
from tkinter import *
import tkinter 
from analizador import analizador
from tkinter import ttk

#from gestorInterfaz import gestorInterfaz

class menuInicio():


    def __init__(self) -> None:
        self.funciones = analizador()
       

        def bCargar():
            #lee el archivo y hace todo el analisis lexico
            txt = self.funciones.cargarArchivo()
            print(txt)
            pass

        def bGestionar():
            ventana.destroy()
            menuGestionar()
            pass

        def bConteo():
            pass

        def bSalir():
            ventana.destroy()
            exit()
            pass
        
        ventana = Tk()

        ventana.geometry("430x350")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)
        ventana.title("Practica 1 de LFP")

        t_curso = Label(ventana,text="Nombre del curso: Lab. Lenguajes de Programación",font=("Times New Roman",13))
        t_nombre = Label(ventana,text="Nombre del estudiante: Ramiro Agustín Télles Carcuz",font=("Times New Roman",13))
        t_carne = Label(ventana,text="Carné del estudiante: 202010044",font=("Times New Roman",13))

        b_cargar= Button(ventana,text="Cargar Archivo",command=bCargar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_gestionar= Button(ventana,text="Gestionar Cursos",command=bGestionar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_conteo= Button(ventana,text="Conteo de Créditos",command=bConteo, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_salir= Button(ventana,text="Salir",command=bSalir, font=('Times New Roman',13), fg='#000000', bg='#ffffff')

        
        t_curso.place(x=20,y=30)
        t_nombre.place(x=20,y=60)
        t_carne.place(x=20,y=90)

        b_cargar.place(x=160,y=150)
        b_gestionar.place(x=150,y=195)
        b_conteo.place(x=144,y=240)
        b_salir.place(x=190,y=285)

        ventana.mainloop()
        pass

class menuGestionar():

    def __init__(self) -> None:

        def bLista():
            ventana.destroy()
            lista()
            pass

        def bAgrerar():
            ventana.destroy()
            IUcursos(True)
            pass

        def bEditar():
            pass

        def bEliminar():
            #ventana.destroy()
            pass


        def bRegresar():
            ventana.destroy()
            menuInicio()
            pass

        ventana = Tk()
        ventana.geometry("430x350")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)
        ventana.title("Practica 1 de LFP")

        b_lista= Button(ventana,text="Lista Cursos",command=bLista, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_agregar= Button(ventana,text="Agregar Curso",command=bAgrerar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_editar= Button(ventana,text="Editar Curso",command=bEditar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_eliminar= Button(ventana,text="Eliminar Curso",command=bEliminar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_regresar= Button(ventana,text="Regresar",command=bRegresar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')

        b_lista.place(x=163,y=30)
        b_agregar.place(x=156,y=85)
        b_editar.place(x=161,y=140)
        b_eliminar.place(x=154,y=195)
        b_regresar.place(x=171,y=250)

        #ventana.mainloop()
        pass

class lista():

    def __init__(self) -> None:

        def bRegresar():
            ventana.destroy()
            menuGestionar()
            pass

        ventana = Tk()
        ventana.geometry("780x380")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)
        ventana.title("Practica 1 de LFP")

        
        table = ttk.Treeview(ventana,columns=('0','1','2','3','4','5','6'),show='headings',height=9)

        style = ttk.Style()
        style.configure('Treeview',background="silver",foreground="black",rowheight=25,fielbackground="silver")
        style.map('Treeview',background=[('selected','gray')])

        table.grid(row=0, column=0,sticky="nsew",padx=65,pady=40)
        table.column('0',width=48, anchor=CENTER)
        table.column('1',width=230,anchor=CENTER)
        table.column('2',width=75,anchor=CENTER)
        table.column('3',width=80,anchor=CENTER)
        table.column('4',width=58,anchor=CENTER)
        table.column('5',width=55,anchor=CENTER)
        table.column('6',width=100,anchor=CENTER)
        
        table.heading('0', text="Codigo",anchor=CENTER)
        table.heading('1', text="Nombre",anchor=CENTER)
        table.heading('2', text="Prerequisito",anchor=CENTER)
        table.heading('3', text="Opcionalidad",anchor=CENTER)
        table.heading('4', text="Semestre",anchor=CENTER)
        table.heading('5', text="Créditos",anchor=CENTER)
        table.heading('6', text="Estado",anchor=CENTER)

        table.insert("",END,values=("192", "Lenguajes Formales de Programacion","192","Si","10","12","Pendiente"))
        for i in range(20):
            table.insert("",END,values=(i,i,i,i,i,i,i,i))

        #table.place(x=40,y=20)

        scrol = ttk.Scrollbar(ventana,orient=tkinter.VERTICAL,command=table.yview)
        table.configure(yscroll=scrol.set)
        #scrol.place(x=40,y=20)
        scrol.grid(row=0,column=0,sticky='nes',padx=65,pady=40)


        b_regresar= Button(ventana,text="Regresar",command=bRegresar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')

        b_regresar.place(x=680,y=330)

        #ventana.mainloop()
        pass

class IUcursos():

    def __init__(self,bool) -> None:
        
        def bAgregar():
            print("Agregar")
            pass

        def bActu():
            print("Actualizar")
            pass

        def bRegresar():
            ventana.destroy()
            menuGestionar()
            pass

        ventana = Tk()
        ventana.geometry("420x370")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)
        ventana.title("Agregar Curso")


        b_agregar= Button(ventana,text="Agregar Curso", font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_regresar= Button(ventana,text="Regresar",command=bRegresar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_agregar.place(x=150,y=325)
        b_regresar.place(x=300,y=325)

        Label(ventana,text="Codigo",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=40)
        Label(ventana,text="Nombre",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=80)
        Label(ventana,text="Prerequisito",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=120)
        Label(ventana,text="Opcionalidad",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=160)
        Label(ventana,text="Semestre",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=200)
        Label(ventana,text="Créditos",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=240)
        Label(ventana,text="Estado",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=280)
        #b_agregar.config(command=bRegresar)
        t_codigo = Entry(ventana,width=35)
        t_nombre = Entry(ventana,width=35)
        t_pre = Entry(ventana,width=35)
        t_opc = Entry(ventana,width=35)
        t_sem = Entry(ventana,width=35)
        t_cre = Entry(ventana,width=35)
        t_est = Entry(ventana,width=35)

        t_codigo.place(x=175,y=45)
        t_nombre.place(x=175,y=85)
        t_pre.place(x=175,y=125)
        t_opc.place(x=175,y=165)
        t_sem.place(x=175,y=205)
        t_cre.place(x=175,y=245)
        t_est.place(x=175,y=285)

        if bool:
            #si es true, agregar curso
            b_agregar.config(command=bAgregar)
            
        else:

            #si es false, editar curso
            #poner los datos del curso
            b_agregar.config(command=bActu)
            b_agregar.config(text="Editar Curso")
            ventana.title("Editar Curso")
        
        #ventana.mainloop()
        pass

class eliminarCurso():

    def __init__(self) -> None:

        def bEliminar():
            print("Eliminar")
            pass

        def bRegresar():
            ventana.destroy()
            menuGestionar()
            pass

        ventana = Tk()
        ventana.geometry("420x150")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)
        ventana.title("Eliminar Curso")

        b_agregar= Button(ventana,text="Eliminar Curso",command=bEliminar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_regresar= Button(ventana,text="Regresar",command=bRegresar, font=('Times New Roman',13), fg='#000000', bg='#ffffff')
        b_agregar.place(x=150,y=95)
        b_regresar.place(x=300,y=95)

        Label(ventana,text="Codigo de Curso",font=("Times New Roman",13),bg="#00E7CE").place(x=40,y=40)

        t_codigo = Entry(ventana,width=35)
        t_codigo.place(x=175,y=45)


        ventana.mainloop()
        pass