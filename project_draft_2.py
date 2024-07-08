from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk



class Bill_App():
    def _init_(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        img=Image.open("images/xmart.jpg")
        img=img.resize((1280,90))
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_image=Label(self.root,image=self.photoimg)
        lbl_image.place(x=0,y=0,width=1280,height=130)
        #TITLE

        lbl_title=Label(self.root,text="X-MART SELF BILLING COUNTER",font=("arial black",30,"bold"),bg='brown2',fg='black')
        lbl_title.place(x=0,y=110,width=1400,height=40)
        #mainframe

        Main_frame=Frame(self.root,bd=10,relief=RIDGE,bg='bisque')
        Main_frame.place(x=0,y=150,width=1280,height=620)

        customer_frame=LabelFrame(Main_frame,text="Customer Details",font=("georgia",12,"bold"),bg="bisque",fg="red")
        customer_frame.place(x=10,y=5,width=350,height=160)

        self.lbl_mobno=Label(customer_frame,text="Mobile No.",font=("georgia",12,"bold"),bg="bisque")
        self.lbl_mobno.grid(row=0,column=0,sticky=W,padx=5)

        self.entry_mobno=ttk.Entry(customer_frame,font=("arial black",12,"bold"),width=20)
        self.entry_mobno.grid(row=0,column=1,pady=5)

        self.lbl_name=Label(customer_frame,text="Name",font=("georgia",12,"bold"),bg="bisque")
        self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=10)

        self.entry_name=ttk.Entry(customer_frame,font=("arial black",12,"bold"),width=20)
        self.entry_name.grid(row=1,column=1,pady=10)

        self.lbl_email=Label(customer_frame,text="Email",font=("georgia",12,"bold"),bg="bisque")
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=10)

        self.entry_email=ttk.Entry(customer_frame,font=("arial black",12,"bold"),width=20)
        self.entry_email.grid(row=2,column=1,pady=10)

        #PRODUCT FRAME

        product_frame=LabelFrame(Main_frame,text="Product",font=("georgia",12,"bold"),bg="bisque",fg="red")
        product_frame.place(x=390,y=5,width=470,height=160)

        self.lbl_category=Label(product_frame,text="Select Categories",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lbl_category.grid(row=0,column=0,sticky=W,padx=5,pady=10)

        self.lbl_subcategory=Label(product_frame,text="Sub-Categories",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lbl_subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=10)

        self.lbl_productname=Label(product_frame,text="Product Name",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lbl_productname.grid(row=2,column=0,sticky=W,padx=5,pady=10)

        self.lbl_price=Label(product_frame,text="Price",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lbl_price.grid(row=0,column=2,sticky=W,padx=5,pady=10)

        self.lbl_qty=Label(product_frame,text="Quantity",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lbl_qty.grid(row=1,column=2,sticky=W,padx=5,pady=10)
        #search bill
        searchframe=Frame(Main_frame,bd=2,bg="bisque")
        searchframe.place(x=890,y=10,width=500,height=30)

        self.lblsearchbill=Label(searchframe,text="Bill No.",font=("georgia",12,"bold"),bg="bisque",fg="red",bd=4)
        self.lblsearchbill.grid(row=0,column=0,sticky=W)

        self.entrybillNO=ttk.Entry(searchframe,font=("arial black",12,"bold"),width=15)
        self.entrybillNO.grid(row=0,column=1,pady=0)

        self.searchbutton=Button(searchframe,text="Search",font=("arial black",9,"bold"),bd=4,relief=RIDGE,cursor="hand2",bg="firebrick1",fg="black",width=10)
        self.searchbutton.grid(row=0,column=2,padx=10)

        

        #combo boxes

        self.combocat=ttk.Combobox(product_frame,state="readonly",font=('arial',10,'bold'),width=10)
        self.combocat.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.combosub=ttk.Combobox(product_frame,state="readonly",font=('arial',10,'bold'),width=10)
        self.combosub.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.comboproduct=ttk.Combobox(product_frame,state="readonly",font=('arial',10,'bold'),width=10)
        self.comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        self.comboprice=ttk.Combobox(product_frame,state="readonly",font=('arial',10,'bold'),width=10)
        self.comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        self.comboqty=ttk.Combobox(product_frame,state="readonly",font=('arial',10,'bold'),width=10)
        self.comboqty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #middle frame pics

        Middleframe=Frame(Main_frame,bd=10,bg='bisque')
        Middleframe.place(x=10,y=170,width=880,height=140)

        img12=Image.open("images/phonepe logo.png")
        img12=img12.resize((150,110))
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(Middleframe,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=150,height=110)

        img13=Image.open("images/Google-Pay-Logo-01.png")
        img13=img13.resize((150,110))
        self.photoimg13=ImageTk.PhotoImage(img13)

        lbl_img13=Label(Middleframe,image=self.photoimg13)
        lbl_img13.place(x=170,y=0,width=150,height=110)

        img14=Image.open("images/cash-01.jpg")
        img14=img14.resize((150,110))
        self.photoimg14=ImageTk.PhotoImage(img14)

        lbl_img14=Label(Middleframe,image=self.photoimg14)
        lbl_img14.place(x=330,y=0,width=150,height=110)

        img15=Image.open("images/OIF.jpg")
        img15=img15.resize((150,110))
        self.photoimg15=ImageTk.PhotoImage(img15)

        lbl_img15=Label(Middleframe,image=self.photoimg15)
        lbl_img15.place(x=500,y=0,width=150,height=110)

        img16=Image.open("images/bank-transfer.jpg")
        img16=img16.resize((150,110))
        self.photoimg16=ImageTk.PhotoImage(img16)

        lbl_img16=Label(Middleframe,image=self.photoimg16)
        lbl_img16.place(x=660,y=0,width=150,height=110)



        #billing area

        rightlabelframe=LabelFrame(Main_frame,text="Bill Area",font=("georgia",12,"bold"),bg="bisque",fg="red")
        rightlabelframe.place(x=890,y=40,width=350,height=273)

        #scroll bar
        scroll_y=Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea=Text(rightlabelframe,yscrollcommand=scroll_y.set,bg="white",fg="red",font=("georgia",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #bill counter

        bottom_frame=LabelFrame(Main_frame,text="Bill Counter",font=("georgia",12,"bold"),bg="bisque",fg="red")
        bottom_frame.place(x=10,y=312,width=1250,height=160)

        self.lblsubtotal=Label(bottom_frame,text="Sub-Total",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=10)

        self.entrysubtotal=ttk.Entry(bottom_frame,font=("arial black",12,"bold"),width=20)
        self.entrysubtotal.grid(row=0,column=1,pady=5)

        self.lbltax=Label(bottom_frame,text="Gov.Tax",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=10)

        self.entrytax=ttk.Entry(bottom_frame,font=("arial black",12,"bold"),width=20)
        self.entrytax.grid(row=1,column=1,pady=5)

        self.lbltotal=Label(bottom_frame,text="Total",font=("georgia",12,"bold"),bg="bisque",bd=4)
        self.lbltotal.grid(row=2,column=0,sticky=W,padx=5,pady=10)

        self.entrytotal=ttk.Entry(bottom_frame,font=("arial black",12,"bold"),width=20)
        self.entrytotal.grid(row=2,column=1,pady=5)

        #BUTTON FRAME
        buttonframe=Frame(bottom_frame,bd=2,bg="white")
        buttonframe.place(x=340,y=30)

        self.buttonaddtoCart=Button(buttonframe,text="Add to Cart",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=20,height=4,cursor="hand2")
        self.buttonaddtoCart.grid(row=0,column=0)

        self.buttongenBill=Button(buttonframe,text="Generate Bill",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=18,height=4,cursor="hand2")
        self.buttongenBill.grid(row=0,column=1)

        self.buttonSavebill=Button(buttonframe,text="Save Bill",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=18,height=4,cursor="hand2")
        self.buttonSavebill.grid(row=0,column=2)

        self.buttonPrint=Button(buttonframe,text="Print Bill",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=15,height=4,cursor="hand2")
        self.buttonPrint.grid(row=0,column=3)

        self.buttonClear=Button(buttonframe,text="Clear",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=15,height=4,cursor="hand2")
        self.buttonClear.grid(row=0,column=4)

        self.buttonExit=Button(buttonframe,text="Exit",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=15,height=4,cursor="hand2")
        self.buttonExit.grid(row=0,column=5)




if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()