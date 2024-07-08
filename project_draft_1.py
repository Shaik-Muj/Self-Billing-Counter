from tkinter import *
from tkinter import messagebox
import random,tempfile,smtplib
from random import randint
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


total_cost_list=[]
total_tax_list=[]  
bill_dict={}

def main():
    global name_entry,phno_entry,email_entry
    bw=Tk()
    bw.geometry("1200x700")
    h1=Label(bw,text="-SELF BILLING COUNTER-",font=('algerian',35,'bold'),bg="black",fg="yellow")
    h1.pack(fill=X,pady=10)

    #CUSTOMER DETAILS ENTRY(H-2)
    h2cd=LabelFrame(bw,text='ENTER CUSTOMER DETAILS', font=('comic sans',12,'bold'),relief=GROOVE,background='grey20',fg='yellow',bd=18,pady=15)
    name=Label(h2cd,text='NAME',bg='black',fg='white', font=('comic sans',15,'bold'),relief=GROOVE)
    h2cd.pack(fill=X)
    name.grid(row=0, column=1,pady=10,padx=20)
    name_entry=Entry(h2cd, bd=3,font=('algerian',13), width=15)
    name_entry.grid(row=0, column=2,padx=20)
    phno=Label(h2cd, text='PHONE NUMBER',bg='black',fg='white',font=('comic sans',15,'bold'),relief=GROOVE)
    phno.grid(row=0, column=3,padx=20)
    phno_entry=Entry(h2cd, bd=3,font=('algerian',13), width=15)
    phno_entry.grid(row=0,column=4,padx=20)
    email_label=Label(h2cd,text="EMAIL",bg='black',fg='white',font=('comic sans',15,'bold'),relief=GROOVE)
    email_label.grid(row=0,column=5,padx=20)
    email_entry=Entry(h2cd,bd=3,font=('algerian',13), width=30)
    email_entry.grid(row=0,column=6,padx=20)

    #ITEM ENTRY DETAILS(H-3)
    h3id=LabelFrame(bw,text="ENTER ITEM DETAILS", font=('comic sans',12,'bold'),relief=GROOVE,background='grey20',fg='yellow',bd=18,pady=5)
    h3id.pack(fill=X,pady=10)
    option_dict={"TOMATO":30,"POTATO":35,"MILK":28}
    options=StringVar(h3id)
    options.set("SELECT")
    def show_item_cost(*args):  # on select function 
        for i,j in option_dict.items():
            if i==options.get():
                item_cost_label.configure(text=str(j)) 
    def show_tot(*args):  # on select function 
        for i,j in option_dict.items():
            if i==options.get():
                t=item_quantity_entry.get()
                c=int(t)*int(j)
                total_cost_disp_label.configure(text=f'{c} Rs')
                totx=int(j)*(6/100)*int(t)
                total_tax_disp_label.config(text="%0.3f Rs"%totx)
    def add_item(*args):

        for i,j in option_dict.items():
            if i==options.get():
                t=item_quantity_entry.get()
                tc=int(t)*int(j)
                tt=int(j)*(6/100)*int(t)
                total_cost_list.append(tc)
                total_tax_list.append(tt)
                bill_dict[i]={"quantity":int(t),"total cost":tc}
                options.set("SELECT")
                item_cost_label.config(text="      ")
                item_quantity_entry.config(text="      ")
                total_cost_disp_label.config(text="      ")
                total_tax_disp_label.config(text="      ")



    def disp_tot():
        amt_to_be_paid=sum(total_cost_list)+sum(total_tax_list)
        total_disp_label.config(text=f"{amt_to_be_paid} Rs")


    options.trace('w',show_item_cost)
    item_name_label=Label(h3id,text="SELECT YOUR ITEM",bg='black',fg='white',font=('comic sans',13,'bold'),relief=GROOVE)
    item_name_label.grid(row=0,column=1,padx=20)
    item_name=OptionMenu(h3id,options,*option_dict)
    item_name.config(font=('comic sans',10,'bold'),relief=GROOVE,width=12)
    item_name.grid(row=0,column=2,padx=20)
    item_cost=Label(h3id,text="COST PER PIECE/Kg",bg='black',fg='white',font=('comic sans',15,'bold'),relief=GROOVE,width=20)
    item_cost.grid(row=0,column=3,padx=12,pady=8)
    item_cost_label=Label(h3id, bd=3,font=('algerian',13), width=13)
    item_cost_label.grid(row=0,column=4,padx=20)
    item_quantity=Label(h3id,text='QUANTITY',bg='black',fg='white',font=('comic sans',15,'bold'),relief=GROOVE)
    item_quantity.grid(row=0,column=5,padx=15)
    item_quantity_entry=Spinbox(h3id, bd=3,from_=0,to=100, width=7,font=('comic sans',15,'bold'))
    item_quantity_entry.grid(row=0,column=6,padx=15)
    crs_ref_label=Label(h3id,text="TO VIEW TOTAL COST OF CURRENT ITEM\nPRESS 'OK'",bg='black',fg='white',font=('comic sans',9,'bold'),relief=GROOVE)
    crs_ref_label.grid(row=1,column=3)
    b1=Button(h3id,text="OK",bg='red',fg='black',font=('comic sans',15,'bold'),relief=GROOVE,command=show_tot,height=1)
    b1.grid(row=1,column=4,padx=10,pady=15)
    total_cost_label=Label(h3id,text="TOTAL COST",bg='black',fg='white',font=('comic sans',14,'bold'),relief=GROOVE,width=11)
    total_cost_label.grid(row=2,column=2,padx=10,pady=28)
    total_cost_disp_label=Label(h3id, bd=3,font=('algerian',13), width=17)
    total_cost_disp_label.grid(row=2,column=3,padx=10)
    total_tax_label=Label(h3id,text="TOTAL TAX",bg='black',fg='white',font=('comic sans',15,'bold'),relief=GROOVE,width=12)
    total_tax_disp_label=Label(h3id, bd=3,font=('algerian',13), width=10)
    total_tax_label.grid(row=2,column=4,padx=10)
    total_tax_disp_label.grid(row=2,column=5,padx=10)


    #ADD ITEM BUTTON
    additem=Button(h3id,text="ADD ITEM\nTO BILL",bg="RED",fg='black',font=('comic sans',10,'bold'),relief=GROOVE,width=12,command=add_item)
    additem.grid(row=3, column=3)
    finish_entry=Button(h3id,text="PROCEED TO\nBILLING",bg="red",fg='black',font=('comic sans',10,'bold'),relief=GROOVE,width=12,command=disp_tot)
    finish_entry.grid(row=3,column=4)

    #TOTAL-DISPLAY
    tot=LabelFrame(bw,text="BILLING OPTIONS",relief=GROOVE,background='grey20',fg='yellow',bd=18,pady=5,font=('comic sans',12,'bold'))
    tot.pack(fill=X,pady=5)
    total=Label(tot,text="TOTAL AMOUNT TO BE PAID(IN RUPEES)",bg='black',fg='white',font=('comic sans',15,'bold'),relief=GROOVE)
    total.pack(pady=5)
    total_disp_label=Label(tot,text="0 Rs",fg="black",font=('comic sans',15,'bold'),relief=GROOVE)
    total_disp_label.pack(pady=5)

    #BILLING OPTIONS FRAME
    bof=Frame(tot,bg="grey20")
    bof.pack(fill=X,pady=5)
    search=Button(bof,text="SEARCH BILL",bg="RED",fg='black',font=('comic sans',10,'bold'),relief=GROOVE,width=15,command=bill_search_win)
    generate_bill=Button(bof,text="GENERATE BILL\nAND DISPLAY",bg="RED",fg='black',font=('comic sans',10,'bold'),relief=GROOVE,width=15,command=bill_window)
    send_to_email=Button(bof,text="GENERATE BILL\nAND SEND TO EMAIL",bg="RED",fg='black',font=('comic sans',10,'bold'),relief=GROOVE,width=20,command=send_email)
    exit_=Button(bof,text="EXIT",bg="RED",fg='black',font=('comic sans',10,'bold'),relief=GROOVE,width=8,command=bw.destroy)
    search.grid(row=0,column=3,padx=80)
    generate_bill.grid(row=0,column=4,padx=80)
    send_to_email.grid(row=0,column=5,padx=80)
    exit_.grid(row=0,column=6,padx=80)

    bw.mainloop()

billnum=random.randint(1000,10000)

def bill_window():
    if name_entry.get()=="" or phno_entry.get()=="":
        messagebox.showerror("ERROR","FILL CUSTOMER DETAILS")
    elif sum(total_cost_list)==0:
        messagebox.showerror("INVALID BILLING","NO PRODECT PURCHASED")
    else:
        def save():
            res=messagebox.askyesno("CONFIRM","WOULD YOU LIKE TO SAVE THE FILE")
            if res:
                bill_cont=text.get(1.0,END)
                fp=open(f"bills/{billnum}.txt","w")
                fp.write(bill_cont)
                fp.close()
                messagebox.showinfo("SAVED",f"Bill with bill number {billnum} is saved")
        def print():
                file=tempfile.mktemp(".txt")
                open(file,"w").write(text.get(1.0,END))
                os.startfile(file,"print")
                messagebox.showinfo("SUCCESS",f"bill with bill number {billnum} has been printed")
        bill=Tk()
        bill.geometry("510x550")
        bill_frame=Frame(bill)
        bill_frame.pack()
        scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        bill_label=Label(bill_frame,text="BILL",font=("times new roman",8,"bold"),bd=8,relief=GROOVE)
        text=Text(bill_frame,height=30,width=60,yscrollcommand=scrollbar.set,bg="grey82")
        bill_label.pack(fill=X)
        text.pack()
        scrollbar.config(command=text.yview)
        text.insert(END,'\t\t      X-MART WELCOMES YOU\n\n')
        text.insert(END,f"   Bill number: {billnum}\n")
        text.insert(END,f"   Customer name: {name_entry.get()}\n")
        text.insert(END,f"   Phone Number: {phno_entry.get()}\n")
        text.insert(END,'============================================================\n')
        text.insert(END,'ITEM NAME\t\t\tQUANTITY\t\t\tTOTAL COST\n')
        text.insert(END,'============================================================\n')
        for i in bill_dict.keys():
            item_name=i
            Quntity=bill_dict[i]["quantity"]
            Tot_cst=bill_dict[i]["total cost"]
            text.insert(END,f"   {item_name}\t\t\t{Quntity}\t\t\t{Tot_cst} Rs\n")
        text.insert(END,'============================================================\n\n')
        text.insert(END,f'TOTAL COST OF ITEMS\t\t\t\t\t\t{sum(total_cost_list)} Rs\n')
        text.insert(END,'TOTAL TAX OF ITEMS\t\t\t\t\t\t%0.2f Rs\n\n'%(sum(total_tax_list)))
        text.insert(END,'*******----------------------------------------------*******\n\n')
        text.insert(END,f"TOTAL COST OF PRODUCTS\t\t\t\t\t\t{sum(total_cost_list)+sum(total_tax_list)} Rs\n\n")
        text.insert(END,'\t\t    THANK YOU FOR USING\n\t\t       OUR SERVICES')
        btn=Frame(bill,bg="grey82")
        btn.pack(fill=X)
        b1=Button(btn,text="SAVE",font=("times new roman",12,"bold"),bg="blue",fg="white",command=save)
        b1.grid(row=0,column=1,padx=110)
        b2=Button(btn,text="PRINT",font=("times new roman",12,"bold"),bg="blue",fg="white",command=print)
        b2.grid(row=0,column=2,padx=40)
        mainloop()


def bill_search_win():
    def search():
        for i in os.listdir('bills/'):
            if i.split(".")[0]==bill_srch_entry.get():
                f=open(f'bills/{i}',"r")
                for data in f:
                    text2.insert(END,data)
                f.close()
                break
        else:
            messagebox.showerror("ERROR","INVALID BILL NUMBER")
    bill_srch=Tk()
    bill_srch.geometry("510x550")
    bill_srch_frame=Frame(bill_srch,bg="grey20")
    bill_srch_frame.pack(fill=X)
    scrollbar=Scrollbar(bill_srch,orient=VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    bill_srch_label=Label(bill_srch_frame,text="ENTER THE BILL NO.",font=("times new roman",10,"bold"),bd=8,relief=GROOVE,bg="sky blue")
    bill_srch_entry=Entry(bill_srch_frame,font=("times new roman",10,"bold"),bd=8,relief=GROOVE)
    bill_srch_btn=Button(bill_srch_frame,text="search",font=("times new roman",10,"bold"),bd=8,relief=GROOVE,bg="sky blue",command=search)
    text2=Text(bill_srch,height=30,width=60,yscrollcommand=scrollbar.set,bg="grey82")
    bill_srch_label.grid(row=0,column=1,padx=30)
    bill_srch_entry.grid(row=0,column=2,padx=20)
    bill_srch_btn.grid(row=0,column=3,padx=20)
    text2.pack()

    bill_srch.mainloop()

def send_email():
    if name_entry.get()=="" or phno_entry.get()=="":
        messagebox.showerror("ERROR","FILL CUSTOMER DETAILS")
    elif sum(total_cost_list)==0:
        messagebox.showerror("INVALID BILLING","NO PRODECT PURCHASED")
    else:

        def save():
            res=messagebox.askyesno("CONFIRM","WOULD YOU LIKE TO SAVE THE FILE")
            if res:
                bill_cont=text.get(1.0,END)
                fp=open(f"bills/{billnum}.txt","w")
                fp.write(bill_cont)
                fp.close()
                messagebox.showinfo("SAVED",f"Bill with bill number {billnum} is saved")
        def send():
            try:
                ob=smtplib.SMTP("smtp.gmail.com",587)
                ob.starttls()
                ob.login("sandyarun154@gmail.com","oomtgnnbgwrnarfw")
                message=text.get(1.0,END)
                x=(email_entry.get()).lower()
                ob.sendmail("sandyarun154@gmail.com",x,message)
                ob.quit()
                messagebox.showinfo("Success","Email sent successfully")
            except:
                messagebox.showerror("ERROR","CANNOT SEND EMAIL")

        bill=Toplevel()
        bill.geometry("510x550")
        bill_frame=Frame(bill)
        bill_frame.pack()
        scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        bill_label=Label(bill_frame,text="BILL",font=("times new roman",8,"bold"),bd=8,relief=GROOVE)
        text=Text(bill_frame,height=30,width=60,yscrollcommand=scrollbar.set,bg="grey82")
        bill_label.pack(fill=X)
        text.pack()
        scrollbar.config(command=text.yview)
        text.insert(END,'\t\t      X-MART WELCOMES YOU\n\n')
        text.insert(END,f"   Bill number: {billnum}\n")
        text.insert(END,f"   Customer name: {name_entry.get()}\n")
        text.insert(END,f"   Phone Number: {phno_entry.get()}\n")
        text.insert(END,'============================================================\n')
        text.insert(END,'ITEM NAME\t\t\tQUANTITY\t\t\tTOTAL COST\n')
        text.insert(END,'============================================================\n')
        for i in bill_dict.keys():
            item_name=i
            Quntity=bill_dict[i]["quantity"]
            Tot_cst=bill_dict[i]["total cost"]
            text.insert(END,f"   {item_name}\t\t\t{Quntity}\t\t\t{Tot_cst} Rs\n")
        text.insert(END,'============================================================\n\n')
        text.insert(END,f'TOTAL COST OF ITEMS\t\t\t\t\t\t{sum(total_cost_list)} Rs\n')
        text.insert(END,'TOTAL TAX OF ITEMS\t\t\t\t\t\t%0.2f Rs\n\n'%(sum(total_tax_list)))
        text.insert(END,'*******----------------------------------------------*******\n\n')
        text.insert(END,f"TOTAL COST OF PRODUCTS\t\t\t\t\t\t{sum(total_cost_list)+sum(total_tax_list)} Rs\n\n")
        text.insert(END,'\t\t    THANK YOU FOR USING\n\t\t       OUR SERVICES')
        btn=Frame(bill,bg="grey82")
        btn.pack(fill=X)
        b1=Button(btn,text="SAVE",font=("times new roman",12,"bold"),bg="blue",fg="white",command=save)
        b1.grid(row=0,column=1,padx=110)
        b2=Button(btn,text="SEND TO EMAIL",font=("times new roman",12,"bold"),bg="blue",fg="white",command=send)
        b2.grid(row=0,column=2,padx=40)
        mainloop()
        



def wel_win():
    root=Tk()
    root.geometry("770x300")
    root.title("WELCOME")
    root.configure(bg='sky blue')
    l1=Label(root,text="WELCOME TO X-MART",font=("copperplate gothic bold",40,"bold"),bg='sky blue',fg='black',pady=20)
    l1.pack()
    l2=Label(root,text="WOULD YOU LIKE TO START BILLING?",font=("copperplate gothic bold",20,"bold"),bg='sky blue',fg='black',pady=20)
    l2.pack()
    l3=Label(root,text="TO START BILLING PRESS PROCEED",font=("copperplate gothic bold",20,"bold"),bg='sky blue',fg='black',pady=20)
    l3.pack()
    b1=Button(root,text="PROCEED",font=("comic sans",10,"bold"),command=main)
    b1.pack()
    mainloop()

wel_win()