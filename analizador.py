
from tkinter import Tk 
from tkinter.filedialog import askopenfilename
#from token import token
#from typeToken import typetoken
from curso import curso

class analizador():

    def __init__(self) -> None:
        pass

    def cargarArchivo(self):
        Tk().withdraw()

        try:
            path = askopenfilename(filetypes=[('.lfp','*.lfp'),('*.*','*.*')])
            

            with open(path,encoding='utf-8') as file:
                txt = file.read().strip()
                file.close()
        except:
            print("Error")
            return None

        
        
        return str(txt)


    def anal(self,txt):
        filas = txt.split("\n")
        listCursos=[]

        for obj in filas:
            column = obj.split(",")
            #preRe = column[2].split(";")
            listCursos.append(curso(column[0],column[1],column[2],column[3],column[4],column[5],column[6]))

        return listCursos

    def imprimirCursos(self,listCursos):
        try:
            print("!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!__!_!_!_!_!_!_!_!_!_!_!_!_!_!_")
            for obj in listCursos:
                print("Codigo: " + obj.cod)
                print("Nombre: " + obj.nombre)
                print("Prerequisito: " + obj.preRe)
                print("Obligatorio: " + obj.obl)
                print("Semestre: " + obj.sem)
                print("Créditos: " + obj.cred)
                print("Estado: " + obj.est)
                print("-------------------------------------------------")
        except:
            print("faltan colocar datos")




# #    def analLexico(self,texto):
# #        estado=0
# #        lexema=""
# #        columna=1
# #        fila=1
# #        
# #        tokens= []
#         i=0
#         actual=""
#         long = len(texto)
#         while(i<long and texto[i]!=None):
#             actual=texto[i]

#             if estado==0:
#                 if actual.isalpha():
#                     lexema+=actual
#                     estado=2
#                     i+=1
#                     columna+=1
#                     continue
#                 elif actual.isdigit():
#                     lexema+=actual
#                     estado=1
#                     i+=1
#                     columna+=1
#                     continue
#                 elif actual == '-':
#                     lexema+= actual
#                     tokens.append(token(typetoken.menos,lexema,fila,columna))
#                     lexema=""
#                     i+=1
#                     columna+=1
#                     continue
#                 elif actual== ',':
#                     lexema+=actual
#                     tokens.append(token(typetoken.coma,lexema,fila,columna))
#                     lexema=""
#                     i+=1
#                     columna+=1
#                     continue
#                 elif actual == ';':
#                     lexema+=actual
#                     tokens.append(token(typetoken.puntoComa,lexema,fila,columna))
#                     lexema=""
#                     i+=1
#                     columna+=1
#                     continue
#                 elif actual=='\n':
#                     fila+=1
#                     i+=1
#                     columna=1
#                     continue
#                 elif actual=='\t' or actual=='\r':
#                     i+=1
#                     columna+=5
#                     continue
#                 elif actual==' ':
#                     i+=1
#                     columna+=1
#                     continue
#                 else:
#                     #print("Simbolo " + actual + " no reconocido")
#                     errores+= "Simbolo "+ actual + " no reconocido en columna: "+ str(columna) + " fila: "+ str(fila)+ "\n"
#                     i+=1
#                     columna+=1
#                     continue
#             elif estado==1:
#                 if actual.isdigit():
#                     lexema+=actual
#                     i+=1
#                     columna+=1
#                     continue
#                 else:
#                     tokens.append(token(typetoken.digito,lexema,fila,columna))
#                     lexema=""
#                     estado=0
#                     continue
#             elif estado==2:
#                 if actual!=",":
#                     tokens.append(token(typetoken.nombre,lexema,fila,columna))
#                     estado=0
#                     lexema=""
#                     continue
#                 else:
#                     lexema+=actual
#                     i+=1
#                     columna+=1
#                     continue
        
#         resultados = []
#         resultados.append(tokens)
#         return resultados