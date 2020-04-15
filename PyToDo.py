from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
import random



root=Tk()

# Change root window bg colour
root.configure(bg="#373F32")

# Create title
root.title("Todo Helper")

tasks=[]

tasks=["buy vegetables","Laundary", "house clean","PTA meeting"]

fontstyle=tkfont.Font(family="Times New Roman",size=20,weight="bold")

lbl_title = Label(root, text="To-Do-List", bg="black",height=1,width=26,fg="White",font=fontstyle)
lbl_title.grid(row= 0, column=0,columnspan=2)


lbl_title = Label(root,text="# PyJunior #",bg="#4E4E4E",width=60,fg="white")
lbl_title.grid(row= 1, column=0,columnspan=2)


txt_input = Entry(root, width=35)
txt_input.grid(row=2 , column=1, padx=10)

def updatelist():
    lb_tasks.delete(0, "end")
    for task in tasks:
        lb_tasks.insert(END,task)


def addtask(event=None):
    task=txt_input.get()

    if task!="":
        tasks.append(task)
        updatelist()
        lbl_output = Label(root, text="Task Added", bg="black",fg="white",height=2,width=60)
        lbl_output.grid(row=12 , columnspan=2 )
    else:
        messagebox.showwarning("Warning","Please Enter a task !")
    txt_input.delete(0,END)

root.bind('<Return>', addtask)

def numoftasks():
    numoftasks=len(tasks)
    msg="There are {} tasks are saved in the todo list".format(numoftasks)
    lbl_output = Label(root, text=msg, bg="black",fg="white",height=2,width=60)
    lbl_output.grid(row=12 , columnspan=2 )


def delete():
    task=lb_tasks.get("active")
    if task in tasks:
        output=messagebox.askyesno("Confirmation","Do you want to delete **{}** task? ".format(task))
        if output:
            tasks.remove(task)
    updatelist()


def sortlistup():
    tasks.sort()
    updatelist()

def sortlistdown():
    tasks.sort()
    tasks.reverse()
    updatelist()

def deletemall():
    global tasks
    confirmdel=messagebox.askyesno("Confirmation","Do you want to delete all tasks?")
    if confirmdel:
        tasks=[]
    updatelist()

def randomtask():
    randomtask=random.choice(tasks)
    lbl_output = Label(root, text=randomtask, bg="black",fg="white",height=2,width=60)
    lbl_output.grid(row=12 , columnspan=2 )



btn_add_task = Button(root, text="Add Task", fg="black", bg="#949494",width=20,command=addtask)
btn_add_task.grid(row= 2, column=0,padx=20,pady=5)

#btn_select_task = Button(root, text="Select Task", fg="green", bg="white", command=select_task)
#btn_select_task.grid(row= 2, column=0 )

btn_num_tasks = Button(root, text="Number of Tasks", fg="black", bg="#949494",width=20,command=numoftasks)
btn_num_tasks.grid(row=4 , column= 0,pady=5)

btn_delete_task = Button(root, text="Delete Task",fg="black", bg="#949494",width=20,command=delete)
btn_delete_task.grid(row=5 , column=0 ,pady=5)

btn_delete_all = Button(root, text="Delete All",fg="black", bg="#949494",width=20,command=deletemall)
btn_delete_all.grid(row=6 , column= 0,pady=5)

btn_sort_list_up = Button(root, text="Sort List Ascending",fg="black", bg="#949494",width=20,command=sortlistup)
btn_sort_list_up.grid(row=7 , column=0 ,pady=5)

btn_sort_list_down = Button(root, text="Sort List Descending",fg="black", bg="#949494",width=20,command=sortlistdown)
btn_sort_list_down.grid(row=8 , column=0 ,pady=5)

btn_rand_task = Button(root, text="Random Task",fg="black", bg="#949494",width=20,command=randomtask)
btn_rand_task.grid(row=9 , column=0 ,pady=5)


btn_quit_program = Button(root, text="Exit",fg="black", bg="#949494", command=root.quit,width=20)
btn_quit_program.grid(row=10 , column=0,pady=5)

lb_tasks = Listbox(root,width=35,height=13)
lb_tasks.grid(row=3 , column=1, rowspan=7,padx=10)

lbl_git = Label(root, text="github.com/Arivolisankar", bg="#4E4E4E",width=60)
lbl_git.grid(row=11 , columnspan=2 )

lbl_output = Label(root, text="Output", bg="black",height=2,width=60)
lbl_output.grid(row=12 , columnspan=2 )

updatelist()
root.mainloop()