from tkinter import *
from tkinter import ttk

from tkinter import messagebox
def do_compute():
    pass
def main():
    global m1_str_var,m2_str_var,m3_str_var
    root_window=Tk()
    root_window.title("Gravitational Force Calculator")
    
    input_frame=ttk.Frame(root_window,padding="3 3 12 12")
    input_frame.grid(column=1,row=1,sticky=(N,W,E,S))
    input_frame.rowconfigure(1,weight=1)
    input_frame.columnconfigure(1,weight=1)
    
    m1_msg=ttk.Label(input_frame)
    m1_msg.configure(text="Enter mass body 1 in kgs:")
    m1_msg.grid(column=1,row=1,sticky=(W,E))
    
    m2_msg=ttk.Label(input_frame)
    m2_msg.configure(text="Enter mass of body 2 in kgs:")
    m2_msg.grid(column=1,row=2,sticky=(W,E))
    
    m3_msg=ttk.Label(input_frame)
    m3_msg.configure(text="Enter the distance between the bodies in meters:")
    m3_msg.grid(column=1,row=3,sticky=(W,E))
    
    m1_str_var=StringVar()
    m1_entry=ttk.Entry(input_frame)
    m1_entry.configure(textvariable=m1_str_var)
    m1_entry.grid(column=2,row=1,sticky=(W,E))
    
    
    m2_str_var=StringVar()
    m2_entry=ttk.Entry(input_frame)
    m1_entry.configure(textvariable=m2_str_var)
    m2_entry.grid(column=2,row=2,sticky=(W,E))
    
    m3_str_var=StringVar()
    m3_entry=ttk.Entry(input_frame)
    m1_entry.configure(textvariable=m3_str_var)
    m3_entry.grid(column=2,row=3,sticky=(W,E))
    
    
    
    
    
    
    
    
    root_window.mainloop()


main()    