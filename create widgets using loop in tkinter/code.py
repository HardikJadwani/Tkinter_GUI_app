#for loop
import tkinter as tk
from tkinter import StringVar, ttk


win=tk.Tk()
win.title('LOOP')

labels= ['What is your name : ' , 'what is your age ', 'what is your gender : ','country : ',
'state : ', 'city : ','address : ']

for i in range(len(labels)):
    cur_label='label' + str(i)
    cur_label=ttk.Label(win, text = labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

#entrybox
#box={'name','age','gender','country','state','city'}
#for j in range(len(box)):
#    cur_var='entrybox' + str(j)
#    cur_var=tk.StringVar()
#    entrybox=ttk.Entry(win,width=16,textvariable=box[j])
#    entrybox.grid(row=j,column=1,sticky=tk.W)
#    if j==0:
#        entrybox.focus()

#entry box
user_info={
    'name': tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar(),
    'address':tk.StringVar(),


}
counter=0
for i in user_info:
    cur_entrybox='entry' + i
    cur_entrybox=ttk.Entry(win, width=16,textvariable=user_info[i])
    cur_entrybox.grid(column=1,row=counter)
    counter+=1

def Submit():
    
    
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())
    print(user_info['address'].get())


submit_btn=ttk.Button(win,text='Submit',command=Submit)
submit_btn.grid(row=counter+1,columnspan=2)
win.mainloop()