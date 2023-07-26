from cProfile import label
import tkinter as tk
import os
from tkinter import StringVar, ttk,W
from typing import Dict

win=tk.Tk()
win.title('Menubar tutorial')

def func():
    print('func called')

#label
label1=tk.Label(win,text='First Label')
label1.grid(row=0,column=0)

#entrybox
var_1=StringVar()
entry1=tk.Entry(win,width=20,textvariable=var_1)
entry1.grid(row=0,column=1,sticky=W)
entry1.focus()




#csv file
def func():
    user_var=var_1.get()
    
    from csv import DictWriter
    with open('menubar.csv','a') as f:
        csv_writer=DictWriter(f,fieldnames=['Index','string'])
        count=os.stat('menubar.csv').st_size
        if (count==0):
            csv_writer.writeheader()
        csv_writer.writerow({
            'Index': count,
            'string': user_var
        })
        
    print('Data saved in menubar.csv')


# **************Simple Menu****************
#
#menubar = tk.Menu(win)
#
#menubar.add_command(label='Save', command=func)
#menubar.add_command(label='Paste', command=func)
#menubar.add_command(label='Copy', command=func)
#menubar.add_command(label='Cut', command=func)

main_menu=tk.Menu(win)
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='Save', command=func)
file_menu.add_separator()

file_menu.add_command(label='Paste', command=func)
file_menu.add_separator()

file_menu.add_command(label='Copy', command=func)
file_menu.add_separator()

file_menu.add_command(label='Cut', command=func)
file_menu.add_separator()

main_menu.add_cascade(label='File',menu=file_menu)

edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Charts', command=func)
edit_menu.add_separator()

edit_menu.add_command(label='Illustrations', command=func)
edit_menu.add_separator()

edit_menu.add_command(label='tables', command=func)
edit_menu.add_separator()

edit_menu.add_command(label='images', command=func)
edit_menu.add_separator()

main_menu.add_cascade(label='Insert',menu=edit_menu)

win.config(menu=main_menu)

win.mainloop()