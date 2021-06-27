#!/usr/bin/env python
# coding: utf-8

# In[275]:


from tkinter import *


# In[276]:


me=Tk()
me.geometry("354x460")
me.title("Calculator")
melabel=Label(me,text="CALCULATOR",bg='white',font=("Times",30,'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')


# In[277]:


textin=StringVar()
operator=''


# In[278]:


def clickbut(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)


# In[279]:


def equlbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=''


# In[280]:


def equlbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=''


# In[281]:


def equlbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=''


# In[282]:


def equlbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=''


# In[283]:


def clrbut():
    textin.set("")


# In[284]:


metext=Entry(me, font=("courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='powder blue')
metext.pack()


# In[285]:


but1=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,"bold"))
but1.place(x=10,y=100)


# In[286]:


but2=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,"bold"))
but2.place(x=10,y=170)


# In[287]:


but3=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,"bold"))
but3.place(x=10,y=240)


# In[288]:


but4=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,"bold"))
but4.place(x=75,y=100)


# In[289]:


but5=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,"bold"))
but5.place(x=75,y=170)


# In[290]:


but6=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,"bold"))
but6.place(x=75,y=240)


# In[291]:


but7=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,"bold"))
but7.place(x=140,y=100)


# In[292]:


but8=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,"bold"))
but8.place(x=140,y=170)


# In[293]:


but9=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,"bold"))
but9.place(x=140,y=240)


# In[294]:


but0=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,"bold"))
but0.place(x=10,y=310)


# In[295]:


butdot=Button(me,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,"bold"))
butdot.place(x=75,y=310)


# In[296]:


butp1=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("+"),text="+",font=("Courier New",16,"bold"))
butp1.place(x=205,y=100)


# In[297]:


butsub=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("-"),text="-",font=("Courier New",16,"bold"))
butsub.place(x=205,y=170)


# In[298]:


butml=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("*"),text="*",font=("Courier New",16,"bold"))
butml.place(x=205,y=240)


# In[299]:


butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("/"),text="/",font=("Courier New",16,"bold"))
butdiv.place(x=205,y=310)


# In[300]:


butclear=Button(me,padx=14,pady=119,bd=4,bg='white',command=clrbut,text="CE",font=("Courier New",16,"bold"))
butclear.place(x=270,y=100)


# In[301]:


butequal=Button(me,padx=151,pady=14,bd=4,bg='white',command=equalbut,text="=",font=("Courier New",16,"bold"))
butequal.place(x=10,y=380)
me.mainloop()


# In[ ]:




