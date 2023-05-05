from tkinter import*
root=Tk()
root.title("Form create")
root.geometry("644x333")
def getvals():
    print("submitting form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")

    with open("record.txt","a")as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}" "\n")
Label(root,text="Welcome to Travelling Form",font="comicsansms 13 underline",pady=10,padx=19,height="1",fg="red").grid(row=0,column=3,ipadx=10,ipady=10,sticky="EW")

name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmode=Label(root,text="Payment Mode")

name.grid(row=1,column=2,)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)


nameentry.grid(row=1,column=3,pady="3")
phoneentry.grid(row=2,column=3,pady="3")
genderentry.grid(row=3,column=3,pady="3")
emergencyentry.grid(row=4,column=3,pady="3")
paymentmodeentry.grid(row=5,column=3,pady="3")

foodservice=Checkbutton(text="want to prebook your meals?",variable=foodservicevalue)
foodservice.grid(row=6,column=3,pady="5")

Button(text="Submit to travellers",command=getvals).grid(row=7,column=3,pady="5")
root.mainloop()