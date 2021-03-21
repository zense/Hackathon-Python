import tkinter as tk
import mysql.connector
window = tk.Tk()
window.title("Contact Tracer")
window.geometry("960x640")
name_var = tk.StringVar()
email_id_var = tk.StringVar()
vaccine_status_var = tk.BooleanVar()
covid_status_var = tk.BooleanVar()
contacts_name_lst = []
contacts_email_id_lst = []
i = 0
def submit():
  sqid=1
  name = name_var.get()
  email_id = email_id_var.get()
  vaccine_status = vaccine_status_var.get()
  covid_status = covid_status_var.get()
  connection = mysql.connector.connect(host="192.168.43.78",database='trackerdb',user='Remote',password='Password')
  cursor = connection.cursor()
  sql = "INSERT INTO Clients (name,email_id,covid_status,vaccine_status) VALUES (%s,%s,%s,%s)"
  val = (name,email_id,covid_status,vaccine_status)
  cursor.execute(sql, val)
  connection.commit()
  cursor.close()
  connection.close()
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
    def add_function(i):
      connection = mysql.connector.connect(host="192.168.43.78",database='trackerdb',user='Remote',password='Password')
      cursor = connection.cursor()
      sql1 = "select email_id from Clients"
      cursor.execute(sql1)
      database=cursor.fetchall()
      connection.commit()
      cursor.close()
      connection.close()
      for email in database:
        if add_email_id_var.get() == email:
          #printing name in table
          e_name = tk.Entry(display, width=20, fg='blue',font=('Arial',16,'bold'))
          e_name.grid(row = i, column=0)
          e_name.insert(tk.END,add_name_var.get())
          #printing email in tabel
          e_email = tk.Entry(display, width=20, fg='blue',font=('Arial',16,'bold'))
          e_email.grid(row=i, column=1)
          e_email.insert(tk.END,add_email_id_var.get())
          #printing covid status
          e_cs = tk.Entry(display, width=20, fg='blue',font=('Arial',16,'bold'))
          e_cs.grid(row=i, column=2)
          e_cs.insert(tk.END,covid_status)
          #printing vaccine status
          e_vs = tk.Entry(display, width=20, fg='blue',font=('Arial',16,'bold'))
          e_vs.grid(row=i, column=3)
          e_vs.insert(tk.END,vaccine_status)
          i += 1
    c_submit = tk.Button(text = "Add",command = add_function(i)).place(x = 100,y = 500) #button in third window
    add_contacts.destroy()
  def update_function():
    update = tk.Tk()
    update.title("Update My Status")
    # email
    email_id_lb = tk.Label(update, text="Email ID ", font=("Times New Roman", 12), bg="white").place(x=60, y=430)
    email_id_entry = tk.Entry(update, textvariable=email_id_var, font=("Times New Roman", 12), bg="white").place(x=280,y=430)
    # covid status
    covid_lb = tk.Label(update, text="Are you infected with Covid-19 ?", font=("Times New Roman", 12),bg="white").place(x=60, y=460)
    covid_r1 = tk.Radiobutton(update, text="Yes", variable=covid_status_var, value=1).place(x=280, y=460)
    covid_r2 = tk.Radiobutton(update, text="No", variable=covid_status_var, value=0).place(x=330, y=460)
    # vaccine status
    vaccine_lb = tk.Label(window, text="Did you get vaccine ?", font=("Times New Roman", 12), bg="white").place(x=60,
                                                                                                                y=490)
    vaccine_r1 = tk.Radiobutton(update, text="Yes", variable=vaccine_status_var, value=1).place(x=280, y=490)
    vaccine_r2 = tk.Radiobutton(update, text="No", variable=vaccine_status_var, value=0).place(x=330, y=490)
    def update_button():
      connection = mysql.connector.connect(host="192.168.43.78",database='trackerdb',user='Remote',password='Password')
      cursor = connection.cursor() 
      sql3= "Update Clients set covid_status=%s,vaccine_status=%s where email_id=%s"
      cursor.execute(sql3,(covid_status_var.get(),vaccine_status_var.get(),email_id_var.get()))
      connection.commit()
      cursor.close()
      connection.close()
    submit_bt = tk.Button(update, text="Update", fg="white", bg="black", command=update_button).place(x=100, y=600)
    update.destroy()
  add_contacts_bt = tk.Button(display, text="Add", command=add).pack()  # button in second window
  update_status = tk.Button(display,text = "Update my status",command = update_function ).pack()          # button in second window
  window.destroy()
#name
name_lb = tk.Label(window,text = "Name", font=("Times New Roman", 12), bg="white").place(x=60,y=400)
name_entry = tk.Entry(window,textvariable = name_var, font=("Times New Roman", 12), bg="white").place(x=280,y=400)
#email
email_id_lb = tk.Label(window,text = "Email ID ", font=("Times New Roman", 12), bg="white").place(x=60,y=430)
email_id_entry = tk.Entry(window,textvariable = email_id_var, font=("Times New Roman", 12), bg="white").place(x=280,y=430)
#covid status
covid_lb = tk.Label(window,text = "Are you infected with Covid-19 ?", font=("Times New Roman", 12), bg="white").place(x=60,y=460)
covid_r1 = tk.Radiobutton(window, text="Yes", variable=covid_status_var, value= 1).place(x=280,y=460)
covid_r2 = tk.Radiobutton(window, text="No", variable=covid_status_var, value= 0).place(x=330,y=460)
#vaccine status
vaccine_lb = tk.Label(window,text = "Did you get vaccine ?", font=("Times New Roman", 12), bg="white").place(x=60,y=490)
vaccine_r1 = tk.Radiobutton(window, text="Yes", variable=vaccine_status_var, value= 1).place(x=280,y=490)
vaccine_r2 = tk.Radiobutton(window, text="No", variable=vaccine_status_var, value= 0).place(x=330,y=490)
#submit button
submit_bt = tk.Button(window,text = "SUBMIT",fg="white", bg="black",command = submit).place(x = 100,y = 600)
window.mainloop()
print(contacts_name_lst)
print(contacts_email_id_lst)
