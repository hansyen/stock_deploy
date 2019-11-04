
print("ohya0915@gmail.com")


import pandas as pd
import pandas_datareader.data as web
import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import *
from tkinter.messagebox import showinfo
import requests
from bs4 import BeautifulSoup
import sys
import numpy as np
import matplotlib.pyplot as plt



print("please wait the program is loading...")


src="https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.60494800%201544016777"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data1=sp.find_all("table") 

a=data1[4].text
a=a.replace("\n \n\n","@")
a=a.replace("\n\n\n\n","@")
a=a.replace("\n\n","\n")
a=a.replace("\n",",")
a=a.replace("@","\n")



src="https://tw.stock.yahoo.com/s/list.php?c=%AD%B9%AB%7E&rr=0.35528600%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data2=sp.find_all("table") 

b=data2[4].text
b=b.replace("\n \n\n","@")
b=b.replace("\n\n\n\n","@")
b=b.replace("\n\n","\n")
b=b.replace("\n",",")
b=b.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.35528700%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data3=sp.find_all("table") 

c=data3[4].text
c=c.replace("\n \n\n","@")
c=c.replace("\n\n\n\n","@")
c=c.replace("\n\n","\n")
c=c.replace("\n",",")
c=c.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%AF%BC%C2%B4&rr=0.35528900%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data4=sp.find_all("table") 

d=data4[4].text
d=d.replace("\n \n\n","@")
d=d.replace("\n\n\n\n","@")
d=d.replace("\n\n","\n")
d=d.replace("\n",",")
d=d.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%F7&rr=0.35529000%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data5=sp.find_all("table") 

e=data5[4].text
e=e.replace("\n \n\n","@")
e=e.replace("\n\n\n\n","@")
e=e.replace("\n\n","\n")
e=e.replace("\n",",")
e=e.replace("@","\n")



print("25% completed...")


src="https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%B9%B9q%C6l&rr=0.35529200%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data6=sp.find_all("table") 

f=data6[4].text
f=f.replace("\n \n\n","@")
f=f.replace("\n\n\n\n","@")
f=f.replace("\n\n","\n")
f=f.replace("\n",",")
f=f.replace("@","\n")



src="https://tw.stock.yahoo.com/s/list.php?c=%A4%C6%BE%C7&rr=0.35529300%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data7=sp.find_all("table") 

g=data7[4].text
g=g.replace("\n \n\n","@")
g=g.replace("\n\n\n\n","@")
g=g.replace("\n\n","\n")
g=g.replace("\n",",")
g=g.replace("@","\n")



src="https://tw.stock.yahoo.com/s/list.php?c=%A5%CD%A7%DE%C2%E5%C0%F8&rr=0.35529400%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data8=sp.find_all("table") 

h=data8[4].text
h=h.replace("\n \n\n","@")
h=h.replace("\n\n\n\n","@")
h=h.replace("\n\n","\n")
h=h.replace("\n",",")
h=h.replace("@","\n")



src="https://tw.stock.yahoo.com/s/list.php?c=%AC%C1%BC%FE&rr=0.35529600%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data9=sp.find_all("table") 

i=data9[4].text
i=i.replace("\n \n\n","@")
i=i.replace("\n\n\n\n","@")
i=i.replace("\n\n","\n")
i=i.replace("\n",",")
i=i.replace("@","\n")



src="https://tw.stock.yahoo.com/s/list.php?c=%B3y%AF%C8&rr=0.35529700%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data10=sp.find_all("table") 

j=data10[4].text
j=j.replace("\n \n\n","@")
j=j.replace("\n\n\n\n","@")
j=j.replace("\n\n","\n")
j=j.replace("\n",",")
j=j.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%BF%FB%C5K&rr=0.35529800%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data11=sp.find_all("table") 

k=data11[4].text
k=k.replace("\n \n\n","@")
k=k.replace("\n\n\n\n","@")
k=k.replace("\n\n","\n")
k=k.replace("\n",",")
k=k.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%BE%F3%BD%A6&rr=0.35530000%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data12=sp.find_all("table") 

l=data12[4].text
l=l.replace("\n \n\n","@")
l=l.replace("\n\n\n\n","@")
l=l.replace("\n\n","\n")
l=l.replace("\n",",")
l=l.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%A8T%A8%AE&rr=0.35530100%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data13=sp.find_all("table") 

m=data13[4].text
m=m.replace("\n \n\n","@")
m=m.replace("\n\n\n\n","@")
m=m.replace("\n\n","\n")
m=m.replace("\n",",")
m=m.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%A5b%BE%C9%C5%E9&rr=0.35530200%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data14=sp.find_all("table") 

n=data14[4].text
n=n.replace("\n \n\n","@")
n=n.replace("\n\n\n\n","@")
n=n.replace("\n\n","\n")
n=n.replace("\n",",")
n=n.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B9q%B8%A3%B6g%C3%E4&rr=0.35530300%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data15=sp.find_all("table") 

o=data15[4].text
o=o.replace("\n \n\n","@")
o=o.replace("\n\n\n\n","@")
o=o.replace("\n\n","\n")
o=o.replace("\n",",")
o=o.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%A5%FA%B9q&rr=0.35530500%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data16=sp.find_all("table") 

p=data16[4].text
p=p.replace("\n \n\n","@")
p=p.replace("\n\n\n\n","@")
p=p.replace("\n\n","\n")
p=p.replace("\n",",")
p=p.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B3q%ABH%BA%F4%B8%F4&rr=0.35530600%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data17=sp.find_all("table") 

q=data17[4].text
q=q.replace("\n \n\n","@")
q=q.replace("\n\n\n\n","@")
q=q.replace("\n\n","\n")
q=q.replace("\n",",")
q=q.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B9s%B2%D5%A5%F3&rr=0.35530700%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data18=sp.find_all("table") 

r=data18[4].text
r=r.replace("\n \n\n","@")
r=r.replace("\n\n\n\n","@")
r=r.replace("\n\n","\n")
r=r.replace("\n",",")
r=r.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B3q%B8%F4&rr=0.35530900%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data19=sp.find_all("table") 

s=data19[4].text
s=s.replace("\n \n\n","@")
s=s.replace("\n\n\n\n","@")
s=s.replace("\n\n","\n")
s=s.replace("\n",",")
s=s.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B8%EA%B0T%AAA%B0%C8&rr=0.35531000%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data20=sp.find_all("table") 

t=data20[4].text
t=t.replace("\n \n\n","@")
t=t.replace("\n\n\n\n","@")
t=t.replace("\n\n","\n")
t=t.replace("\n",",")
t=t.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5%A6%B9q%A4l&rr=0.35531100%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data21=sp.find_all("table") 

u=data21[4].text
u=u.replace("\n \n\n","@")
u=u.replace("\n\n\n\n","@")
u=u.replace("\n\n","\n")
u=u.replace("\n",",")
u=u.replace("@","\n")

print("please wait the program is loading...")



src="https://tw.stock.yahoo.com/s/list.php?c=%C0%E7%AB%D8&rr=0.35531200%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data22=sp.find_all("table") 

v=data22[4].text
v=v.replace("\n \n\n","@")
v=v.replace("\n\n\n\n","@")
v=v.replace("\n\n","\n")
v=v.replace("\n",",")
v=v.replace("@","\n")



src="https://tw.stock.yahoo.com/s/list.php?c=%AF%E8%B9B&rr=0.35531400%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data23=sp.find_all("table") 

w=data23[4].text
w=w.replace("\n \n\n","@")
w=w.replace("\n\n\n\n","@")
w=w.replace("\n\n","\n")
w=w.replace("\n",",")
w=w.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%C6%5B%A5%FA&rr=0.35531500%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data24=sp.find_all("table") 

x=data24[4].text
x=x.replace("\n \n\n","@")
x=x.replace("\n\n\n\n","@")
x=x.replace("\n\n","\n")
x=x.replace("\n",",")
x=x.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%AA%F7%BF%C4&rr=0.35531600%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data25=sp.find_all("table") 

y=data25[4].text
y=y.replace("\n \n\n","@")
y=y.replace("\n\n\n\n","@")
y=y.replace("\n\n","\n")
y=y.replace("\n",",")
y=y.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%B6T%A9%F6%A6%CA%B3f&rr=0.35531700%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data26=sp.find_all("table") 

z=data26[4].text
z=z.replace("\n \n\n","@")
z=z.replace("\n\n\n\n","@")
z=z.replace("\n\n","\n")
z=z.replace("\n",",")
z=z.replace("@","\n")


print("50% completed...")

src="https://tw.stock.yahoo.com/s/list.php?c=%AAo%B9q%BFU%AE%F0&rr=0.35531800%201535770407h"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data27=sp.find_all("table") 

A=data27[4].text
A=A.replace("\n \n\n","@")
A=A.replace("\n\n\n\n","@")
A=A.replace("\n\n","\n")
A=A.replace("\n",",")
A=A.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5L&rr=0.35532000%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data28=sp.find_all("table") 

B=data28[4].text
B=B.replace("\n \n\n","@")
B=B.replace("\n\n\n\n","@")
B=B.replace("\n\n","\n")
B=B.replace("\n",",")
B=B.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%A6s%B0U%BE%CC%C3%D2&rr=0.35532100%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data29=sp.find_all("table") 

C=data29[4].text
C=C.replace("\n \n\n","@")
C=C.replace("\n\n\n\n","@")
C=C.replace("\n\n","\n")
C=C.replace("\n",",")
C=C.replace("@","\n")







src="https://tw.stock.yahoo.com/s/list.php?c=%AB%FC%BC%C6%C3%FE&rr=0.35532500%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data32=sp.find_all("table") 

F=data32[4].text
F=F.replace("\n \n\n","@")
F=F.replace("\n\n\n\n","@")
F=F.replace("\n\n","\n")
F=F.replace("\n",",")
F=F.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=ETF&rr=0.35532600%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data33=sp.find_all("table") 

G=data33[4].text
G=G.replace("\n \n\n","@")
G=G.replace("\n\n\n\n","@")
G=G.replace("\n\n","\n")
G=G.replace("\n",",")
G=G.replace("@","\n")




src="https://tw.stock.yahoo.com/s/list.php?c=%A8%FC%AFq%C3%D2%A8%E9&rr=0.35532700%201535770407"
html=requests.get(src)
html.encoding="cp950"

sp=BeautifulSoup(html.text,"html.parser")

data34=sp.find_all("table") 

H=data34[4].text
H=H.replace("\n \n\n","@")
H=H.replace("\n\n\n\n","@")
H=H.replace("\n\n","\n")
H=H.replace("\n",",")
H=H.replace("@","\n")


print("please wait the program is loading...")



win=tk.Tk()
win.title("ohya0915@gmail.com")
lable=tk.Label(win, text="This version is for test not for product.")
lable.grid(column=0,row=0,columnspan=5)

lable=tk.Label(win, text="Taiwan stock :")
lable.grid(column=0,row=1)


tt=Text(win,heigh=30,width=80)

entry1=tk.Entry(win,width=10)
entry2=tk.Entry(win,width=10)
entry3=tk.Entry(win,width=10)
entry4=tk.Entry(win,width=10)
entry5=tk.Entry(win,width=10)
entry6=tk.Entry(win,width=10)
entry7=tk.Entry(win,width=10)


lable=tk.Label(win, text="Start year"+"\n"+"(ex:2018)")
lable.grid(column=0,row=8)
lable=tk.Label(win, text="Month"+"\n"+"(ex:1)")
lable.grid(column=2,row=8)
lable=tk.Label(win, text="Date"+"\n"+"(ex:1)")
lable.grid(column=4,row=8)
lable=tk.Label(win, text="End year"+"\n"+"(ex:2018)")
lable.grid(column=0,row=9)
lable=tk.Label(win, text="Month"+"\n"+"(ex:7)")
lable.grid(column=2,row=9)
lable=tk.Label(win, text="Date"+"\n"+"(ex:7)")
lable.grid(column=4,row=9)

lable=tk.Label(win, text="Taiwan stock NO."+"\n"+"(ex:2330.TW)")
lable.grid(column=0,row=10)

lable=tk.Label(win, text="or Stock name"+"\n"+"(ex:AAPL,GOOG)")
lable.grid(column=2,row=10)

lable=tk.Label(win, text="Max=9999 datas")
lable.grid(column=0,row=11)

pd.set_option('display.max_rows',9999)
pd.set_option('display.max_columns',9999)


print("75% completed...")



def collect():
    win=tk.Tk()
    win.title("ohya0915@gmail.com")
    lable=tk.Label(win, text="This version is for test not for product.")
    lable.grid(column=0,row=0,columnspan=5)
   

    start=datetime.datetime(int(entry1.get()),int(entry2.get()),int(entry3.get()))
    end=datetime.datetime(int(entry4.get()),int(entry5.get()),int(entry6.get()))
    stock=entry7.get()
    result=web.DataReader(stock,'yahoo',start,end)

    tt.delete(1.0,END)
    tt.insert(END,result)
    
    def highplot():

        result['High'].plot()
        
        plt.show()

    lable=tk.Label(win, text="high is the highest price of the stock on that trading day")
    lable.grid(column=1,row=1)

    button=tk.Button(win,text="High",command=highplot) 
    button.grid(column=0,row=1,padx=5,pady=5)
   
    def lowplot():
        result['Low'].plot()
        
        plt.show()

    lable=tk.Label(win, text="low is the lowest price of the stock on that trading day")
    lable.grid(column=1,row=2)

    button=tk.Button(win,text="Low",command=lowplot) 
    button.grid(column=0,row=2,padx=5,pady=5)
    
    def openplot():
        result['Open'].plot()
        
        plt.show()

    lable=tk.Label(win, text="Open is the price of the stock at the beginning of the trading day (it need not be the closing price of the previous trading day)")
    lable.grid(column=1,row=3)

    button=tk.Button(win,text="Open",command=openplot) 
    button.grid(column=0,row=3,padx=5,pady=5)

    def closeplot():
        result['Close'].plot()
        
        plt.show()

    lable=tk.Label(win, text="close is the price of the stock at closing time.")
    lable.grid(column=1,row=4)

    button=tk.Button(win,text="Close",command=closeplot) 
    button.grid(column=0,row=4,padx=5,pady=5)

    def volumeplot():
        result['Volume'].plot()
       
        plt.show()
    
    lable=tk.Label(win, text="Volume indicates how many stocks were traded")
    lable.grid(column=1,row=5)

    button=tk.Button(win,text="Volume",command=volumeplot)
    button.grid(column=0,row=5,padx=5,pady=5)


    def adjcloseplot():
        result['Adj Close'].plot()
        
        plt.show()

    lable=tk.Label(win, text="Adjusted close is the closing price of the stock that adjusts the price of the stock for corporate actions")
    lable.grid(column=1,row=6)

    button=tk.Button(win,text="Adj Close",command=adjcloseplot) 
    button.grid(column=0,row=6,padx=5,pady=5)    
   

    win.mainloop()    


    
def click1():
    tt.delete(1.0,END)
    tt.insert(END,a[4:len(a)-1])

def click2():
    tt.delete(1.0,END)
    tt.insert(END,b[4:len(b)-1])

def click3():
    tt.delete(1.0,END)
    tt.insert(END,c[4:len(c)-1])

def click4():
    tt.delete(1.0,END)
    tt.insert(END,d[4:len(d)-1])

def click5():
    tt.delete(1.0,END)
    tt.insert(END,e[4:len(e)-1])
    
def click6():
    tt.delete(1.0,END)
    tt.insert(END,f[4:len(f)-1])
    
def click7():
    tt.delete(1.0,END)
    tt.insert(END,g[4:len(g)-1])
    
def click8():
    tt.delete(1.0,END)
    tt.insert(END,h[4:len(h)-1])
    
def click9():
    tt.delete(1.0,END)
    tt.insert(END,i[4:len(i)-1])
 
def click10():
    tt.delete(1.0,END)
    tt.insert(END,j[4:len(j)-1])
    
def click11():
    tt.delete(1.0,END)
    tt.insert(END,k[4:len(k)-1])
    
def click12():
    tt.delete(1.0,END)
    tt.insert(END,l[4:len(l)-1])
    
def click13():
    tt.delete(1.0,END)
    tt.insert(END,m[4:len(m)-1])
    
def click14():
    tt.delete(1.0,END)
    tt.insert(END,n[4:len(n)-1])
    
def click15():
    tt.delete(1.0,END)
    tt.insert(END,o[4:len(o)-1])
    
def click16():
    tt.delete(1.0,END)
    tt.insert(END,p[4:len(p)-1])
    
def click17():
    tt.delete(1.0,END)
    tt.insert(END,q[4:len(q)-1])
    
def click18():
    tt.delete(1.0,END)
    tt.insert(END,r[4:len(r)-1])
    
def click19():
    tt.delete(1.0,END)
    tt.insert(END,s[4:len(s)-1])
    
def click20():
    tt.delete(1.0,END)
    tt.insert(END,t[4:len(t)-1])
    
def click21():
    tt.delete(1.0,END)
    tt.insert(END,u[4:len(u)-1])
    
def click22():
    tt.delete(1.0,END)
    tt.insert(END,v[4:len(v)-1])
    
def click23():
    tt.delete(1.0,END)
    tt.insert(END,w[4:len(w)-1])
    
def click24():
    tt.delete(1.0,END)
    tt.insert(END,x[4:len(x)-1])
    
def click25():
    tt.delete(1.0,END)
    tt.insert(END,y[4:len(y)-1])
    
def click26():
    tt.delete(1.0,END)
    tt.insert(END,z[4:len(z)-1])
    
def click27():
    tt.delete(1.0,END)
    tt.insert(END,A[4:len(A)-1])
    
def click28():
    tt.delete(1.0,END)
    tt.insert(END,B[4:len(B)-1])
    
def click29():
    tt.delete(1.0,END)
    tt.insert(END,C[4:len(C)-1])
    
def click30():
    tt.delete(1.0,END)
    tt.insert(END,F[4:len(F)-1])
    
def click31():
    tt.delete(1.0,END)
    tt.insert(END,G[4:len(G)-1])
    
def click32():
    tt.delete(1.0,END)
    tt.insert(END,H[4:len(H)-1])
    


def click999():
    win.destroy()





button=tk.Button(win, text="Cement"+"\n"+"class",command=click1)
button.grid(column=1,row=1,padx=5,pady=5)
button=tk.Button(win, text="Food"+"\n"+"class",command=click2)
button.grid(column=2,row=1,padx=5,pady=5)
button=tk.Button(win, text="Plastic"+"\n"+"class",command=click3)
button.grid(column=3,row=1,padx=5,pady=5)
button=tk.Button(win, text="Textile"+"\n"+"class",command=click4)
button.grid(column=4,row=1,padx=5,pady=5)
button=tk.Button(win, text="Motor"+"\n"+"class",command=click5)
button.grid(column=5,row=1,padx=5,pady=5)
button=tk.Button(win, text="Electrical"+"\n"+"cable",command=click6)
button.grid(column=0,row=2,padx=5,pady=5)
button=tk.Button(win, text="Chemistry"+"\n"+"class",command=click7)
button.grid(column=1,row=2,padx=5,pady=5)
button=tk.Button(win, text="Biomedical"+"\n"+"class",command=click8)
button.grid(column=2,row=2,padx=5,pady=5)
button=tk.Button(win, text="Glass"+"\n"+"class",command=click9)
button.grid(column=3,row=2,padx=5,pady=5)
button=tk.Button(win, text="Paper"+"\n"+"class",command=click10)
button.grid(column=4,row=2,padx=5,pady=5)
button=tk.Button(win, text="Steel"+"\n"+"class",command=click11)
button.grid(column=5,row=2,padx=5,pady=5)
button=tk.Button(win, text="Rubber"+"\n"+"class",command=click12)
button.grid(column=0,row=3,padx=5,pady=5)
button=tk.Button(win, text="Car"+"\n"+"class",command=click13)
button.grid(column=1,row=3,padx=5,pady=5)
button=tk.Button(win, text="Semiconductor"+"\n"+"class",command=click14)
button.grid(column=2,row=3,padx=5,pady=5)
button=tk.Button(win, text="Computer"+"\n"+"Peripherals",command=click15)
button.grid(column=3,row=3,padx=5,pady=5)
button=tk.Button(win, text="Photovoltaic"+"\n"+"industry",command=click16)
button.grid(column=4,row=3,padx=5,pady=5)
button=tk.Button(win, text="Communication"+"\n"+"network",command=click17)
button.grid(column=5,row=3,padx=5,pady=5)
button=tk.Button(win, text="Electronic"+"\n"+"components",command=click18)
button.grid(column=0,row=4,padx=5,pady=5)
button=tk.Button(win, text="Electronic"+"\n"+"pathway",command=click19)
button.grid(column=1,row=4,padx=5,pady=5)
button=tk.Button(win, text="Information"+"\n"+"service",command=click20)
button.grid(column=2,row=4,padx=5,pady=5)
button=tk.Button(win, text="Other"+"\n"+"electronics",command=click21)
button.grid(column=3,row=4,padx=5,pady=5)
button=tk.Button(win, text="Construction"+"\n"+"class",command=click22)
button.grid(column=4,row=4,padx=5,pady=5)
button=tk.Button(win, text="Shipping"+"\n"+"class",command=click23)
button.grid(column=5,row=4,padx=5,pady=5)
button=tk.Button(win, text="Travel"+"\n"+"class",command=click24)
button.grid(column=0,row=5,padx=5,pady=5)
button=tk.Button(win, text="Financial"+"\n"+"class",command=click25)
button.grid(column=1,row=5,padx=5,pady=5)
button=tk.Button(win, text="Department"+"\n"+"store",command=click26)
button.grid(column=2,row=5,padx=5,pady=5)
button=tk.Button(win, text="Oil"+"\n"+"gas",command=click27)
button.grid(column=3,row=5,padx=5,pady=5)
button=tk.Button(win, text="Other",command=click28)
button.grid(column=4,row=5,padx=5,pady=5)
button=tk.Button(win, text="Depository"+"\n"+"receipt",command=click29)
button.grid(column=5,row=5,padx=5,pady=5)
button=tk.Button(win, text="Index"+"\n"+"class",command=click30)
button.grid(column=0,row=6,padx=5,pady=5)
button=tk.Button(win, text="ETF",command=click31)
button.grid(column=1,row=6,padx=5,pady=5)
button=tk.Button(win, text="Beneficiary"+"\n"+"securities",command=click32)
button.grid(column=2,row=6,padx=5,pady=5)


button=tk.Button(win,text="collect data",command=collect) 
button.grid(column=3,row=10,padx=5,pady=5)



button=tk.Button(win, text="Exit",command=click999)
button.grid(column=2,row=14,padx=5,pady=5)


entry1.grid(column=1,row=8)
entry2.grid(column=3,row=8)
entry3.grid(column=5,row=8)
entry4.grid(column=1,row=9)
entry5.grid(column=3,row=9)
entry6.grid(column=5,row=9)
entry7.grid(column=1,row=10)




scr2 = Scrollbar(win,orient='horizontal')
tt.configure(xscrollcommand = scr2.set)
scr2['command']=tt.xview
scr2.grid(row=11,column=7)

scr3 = Scrollbar(win)
tt.configure(yscrollcommand = scr3.set)
scr3['command']=tt.yview
scr3.grid(row=4,column=8)

tt.grid(row=1,column=7,rowspan=10)

win.mainloop()










