#!/usr/bin/python3

from tkinter import *
import random

def generate():
	pwdChars = []
	currLen = 0
	pwd = ""
	
	lc = "abcdefghijklmnopqrstuvwxyz"
	uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sc = "!@#$%^&*_"
	nc = "1234567890"
	cList = [lc, uc, nc, sc]
	
		
	if(int(e1.get()) >= 4):
		chars = []
		lchars = round(int(e1.get()) / 4)
		uchars = round(int(e1.get()) / 4)
		schars = round(int(e1.get()) / 4)
		nchars = round(int(e1.get()) / 4)
			
		currLen = lchars + uchars + schars + nchars
			
		while currLen != int(e1.get()):
			if(currLen > int(e1.get())):
				schars -= 1
				nchars -= 1
				currLen = lchars + uchars + schars + nchars
			
			else:
				lchars += 1
				currLen = lchars + uchars + schars + nchars
			
		for i in range(0,lchars):
			chars.append(lc)
			
		for i in range(0,uchars):
			chars.append(uc)
			
		for i in range(0,schars):
			chars.append(sc)
			
		for i in range(0,nchars):
			chars.append(nc)
			
		i = 0
		while i < int(e1.get()):
			i += 1
			rndChar = random.choices(chars)
			pwdChars += random.choices(rndChar[0])
	
				
	else:
		i = 0
		while i < int(e1.get()):
			i += 1
			rndChar = random.choices(cList)
			pwdChars += random.choices(rndChar[0])
	
	
	for c in pwdChars:
		pwd += c
		
	e2.delete(0,END)
	e2.insert(0,pwd)

top = Tk()
top.geometry("300x150")
top.title("Password Generator")

pwdlen = StringVar(top)

charAmountLabel = Label(top, text="Char amount", font=("Arial", 12)).place(x=20,y=20)

e1 = Spinbox(top, from_=1, to=100, textvariable=pwdlen, width=10, state='readonly')
e1.place(x=20,y=40)
pwdlen.set(8)

gen = Button(top, text="Generate", width=15, command=generate).place(x=120,y=30)

pwdLabel = Label(top, text="Password", font=("Arial", 12)).place(x=20,y=70)
e2 = Entry(top, width=30)
e2.place(x=20,y=90)

noteLabel = Label(top, text="*Password should be atleast 8 characters", font=("Arial", 10)).place(x=20,y=120)

top.mainloop()



	

