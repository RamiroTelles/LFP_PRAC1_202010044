from tkinter import Tk 
from tkinter.filedialog import askopenfilename

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
