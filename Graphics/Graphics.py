
from tkinter import*
from tkinter import ttk 

c=0

def clicker(event): 
    global c
    c+=1 
    lbl.configure(text=c)
def clicker1(event): 
    global c 
    if c>0:  
        c-=1 
   
        
    lbl.configure(text=c)

def entry_to_label(event): 
    text=ent.get() 
    lbl.configure(text=text) 
    ent.delete(0, END) #0,END or  5,10 will remove 5, 10 elements 

def choice(): 
    text=var.get()       # take from variable var
    ent.insert(END, text) # 0 start END 

def new_window(ind:int): 
    def tab_choice(ind:int): 
        newwindow.title(texts[ind])

    newwindow=Toplevel() 
    tabs=ttk.Notebook(newwindow) 
    texts=['First','Second','Third','Fourth'] 
    tab=[]
    for i in range(len(texts)): 
        tab.append('tab'+str(i))    
        tab[i]=Frame(tabs) 
        tabs.add(tab[i],text=texts[i]) 
        tab[i].bind('<Button 1>',tab_choice(i))
    tabs.grid(row=0,column=0) 
    tabs.select(ind) 




    newwindow.title(texts[ind]) 
    newwindow.mainloop() 









window=Tk()#responds for formation 
window.title('The first window') 
window.geometry('600x300')# change size
m=Menu(window) 
window.config(menu=m) 
m1=Menu(m) # add to menu menu 
m.add_cascade(label='Tabs', menu=m1) # what is going to be in menu 
m1.add_command(label='Tabs1', accelerator='Command+A', command=lambda:new_window(0))
m1.add_command(label='Tabs2', accelerator='Command+B', command=lambda:new_window(1)) 
m1.add_command(label='Tabs3', accelerator='Command+C', command=lambda:new_window(2)) 
m1.add_command(label='Tabs4', accelerator='Command+D', command=lambda:new_window(3))










lbl=Label(window,text='.....', font='Arial 20') 

btn=Button(window, text='Press',font='Arial 20', fg='black', bg='#32a852',width=30, height=5, relief=RAISED) #GROOVE,SUNKEN,RAISED .pack()

ent=Entry(window,fg='black', bg='#32a852' , width=30, justify=CENTER) #Text box


var=IntVar() #stringVar() 
r1=Radiobutton(window, text='first', width=30, font='Arial 20', variable=var, value=1, command=choice ) 

r2=Radiobutton(window, text='Second', width=30, font='Arial 20',  variable=var, value=2, command=choice  )

btn.bind('<Button-1>', clicker)   # 1 left 3 right #2 wheel. connection beetwen button and action
btn.bind('<Button-3>', clicker1)   
ent.bind('<Return>', entry_to_label) #Enter
btn.pack()
lbl.pack() 
ent.pack()
r1.pack(side=LEFT) #from left to right
r2.pack(side=LEFT)

window.mainloop() # start the window
