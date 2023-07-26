import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox as m_box

win=tk.Tk()
win.title(' ')

#label frame
label_frame=tk.LabelFrame(win,text='Contact Details: ')
label_frame.grid(row=0,column=0)

#labels
label_1=tk.Label(label_frame,text='Enter your name below:',font=('Helvetica',14,'bold'))
label_1.grid(row=1,column=0)
label_2=tk.Label(label_frame,text='Enter your age below:',font=('Helvetica',14,'bold'))
label_2.grid(row=1,column=1)

#entry box variables:
name_var=StringVar()
age_var=StringVar()


#entry boxes 
entry_1=tk.Entry(label_frame,textvariable=name_var)
entry_1.grid(row=2,column=0)
entry_2=tk.Entry(label_frame,textvariable=age_var)
entry_2.grid(row=2,column=1)

def submit():
    #m_box.showinfo('title','content of this message box !! ')
    #m_box.showerror('title','content of this message box !! ')
    #m_box.showwarning('title','content of this message box !! ')
    name=name_var.get()
    age=age_var.get()
    if name=='' or age=='':
        m_box.showerror('Error', 'Please fill both name and age ')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('title','Only digits are allowed in age field')
        else:
            if age<18:
                m_box.showwarning('warning','you are not 18, visit this content at your own risk')
            print(f'{name} : {age}')
#submit button
submit_button = tk.Button(label_frame,text='submit',command=submit)
submit_button.grid(row=3,columnspan=2)



win.mainloop()