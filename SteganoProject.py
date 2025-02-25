from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

window = Tk()
window.geometry('700x480')
window.config(bg='black')
#Button functions
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File Type',
                                           filetypes=(('PNG files', '*.png'),
                                                      ('JPG files', '*.jpg'),
                                                      ('All file', '*.txt')))
    img = Image.open(open_file)
    img = ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image = img

#Button functions2
def hide():
    global hide_msg
    password = code.get()
    if password =='9090':
        mes = text1.get('1.0', END)
        hide_msg = lsb.hide(str(open_file), mes)
        messagebox.showinfo('success','your message is successfully hidden in a image plz save it')
    elif password == '':
        messagebox.showerror('Error','Please enter secret key')
    else:
        messagebox.showerror('Error','Invalid secret key')
        code.set('')

    msg = text1.get('1.0', END)
    hide_msg = lsb.hide(str(open_file), msg)

#Button functions3
def save_img():
    hide_msg.save('Secret.file.png')
    messagebox.showinfo('saved','Image has been seccessfully saved')

#Button functions4
def show():
    password = code.get()
    if password =='9090':
        show_msg = lsb.reveal(open_file)
        text1.delete('1.0', END)
        text1.insert(END, show_msg)
    elif password == '':
        messagebox.showerror('Error','Please enter secret key')
    else:
        messagebox.showerror('Error','Invalid secret key')
        code.set('')



#logo
logo = PhotoImage(file='hacker.png')
Label(window,image=logo,bd=0).place(x=200,y=0)

#title
Label(window,text='Steganography',font=('Arial',20),bg='black',fg='red').place(x=260,y=12)

#Frames
f1 = Frame(window,width=250,height=220,bd=5, bg='purple')
f1.place(x=50,y=100)
lf1 = Label(f1,bg='purple')
lf1.place(x=0,y=0)

#Frame2
f2 = Frame(window,width=320,height=220,bd=5, bg='white')
f2.place(x=330,y=100)
text1 = Text(f2,font= 'Arial 15 bold',wrap=WORD)
text1.place(x=0,y=0,width=310,height=210)

#Label for Secret Key
Label(window,text='Enter secret key:',font=('Arial',15),bg='black',fg='yellow').place(x=270,y=330)

#entry widget
code=StringVar()
e = Entry(window,textvariable=code,bd=2,font='impact 10 bold',show='*')
e.place(x=260,y=360)

#Buttons
open_button = Button(window,text='Open image',font='ariel 12 bold',bg='blue',fg='white', cursor= 'hand2', command=open_img)
open_button.place(x=60,y=417)

save_button = Button(window,text='Save image',font='ariel 12 bold',bg='green',fg='white', cursor= 'hand2', command=save_img) 
save_button.place(x=190,y=417)

hide_button = Button(window,text='Hide data',font='ariel 12 bold',bg='red',fg='white', cursor= 'hand2', command=hide)
hide_button.place(x=400,y=417)

show_button = Button(window,text='Show data',font='ariel 12 bold',bg='orange',fg='white', cursor= 'hand2', command=show)
show_button.place(x=510,y=417)

mainloop()