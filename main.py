from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("612x408")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

bg = PhotoImage(file="try.png")

root.iconbitmap('icon1.png')

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

Label(root, text = 'RANDOM PASSWORD GENERATOR' , font ='arial 20 bold',bg='black',fg='yellow').pack()
Label(root, text ='Zense Hackathon 2021', font ='arial 20 bold').pack(side = BOTTOM)
Label(root,text='Thank you for Using this software',font='arial 25 bold').pack(side=BOTTOM, pady=40)

Label(root,text='Instructions:',font='arial 15 ').place(x=350 ,y=90)
Label(root,text='1.Kindly enter the length of the password ',font='arial 8 ').place(x=350, y=125)
Label(root, text='required and click on the button to get a ',font='arial 8 ').place(x=350, y=150)
Label(root, text='random password' ,font='arial 8 ').place(x=350, y=175)
Label(root, text='2.You can also copy the password, click on' ,font='arial 8 ').place(x=350, y=200)
Label(root, text='copy to clipboard button :)' ,font='arial 8 ').place(x=350, y=225)


pass_label = Label(root, text = 'Password length', font = 'arial 17 bold',bg='black',fg='green').place(x=1 , y=85)
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 25).place(x=1,y=125)

pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,4):
        Password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


Button(root, text = "GENERATE PASSWORD" , command = Generator ).place(x=1 , y=150)
Entry(root , textvariable = pass_str).place(x=1 ,y=180)

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).place(x=1,y=205)

root.mainloop()