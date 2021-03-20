import tkinter as tk
window = tk.Tk()
window.title("Contact Tracer")
window.geometry("960x640")
img = tk.PhotoImage(file="window.png")
imglbl = tk.Label(window, image=img)
imglbl.place(x=0, y=0)
name_var = tk.StringVar()
email_id_var = tk.StringVar()
vaccine_status_var = tk.BooleanVar()
covid_status_var = tk.BooleanVar()
contacts_name_lst = []
contacts_email_id_lst = []
#function when submit button is clicked
def submit():
  name = name_var.get()
  email_id = email_id_var.get()
  vaccine_status = vaccine_status_var.get()
  covid_status = covid_status_var.get()
  display = tk.Tk()
  display.title("Add Your Contacts")
  def add():
    add_contacts = tk.Tk()
    add_contacts.title("Contacts Information")
    add_name_var = tk.StringVar()
    add_email_id_var = tk.StringVar()
    #name
    c_name_lb = tk.Label(add_contacts,text = "Name", font=("Times New Roman", 12), bg="white").place(x=60,y=400)
    name_entry = tk.Entry(add_contacts,textvariable = add_name_var, font=("Times New Roman", 12), bg="white").place(x=280,y=400)
    #email
    c_email_id_lb = tk.Label(add_contacts,text = "Email ID ", font=("Times New Roman", 12), bg="white").place(x=60,y=430)
    c_email_id_entry = tk.Entry(add_contacts,textvariable = add_email_id_var, font=("Times New Roman", 12), bg="white").place(x=280,y=430)
    def add_button():
      contacts_name_lst.append(add_name_var.get())
      contacts_email_id_lst.append(add_email_id_var.get())
      add_contacts.destroy()
    c_submit = tk.Button(text = "Add",command = add_button).place(x = 100,y = 500)
    add_contacts.mainloop()
  add_contacts_bt = tk.Button(display, text="Add", command=add).pack()
  window.destroy()
#name
name_lb = tk.Label(window,text = "Name", font=("Times New Roman", 12), bg="white").place(x=60,y=400)
name_entry = tk.Entry(window,textvariable = name_var, font=("Times New Roman", 12), bg="white").place(x=280,y=400)
#email
email_id_lb = tk.Label(window,text = "Email ID ", font=("Times New Roman", 12), bg="white").place(x=60,y=430)
email_id_entry = tk.Entry(window,textvariable = email_id_var, font=("Times New Roman", 12), bg="white").place(x=280,y=430)
#covid status
covid_lb = tk.Label(window,text = "Are you infected with Covid-19 ?", font=("Times New Roman", 12), bg="white").place(x=60,y=460)
covid_r1 = tk.Radiobutton(window, text="Yes", variable=covid_status_var, value= True).place(x=280,y=460)
covid_r2 = tk.Radiobutton(window, text="No", variable=covid_status_var, value= False).place(x=330,y=460)
#vaccine status
vaccine_lb = tk.Label(window,text = "Did you get vaccine ?", font=("Times New Roman", 12), bg="white").place(x=60,y=490)
vaccine_r1 = tk.Radiobutton(window, text="Yes", variable=vaccine_status_var, value= True).place(x=280,y=490)
vaccine_r2 = tk.Radiobutton(window, text="No", variable=vaccine_status_var, value= False).place(x=330,y=490)
#submit button
submit_bt = tk.Button(window,text = "SUBMIT",fg="white", bg="black",command = submit).place(x = 100,y = 600)
window.mainloop()
print(contacts_name_lst)
print(contacts_email_id_lst)