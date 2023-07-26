import tkinter as tk
from tkinter import StringVar, ttk


win=tk.Tk()
win.title('Label Frame')
label_frame= ttk.Labelframe(win,text='Enter your details below')
label_frame.grid(row=0,column=0,padx=40,pady=20)

labels= ['What is your name : ' , 'what is your age ', 'what is your gender : ','country : ',
'state : ', 'city : ','address : ']

for i in range(len(labels)):
    cur_label='label' + str(i)
    cur_label=ttk.Label(label_frame, text = labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

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
    cur_entrybox=ttk.Entry(label_frame, width=16,textvariable=user_info[i])
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


submit_btn=ttk.Button(label_frame,text='Submit',command=Submit)
submit_btn.grid(row=counter+1,columnspan=2)

for child in label_frame.winfo_children():
    child.grid_configure(padx=4,pady=4)

win.mainloop()