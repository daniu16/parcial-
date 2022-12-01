from tkinter import *
import random


print("-------------------------------------------------------------------------------")
print("----diseñar un programa que determine los muneros repetidos en las columnas----")
print("-------------------------------------------------------------------------------")

n=int(input("ingrese el numero que desea que mida la matriz: "))
k=int(input("ingrese ell valor que desea hallar: "))

base=600
altura=600

principal = Tk()
principal.title("matriz de numeros")
principal.geometry("620x620")
principal.resizable(False,False)
principal.config(bg= "lime green")

c = Canvas(principal , width=base , height=altura)
c.place(x=10 , y=10)

ñ=0

u=0
uu=600/n
p=0
pp=600/n

x=20+uu/2
y=20+uu/2

while u<600:
    for i in (0,n+1):
        while u<600:
            if ñ==k:
                color=("green") 
            color = ("red")
            ñ=random.randint(0, 9)
            texto = c.create_text(x+u,y+p, anchor="center", text=ñ, font=("Arial","30", "bold"),fill=color,activefill="green")
            u=u+uu
        p=p+pp
p=p+pp
principal.mainloop()