from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random, os
from tkinter import messagebox
import tempfile
from time import strftime


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x770+0+0")
        self.root.title("Billing Software")
        #variables
        self.custName=StringVar()
        self.custPhone=StringVar()
        self.billno=StringVar()
        z=random.randint(1000,9999)
        self.billno.set(z)
        self.custEmail=StringVar()
        self.searchBill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.subtotal=StringVar()
        self.taxInput=StringVar()
        self.total=StringVar()


        #product categories list
        self.category=["Select Option","Clothing","Lifestyle","Mobiles"]
        #SubCatclothing
        self.subcatClothing=["Pant","T-Shirt","Shirt"]
        #PANT
        self.pant=["Levis","LeeCooper","Denim","AllenSolly"]
        self.price_Levis=4000
        self.price_LeeCooper=3500
        self.price_Denim=2500
        self.price_AllenSolly=3000
        #T-shirt
        self.tshirt=["Polo","Netplay","Armani","Puma","Nike"]
        self.price_Polo=2000
        self.price_Netplay=1500
        self.price_Armani=4000
        self.price_Puma=2500
        self.price_Nike=3000
        #SHIRT
        self.shirt=["Gucci","Zara","Wrangler","GAP","Adidas","Crocodile"]
        self.price_Gucci=15000
        self.price_Zara=8000
        self.price_Wrangler=4000
        self.price_GAP=3000
        self.price_Adidas=3000
        self.price_Crocodile=2500
        #SubCatLifestyle
        self.subcatLifestyle=["Bath Soap","Face Cream","Shampoo","Perfume"]
        #bath soap
        self.Bath_Soap=["Dettol","Dove","LUX","MamaEarth"]
        self.price_Dettol=20
        self.price_Dove=35
        self.price_LUX=30
        self.price_MamaEarth=40
        #face cream
        self.facecream=["FairEver","Vaseline","Lakme","CeraVe","Johnson Baby"]
        self.price_FairEver=40
        self.price_Vaseline=80
        self.price_Lakme=60
        self.price_CeraVe=90
        self.price_JohnsonBaby=70
        #SHampoo
        self.shampoo=["Head&Shoulders","Tresemme","Loreal","Wella"]
        self.price_HeadShoulders=120
        self.price_Tresemme=250
        self.price_Loreal=300
        self.price_Wella=550
        #Perfume
        self.perfume=["ParkAvenue","Fogg","Dior","Axe"]
        self.price_ParkAvenue=300
        self.price_Fogg=250
        self.price_Dior=900
        self.price_Axe=200
        #SUbCAtMobiles
        
        self.subcatMobiles=["Apple","Samsung","OnePlus","Redmi"]
        #Apple
        self.apple=["IPhone13","IPhone14","IPhone14Pro","Iphone14ProMax"]
        self.price_IPhone13=55000
        self.price_IPhone14=65000
        self.price_Iphone14Pro=90000
        self.price_IPhone14ProMax=110000
        #Samsung
        self.samsung=["S20","S20Ultra","Note20","Note21","A50","A51"]
        self.price_S20=70000
        self.price_S20Ultra=80000
        self.price_Note20=75000
        self.price_Note21=90000
        self.price_A50=25000
        self.price_A51=30000
        #oneplus
        self.oneplus=["Nord","Nord2","Nord2T","9pro","9plus"]
        self.price_Nord=20000
        self.price_Nord2=25000
        self.price_Nord2T=30000
        self.price_9pro=50000
        self.price_9plus=40000
        #redmi
        self.redmi=["Note7","Note7plus","K20","K30"]
        self.price_Note7=18000
        self.price_Note7plus=20000
        self.price_K20=22000
        self.price_K30=26000
    
        


        img=Image.open("images/xmart.jpg")
        img=img.resize((1280,90))
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_image=Label(self.root,image=self.photoimg)
        lbl_image.place(x=0,y=0,width=1280,height=130)
        #TITLE

        lbl_title=Label(self.root,text="X-MART SELF BILLING COUNTER",font=("arial black",30,"bold"),bg='brown2',fg='black')
        lbl_title.place(x=0,y=110,width=1400,height=40)
        #time
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(lbl_title,font=('times new roman',16,'bold'),bg='brown2',fg='black')
        lbl.place(x=0,y=0,width=120,height=45)
        time()
        #mainframe

        Main_frame=Frame(self.root,bd=10,relief=RIDGE,bg='bisque')
        Main_frame.place(x=0,y=150,width=1280,height=620)
        #customer label frame

        customer_frame=LabelFrame(Main_frame,text="Customer Details",font=("georgia",12,"bold"),bg="bisque",fg="red")
        customer_frame.place(x=10,y=5,width=350,height=160)

        self.lbl_mobno=Label(customer_frame,text="Mobile No.",font=("georgia",12,"bold"),bg="bisque")
        self.lbl_mobno.grid(row=0,column=0,sticky=W,padx=5)

        self.entry_mobno=ttk.Entry(customer_frame,textvariable=self.custPhone,font=("arial black",12,"bold"),width=20)
        self.entry_mobno.grid(row=0,column=1,pady=5)

        self.lbl_name=Label(customer_frame,text="Name",font=("georgia",12,"bold"),bg="bisque")
        self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=10)

        self.entry_name=ttk.Entry(customer_frame,textvariable=self.custName,font=("arial black",12,"bold"),width=20)
        self.entry_name.grid(row=1,column=1,pady=10)

        self.lbl_email=Label(customer_frame,text="Email",font=("georgia",12,"bold"),bg="bisque")
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=10)

        self.entry_email=ttk.Entry(customer_frame,textvariable=self.custEmail,font=("arial black",12,"bold"),width=20)
        self.entry_email.grid(row=2,column=1,pady=10)

        #PRODUCT FRAME

        product_frame=LabelFrame(Main_frame,text="Product",font=("georgia",12,"bold"),bg="bisque",fg="red")
        product_frame.place(x=370,y=5,width=470,height=160)

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

        self.entrybillNO=ttk.Entry(searchframe,textvariable=self.searchBill,font=("arial black",12,"bold"),width=15)
        self.entrybillNO.grid(row=0,column=1,pady=0)

        self.searchbutton=Button(searchframe,command=self.find_bill,text="Search",font=("arial black",9,"bold"),bd=4,relief=RIDGE,cursor="hand2",bg="firebrick1",fg="black",width=10)
        self.searchbutton.grid(row=0,column=2,padx=10)

        
        


        

        #combo boxes
        #category box

        self.combocat=ttk.Combobox(product_frame,value=self.category,state="readonly",font=('arial',10,'bold'),width=10)
        self.combocat.current(0)
        self.combocat.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combocat.bind("<<ComboboxSelected>>",self.Categories)

        #sub category box

        self.combosub=ttk.Combobox(product_frame,value=[''],state="readonly",font=('arial',10,'bold'),width=10)
        self.combosub.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combosub.bind("<<ComboboxSelected>>",self.product_add)
        #Product name

        self.comboproduct=ttk.Combobox(product_frame,textvariable=self.product,state="readonly",font=('arial',10,'bold'),width=10)
        self.comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.comboproduct.bind("<<ComboboxSelected>>",self.price)
        #price

        self.comboprice=ttk.Combobox(product_frame,textvariable=self.prices,state="readonly",font=('arial',10,'bold'),width=10)
        self.comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        #qty

        self.comboqty=ttk.Entry(product_frame,textvariable=self.qty,font=('arial',10,'bold'),width=10)
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
        rightlabelframe.place(x=850,y=40,width=410,height=430)

        #scroll bar
        scroll_y=Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea=Text(rightlabelframe,yscrollcommand=scroll_y.set,bg="white",fg="red",font=("georgia",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #bill counter

        bottom_frame=LabelFrame(Main_frame,text="Options",font=("georgia",12,"bold"),bg="bisque",fg="red")
        bottom_frame.place(x=10,y=312,width=840,height=160)

        

        #BUTTON FRAME
        buttonframe=Frame(bottom_frame,bd=2,bg="white")
        buttonframe.place(x=10,y=30)

        self.buttonaddtoCart=Button(buttonframe,command=self.additem,text="Add to Cart",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=14,height=4,cursor="hand2")
        self.buttonaddtoCart.grid(row=0,column=0)

        self.buttongenBill=Button(buttonframe,command=self.gen_bill,text="Generate Bill",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=14,height=4,cursor="hand2")
        self.buttongenBill.grid(row=0,column=1)

        self.buttonSavebill=Button(buttonframe,command=self.save_bill,text="Save Bill",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=14,height=4,cursor="hand2")
        self.buttonSavebill.grid(row=0,column=2)

        self.buttonPrint=Button(buttonframe,command=self.iprint,text="Print Bill",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=14,height=4,cursor="hand2")
        self.buttonPrint.grid(row=0,column=3)

        self.buttonClear=Button(buttonframe,command=self.clear,text="Clear",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=14,height=4,cursor="hand2")
        self.buttonClear.grid(row=0,column=4)

        self.buttonExit=Button(buttonframe,command=self.root.destroy,text="Exit",font=("arial black",9,"bold"),bd=4,relief=RIDGE,bg="firebrick1",fg="black",width=14,height=4,cursor="hand2")
        self.buttonExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]

    ###############################FUNCTION DECLARATION#######################################
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome to X-Mart")
        self.textarea.insert(END,f"\n BILL NUMBER:{self.billno.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.custName.get()}")
        self.textarea.insert(END,f"\n Phone No.:{self.custPhone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.custEmail.get()}")

        self.textarea.insert(END,"\n======================================================================")
        self.textarea.insert(END,f"\nProducts\t\tQuantity\t\tPrice")
        self.textarea.insert(END,"\n======================================================================\n")

    def additem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the product first")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.subtotal.set(str("Rs.%.2f"%(sum(self.l))))
            self.taxInput.set(str("Rs.%.2f"%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
    

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please add products to the cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n======================================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.subtotal.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.taxInput.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n======================================================================")
    

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bills/"+str(self.billno.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.billno.get()} Saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'print')

    def find_bill(self):
        found='no'
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.searchBill.get():
                f1=open(f"bills/{i}",'r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.custName.set("")
        self.custEmail.set("")
        self.custPhone.set("")
        x=random.randint(1000,9999)
        self.billno.set(str(x))
        self.searchBill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.subtotal.set("")
        self.taxInput.set("")
        self.welcome()

    










            





    

    







    
    def Categories(self,arg=""):
        if self.combocat.get()=="Clothing":
            self.combosub.config(value=self.subcatClothing)
            self.combosub.current(0)

        if self.combocat.get()=="Lifestyle":
            self.combosub.config(value=self.subcatLifestyle)
            self.combosub.current(0)
        
        if self.combocat.get()=="Mobiles":
            self.combosub.config(value=self.subcatMobiles)
            self.combosub.current(0)
    
    def product_add(self,arg=""):
        if self.combosub.get()=="Pant":
            self.comboproduct.config(value=self.pant)
            self.comboproduct.current(0)
        
        if self.combosub.get()=="T-Shirt":
            self.comboproduct.config(value=self.tshirt)
            self.comboproduct.current(0)

        if self.combosub.get()=="Shirt":
            self.comboproduct.config(value=self.shirt)
            self.comboproduct.current(0)

        #life style
        if self.combosub.get()=="Bath Soap":
            self.comboproduct.config(value=self.Bath_Soap)
            self.comboproduct.current(0)
        if self.combosub.get()=="Face Cream":
            self.comboproduct.config(value=self.facecream)
            self.comboproduct.current(0)
        if self.combosub.get()=="Shampoo":
            self.comboproduct.config(value=self.shampoo)
            self.comboproduct.current(0)
        if self.combosub.get()=="Perfume":
            self.comboproduct.config(value=self.perfume)
            self.comboproduct.current(0)
        #Mobiles
        if self.combosub.get()=="Apple":
            self.comboproduct.config(value=self.apple)
            self.comboproduct.current(0)
        if self.combosub.get()=="Samsung":
            self.comboproduct.config(value=self.samsung)
            self.comboproduct.current(0)
        if self.combosub.get()=="OnePlus":
            self.comboproduct.config(value=self.oneplus)
            self.comboproduct.current(0)
        if self.combosub.get()=="Redmi":
            self.comboproduct.config(value=self.redmi)
            self.comboproduct.current(0)
    
    def price(self,arg=""):
        #clothing
        #pant
        if self.comboproduct.get()=="Levis":
            self.comboprice.config(value=self.price_Levis)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="LeeCooper":
            self.comboprice.config(value=self.price_LeeCooper)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Denim":
            self.comboprice.config(value=self.price_Denim)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="AllenSolly":
            self.comboprice.config(value=self.price_AllenSolly)
            self.comboprice.current(0)
            self.qty.set(1)
        #t-shirt
        if self.comboproduct.get()=="Polo":
            self.comboprice.config(value=self.price_Polo)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Netplay":
            self.comboprice.config(value=self.price_Netplay)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Armani":
            self.comboprice.config(value=self.price_Armani)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Puma":
            self.comboprice.config(value=self.price_Puma)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Nike":
            self.comboprice.config(value=self.price_Nike)
            self.comboprice.current(0)
            self.qty.set(1)
        #shirt
        if self.comboproduct.get()=="Gucci":
            self.comboprice.config(value=self.price_Gucci)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Zara":
            self.comboprice.config(value=self.price_Zara)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Wrangler":
            self.comboprice.config(value=self.price_Wrangler)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="GAP":
            self.comboprice.config(value=self.price_GAP)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Adidas":
            self.comboprice.config(value=self.price_Adidas)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Crocodile":
            self.comboprice.config(value=self.price_Crocodile)
            self.comboprice.current(0)
            self.qty.set(1)
        #lifestyle
        #bath soap
        if self.comboproduct.get()=="Dettol":
            self.comboprice.config(value=self.price_Dettol)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Dove":
            self.comboprice.config(value=self.price_Dove)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="LUX":
            self.comboprice.config(value=self.price_LUX)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="MamaEarth":
            self.comboprice.config(value=self.price_MamaEarth)
            self.comboprice.current(0)
            self.qty.set(1)
        #face cream
        if self.comboproduct.get()=="FairEver":
            self.comboprice.config(value=self.price_FairEver)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Vaseline":
            self.comboprice.config(value=self.price_Vaseline)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Lakme":
            self.comboprice.config(value=self.price_Lakme)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="CeraVe":
            self.comboprice.config(value=self.price_CeraVe)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Johnson Baby":
            self.comboprice.config(value=self.price_JohnsonBaby)
            self.comboprice.current(0)
            self.qty.set(1)
        #Shampoo
        if self.comboproduct.get()=="Head&Shoulders":
            self.comboprice.config(value=self.price_HeadShoulders)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Tresemme":
            self.comboprice.config(value=self.price_Tresemme)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Loreal":
            self.comboprice.config(value=self.price_Loreal)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Wella":
            self.comboprice.config(value=self.price_Wella)
            self.comboprice.current(0)
            self.qty.set(1)
        #perfumes
        if self.comboproduct.get()=="ParkAvenue":
            self.comboprice.config(value=self.price_ParkAvenue)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Fogg":
            self.comboprice.config(value=self.price_Fogg)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Dior":
            self.comboprice.config(value=self.price_Dior)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Axe":
            self.comboprice.config(value=self.price_Axe)
            self.comboprice.current(0)
            self.qty.set(1)
        #mobiles
        #apple
        if self.comboproduct.get()=="IPhone13":
            self.comboprice.config(value=self.price_IPhone13)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="IPhone14":
            self.comboprice.config(value=self.price_IPhone14)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="IPhone14Pro":
            self.comboprice.config(value=self.price_Iphone14Pro)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Iphone14ProMax":
            self.comboprice.config(value=self.price_IPhone14ProMax)
            self.comboprice.current(0)
            self.qty.set(1)
        #samsung
        if self.comboproduct.get()=="S20":
            self.comboprice.config(value=self.price_S20)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="S20Ultra":
            self.comboprice.config(value=self.price_S20Ultra)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Note20":
            self.comboprice.config(value=self.price_Note20)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Note21":
            self.comboprice.config(value=self.price_Note21)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="A50":
            self.comboprice.config(value=self.price_A50)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="A51":
            self.comboprice.config(value=self.price_A51)
            self.comboprice.current(0)
            self.qty.set(1)
        #oneplus
        if self.comboproduct.get()=="Nord":
            self.comboprice.config(value=self.price_Nord)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Nord2":
            self.comboprice.config(value=self.price_Nord2)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Nord2T":
            self.comboprice.config(value=self.price_Nord2T)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="9pro":
            self.comboprice.config(value=self.price_9pro)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="9plus":
            self.comboprice.config(value=self.price_9plus)
            self.comboprice.current(0)
            self.qty.set(1)
        #redmi
        if self.comboproduct.get()=="Note7":
            self.comboprice.config(value=self.price_Note7)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="Note7plus":
            self.comboprice.config(value=self.price_Note7plus)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="K20":
            self.comboprice.config(value=self.price_K20)
            self.comboprice.current(0)
            self.qty.set(1)
        if self.comboproduct.get()=="K30":
            self.comboprice.config(value=self.price_K30)
            self.comboprice.current(0)
            self.qty.set(1)

if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
