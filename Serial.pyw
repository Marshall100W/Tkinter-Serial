### Abril 2024 ###

from tkinter import *
import serial
import time


puerto = 'COM14'
valor = 0
lectura = 1
intentos = 5
Up = False

def conectarse_a_puerto():
    try:
        global serial_XIAO
        serial_XIAO = serial.Serial(puerto, 115200)
        time.sleep(1)
        print('*** Conectado a COM14 ***')
    except:
        print('*** No se pudo conectar a', puerto, '***')
        time.sleep(2)


def lee_datos(valor, lectura):
    try:
        valor = serial_XIAO.readline().decode('ascii')
        valor = valor[slice(0,len(valor)-1)]
        print(valor)
        lab_01 = Label(ventana, text=valor, bg='light green', fg='red')
        lab_01.config(font=('Courier', 30))
        if valor[slice(0,2)] != 'UP':
            lab_01.config(text='                    ')
            lab_01.place(x=70, y=130)
            lab_01 = Label(ventana, text=valor, bg='light green', fg='red')
            lab_01.config(font=('Courier', 30))
            lab_01.place(x=170, y=130)
        else:
            lab_01.place(x=70, y=130)
        lectura = 1
    except:
        print('Error ('+ str(lectura) + ') leyendo puerto ' + puerto, end=' ')
        conectarse_a_puerto()
        lectura += 1
    finally:
        return valor, lectura


def loop_ppal():
    global valor, lectura
    resultado = lee_datos(valor, lectura)
    valor = resultado[0]
    lectura = resultado[1]
    #time.sleep(1)
    ventana.after(1000, loop_ppal)


print('\n\nUP THE IRONS!\n')
conectarse_a_puerto()


ventana = Tk()
ventana.geometry('600x400')
ventana.resizable(False, False)
# frame_01 = Frame(ventana, bg="blue", relief='groove', bd=5)
# frame_01.pack()

lab_01 = Label(ventana, text='UP THE IRONS!', bg='light green', fg='red', relief='groove')
lab_01.config(font=('Courier', 30))
lab_01.pack()

# lab_02 = Label(frame_01, text='UP', bg='light green', fg='red', relief='groove')
# lab_02.config(font=('Courier', 30))
# lab_02.pack()

# frame_02 = Frame(ventana, bg="blue", relief='groove', bd=5)
# frame_02.pack()

# butt_01 = Button(frame_02, text='ON', bg='light grey', fg='black', relief='groove')
# butt_01.config(font=('Courier', 30))
# butt_01.pack(side='left')

# butt_02 = Button(frame_02, text='OFF', bg='light grey', fg='black', relief='groove')
# butt_02.config(font=('Courier', 30))
# butt_02.pack(side='right')

ventana.after(1000, loop_ppal)
ventana.mainloop()
