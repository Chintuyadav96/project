import tkinter
import tkinter.messagebox
import pickle
from tkinter import *

window = tkinter.Tk()
window.title("To-Do List")
window.minsize(width=100,height=200)
window.maxsize(width=400,height=800)
task_list = []


def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION!!",message="to add a task,please enter a task")

def task_removing():
    global task_list
    task = str(todo_box.get(ANCHOR))
    if task in task_list:
        task.remove(task)
        with open("tasklist.txt",'w')as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        todo_box.delete(ANCHOR)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION!!",message="to Delete a task,please enter a task")
def task_load():
    try:
        todo_task = pickle.load(open("tasks.dat","rb"))
        list_frame.delete(0,tkinter.END)
        for todo in tasks:
            list_frame.inset(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION!!",message="cannot find task.to update")

def task_completed():
     completed=tkinter.messagebox.showinfo(title="CAUTION!!",message="task completed!,Done")
    
        
list_frame = tkinter.Frame(window,bg="black")
list_frame.pack()

todo_box = tkinter.Listbox(list_frame,height=20,width=50)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)

task_add = tkinter.Entry(window,width=70,fg="grey")
task_add.pack()

add_task_button = tkinter.Button(window,text="click to Add Task",font=("arial",15,"bold"),bg="white",command=task_adding,fg="black",bd=6)
add_task_button.pack()

remove_task_button = tkinter.Button(window,text="click to Delete Task",font=("arial",15,"bold"),bg="white",command=task_removing,fg="black",bd=6)
remove_task_button.pack()

load_task_button = tkinter.Button(window,text="Update Task",font=("arial",7,"bold"),bg="white",command=task_load,fg="black",width=11,height=3,bd=6)
load_task_button.pack(side=tkinter.LEFT)
  
task_complete = tkinter.Button(window,text="Task Completed",font=("arial",7,"bold"),bg="white",command=task_completed,fg="black",width=11,height=3,bd=6)
task_complete.pack(side=tkinter.RIGHT)





window.mainloop()

            
       
