import time
from tkinter import *
#Funcion hora 
def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time,bg="black", fg="white", font="Arial 50 bold")
    clock.after(1000,times)
    #Windoww
root= Tk()
root.title("Time")
root.resizable(1,0)
root.config(bg="gray")
clock=Label(root, font=("Arial", 50 ))
clock.grid(row=2, column=1, pady=30, padx=100)
times()
#Etiqueta 
digi=Label(root, text="Hora Actual", font="Arial", fg="Black")
digi.grid(row=0, column=1)
root.mainloop()