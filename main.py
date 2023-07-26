
from collections import UserString
import email
from http.client import UNSUPPORTED_MEDIA_TYPE
import tkinter as tk
from tkinter import W, ttk
import os
win= tk.Tk()
win.title('GUI')


#create labels
name_label=ttk.Label(win, text='Enter your Name : ')
name_label.grid(row=0,column=0, sticky=W)
#.pack()

#email label
email_label=ttk.Label(win,text='Enter your mail id : ')
email_label.grid(row=1,column=0,sticky=tk.W)
#age label
age_label=ttk.Label(win, text='Enter your age : ')
age_label.grid(row=2, column=0, sticky=W)
#pack,grid

#gender_label
gender_label=ttk.Label(win, text='Select your gender : ')
gender_label.grid(row=3,column=0, sticky=W)

#create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=20, textvariable =name_var)
name_entrybox.grid(row=0,column=1,sticky=W)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=20,textvariable=email_var)
email_entrybox.grid(row=1,column=1,sticky=W)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=20,textvariable=age_var)
age_entrybox.grid(row=2,column=1,sticky=W)

#create combobox class
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win, width=16,textvariable=gender_var,state='readonly')
gender_combobox['values']= ('Select','Male','Female','Other')
gender_combobox.current(0)
#gender_combobox
gender_combobox.grid(row=3,column=1,sticky=W)

#radio button
user_type=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='Student',value='Student',variable= user_type)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable= user_type)
radiobtn2.grid(row=4,column=1)

#check button
newsltr_var=tk.IntVar()
newsltr_label= ttk.Checkbutton(win, text='check if you want to subscribe to our newsletter',variable=newsltr_var)
newsltr_label.grid(row=5,columnspan=3)



#create button
def action():
    username= name_var.get()
    userage= age_var.get()
    useremail= email_var.get()
    print(f'{username} is a {userage} years old cutie, send love @ {useremail}')
    usergender=gender_var.get()
    usertype=user_type.get()
    if newsltr_var.get()==0:
        subscribed="No"
    else:
        subscribed="Yes"
    print(f"gender : {usergender} \n user type: {usertype} \n subscribed to newsletter: {subscribed} ")    

    with open('text.txt','a') as f:
        f.write(f"{username} \n {userage} \n {useremail} \n {usergender} \n {usertype} \n {subscribed}")

    name_entrybox.delete(0,tk.END)   
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Blue')
    submit_button.configure(foreground='Blue')




#copying to csv file
def action():
    username= name_var.get()
    userage= age_var.get()
    useremail= email_var.get()
    usergender=gender_var.get()
    usertype=user_type.get()
    if newsltr_var.get()==0:
        subscribed="No"
    else:
        subscribed="Yes"
    
    from csv import DictWriter
    with open('data_entry.csv','a',newline='') as f:
        csv_writer=DictWriter(f,fieldnames=['name','age','email','gender','type','newsletter'])
        if os.stat('data_entry.csv').st_size==0:
            csv_writer.writeheader()

        csv_writer.writerow({
            'name': username,
            'age': userage,
            'email':useremail,
            'gender':usergender,
            'type': usertype,
            'newsletter': subscribed
        })

    name_entrybox.delete(0,tk.END)   
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Blue')
    submit_button.configure(foreground='Blue')

#submit_button= ttk.Button(win, text='Submit',command=action)   (#if change in color is not required)
submit_button= tk.Button(win, text='Submit',command=action)  #(if change in color is required)
submit_button.grid(row=6,columnspan=2)




win.mainloop()
