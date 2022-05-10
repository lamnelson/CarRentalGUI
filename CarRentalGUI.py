import tkinter
from tkinter import *
from datetime import date

import sqlite3

root = Tk()

root.title('Address Book')
root.geometry("372x250")

address_book_connect = sqlite3.connect('CarRental.db')
address_book_cur = address_book_connect.cursor()

mainFrame = tkinter.Frame(root)
custFrame = tkinter.Frame(root)
vehicleFrame = tkinter.Frame(root)
rentalFrame = tkinter.Frame(root)
returnFrame = tkinter.Frame(root)

mainFrame.grid()

def custClick():
    custFrame.grid()
    mainFrame.grid_forget()
def vehicleClick():
    vehicleFrame.grid()
    mainFrame.grid_forget()
def returnClick():
    returnFrame.grid()
    mainFrame.grid_forget()
def rentalClick():
    rentalFrame.grid()
    mainFrame.grid_forget()
def returnMain():
    mainFrame.grid()
    custFrame.grid_forget()
    vehicleFrame.grid_forget()
    rentalFrame.grid_forget()
    returnFrame.grid_forget()
def submitCust():
    submit_conn = sqlite3.connect('CarRental.db')
    submit_cur = submit_conn.cursor()
    submit_cur.execute("INSERT INTO CUSTOMER (CustID, Name, Phone) VALUES (:CustID, :Name, :Phone)",
                       {'CustID': CustID.get(),
                        'Name': Name.get(),
                        'Phone': Phone.get()
                        })
    submit_conn.commit()
    # display results
    submit_cur.execute("SELECT * FROM CUSTOMER")
    result_set = submit_cur.fetchall()
    print("\n\nResult:\n")
    print("\tVehicleID\t\t\tDescription\tYear\tType\tCategory")
    i = 1
    for row in result_set:
        print("{}: {}\t{}\t{}\t{}\t{}".format(i, row[0], row[1], row[2], row[3], row[4]))
        i = i + 1
    i = i - 1
    print("The total rows returned: {}".format(i))
    submit_conn.close()
def submitVehicle():
    submit_conn = sqlite3.connect('CarRental.db')
    submit_cur = submit_conn.cursor()
    submit_cur.execute("INSERT INTO VEHICLE (VehicleID, Description, Year, Type, Category) VALUES (:VehicleID, :Description, :Year, :Type, :Category)",
                       {
                        'VehicleID': VehicleID.get(),
                        'Description': Description.get(),
                        'Year': Year.get(),
                        'Type': Type.get(),
                        'Category': Category.get()
                        })
    submit_conn.commit()
    # display results
    submit_cur.execute("SELECT * FROM VEHICLE")
    result_set = submit_cur.fetchall()
    print("\n\nResult:\n")
    print("\tVehicleID\t\t\tDescription\tYear\tType\tCategory")
    i = 1
    for row in result_set:
        print("{}: {}\t{}\t{}\t{}\t{}".format(i, row[0], row[1], row[2], row[3], row[4]))
        i = i + 1
    i = i - 1
    print("The total rows returned: {}".format(i))
    submit_conn.close()
def submitRental():
    submit_conn = sqlite3.connect('CarRental.db')
    submit_cur = submit_conn.cursor()
    submit_cur.execute(
        "INSERT INTO RENTAL (CustID, VehicleID, RentalType, StartDate, OrderDate) VALUES (:CustID, :VehicleID, :RentalType, :StartDate, :OrderDate)",
        {
            'CustID': CustID.get(),
            'VehicleID': VehicleID.get(),
            'RentalType' : RentalType.get(),
            'StartDate': StartDate.get(),
            'OrderDate': OrderDate
        })
    submit_conn.commit()
    # display results
    submit_cur.execute("SELECT * FROM RENTAL")
    result_set = submit_cur.fetchall()
    print("\n\nResult:\n")
    print("\tCustID\t\t\tVehicleID\tRentalType\t")
    i = 1
    for row in result_set:
        print("{}: {}\t{}\t{}\t{}".format(i, row[0], row[1], row[2], row[4]))
        i = i + 1
    i = i - 1
    print("The total rows returned: {}".format(i))
    submit_conn.close()
def search():
    today = date.today()
    submit_conn = sqlite3.connect('CarRental.db')
    submit_cur = submit_conn.cursor()

    #submit_cur.execute("UPDATE RENTAL SET PaymentDate = ? FROM RENTAL WHERE ReturnDate = ?, CustID = ?, VehicleID = ?", (today.strftime("%m/%d/%y"), returnDate.get(), customerID.get(), vehicleInfo.get()))
    submit_cur.execute("SELECT TotalAmount FROM RENTAL WHERE ReturnDate=?, CustID=?, VehicleID=?",(
                           returnDate.get(),
                           customerID.get(),
                           vehicleInfo.get()
    ))
    submit_conn.commit()
    submit_conn.close()

OrderDate = "05/10/2022"

custButton = Button(mainFrame, text="Insert Customer", padx=51, pady=50, command=custClick)
vehicleButton = Button(mainFrame, text="Insert Vehicle", padx=52, pady=50, command=vehicleClick)
returnButton = Button(mainFrame, text="Return Vehicle", padx=50, pady=50, command=returnClick)
rentalButton = Button(mainFrame, text="Rental Reservation", padx=44,pady=50, command=rentalClick)

custButton.grid(row=0, column=0)
vehicleButton.grid(row=0, column=51)
returnButton.grid(row=51, column=51)
rentalButton.grid(row=51, column=0)

#customer
CustID_label = Label(custFrame, text='CustID:')
CustID_label.grid(row=0, column=0)
CustID = Entry(custFrame, width=30)
CustID.grid(row=0, column=1)

Name_label = Label(custFrame, text='Name:')
Name_label.grid(row=1, column=0)
Name = Entry(custFrame, width=30)
Name.grid(row=1, column=1)

Phone_label = Label(custFrame, text='Phone:')
Phone_label.grid(row=2, column=0)
Phone = Entry(custFrame, width=30)
Phone.grid(row=2, column=1)

submit_btn = Button(custFrame, text='Add New Record To DB', width=5, command=submitCust)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

#vehicle
VehicleID_label = Label(vehicleFrame, text='VehicleID:')
VehicleID_label.grid(row=0, column=0)
VehicleID = Entry(vehicleFrame, width=30)
VehicleID.grid(row=0, column=1)

Description_label = Label(vehicleFrame, text='Description:')
Description_label.grid(row=1, column=0)
Description = Entry(vehicleFrame, width=30)
Description.grid(row=1, column=1)

Year_label = Label(vehicleFrame, text='Year:')
Year_label.grid(row=2, column=0)
Year = Entry(vehicleFrame, width=30)
Year.grid(row=2, column=1)

Type_label = Label(vehicleFrame, text='Type:')
Type_label.grid(row=3, column=0)
Type = Entry(vehicleFrame, width=30)
Type.grid(row=3, column=1)

Category_label = Label(vehicleFrame, text='Category:')
Category_label.grid(row=4, column=0)
Category = Entry(vehicleFrame, width=30)
Category.grid(row=4, column=1)

submit_btn = Button(vehicleFrame, text='Add New Record To DB', width=5, command=submitVehicle)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

# req 4
returnDate_label = Label(returnFrame, text='Return Date:')
returnDate_label.grid(row=0, column=0)
returnDate = Entry(returnFrame, width=30)
returnDate.grid(row=0, column=1)

customerID_label = Label(returnFrame, text='Customer ID:')
customerID_label.grid(row=1, column=0)
customerID = Entry(returnFrame, width=30)
customerID.grid(row=1, column=1)

vehicleInfo_label = Label(returnFrame, text='Vehicle ID:')
vehicleInfo_label.grid(row=2, column=0)
vehicleInfo = Entry(returnFrame, width=30)
vehicleInfo.grid(row=2, column=1)

submit_btn = Button(returnFrame, text='Update DB', width=5, command=search)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

# Building the GUI components for req 3
Available_label = Label(rentalFrame, text='Available Car(s) [Description, Year, Type, Category]:')
Available_label.grid(row=0, column=0)
Available = Label(rentalFrame, text='')
Available.grid(row=0, column=1)
# Display Available Rental Car
availcar_conn = sqlite3.connect('CarRental.db')
availcar_cur = availcar_conn.cursor()
availcar_cur.execute(
    "SELECT V.VehicleID, V.Description, V.Year, V.Type, V.Category FROM RENTAL AS R, VEHICLE AS V WHERE R.VehicleID = V.VehicleID AND R.ReturnDate = \"01/29/20\"")
availcar_conn.commit()
result_set = availcar_cur.fetchall()
print("\tVehicleID\tDescription\tYear\tType\tCategory")
i = 1
for row in result_set:
    print("{}: {}\t{}\t{}\t{}".format(i, row[0], row[1], row[2], row[3], row[4]))
    i = i + 1

i = 1
list = []
for row in result_set:
    list.append(row)
Available.config(text=list)

VehicleID_label = Label(rentalFrame, text='Select From The Vehicle Number:')
VehicleID_label.grid(row=1, column=0)
VehicleID = Entry(rentalFrame, width=30)
VehicleID.grid(row=1, column=1)

CustID_label = Label(rentalFrame, text='Enter your CustID:')
CustID_label.grid(row=2, column=0)
CustID = Entry(rentalFrame, width=30)
CustID.grid(row=2, column=1)

RentalType_label = Label(rentalFrame, text='What is your rental period (1 for Daily / 7 for Weekly):')
RentalType_label.grid(row=3, column=0)
RentalType = Entry(rentalFrame, width=30)
RentalType.grid(row=3, column=1)

submit_btn = Button(rentalFrame, text='Add New Record To DB', width=5, command=submitRental)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

StartDate_label = Label(rentalFrame, text='What is your start date? (MM/DD/YYYY)')
StartDate_label.grid(row=4, column=0)
StartDate = Entry(rentalFrame, width=30)
StartDate.grid(row=4, column=1)

#return to menu buttons for each frame
menuButton1 = Button(custFrame, text="Return to Main Menu", width=5, command=returnMain)
menuButton1.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

menuButton2 = Button(vehicleFrame, text="Return to Main Menu", width=5, command=returnMain)
menuButton2.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

menuButton3 = Button(returnFrame, text="Return to Main Menu", width=5, command=returnMain)
menuButton3.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

menuButton4 = Button(rentalFrame, text="Return to Main Menu", width=5, command=returnMain)
menuButton4.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)



root.mainloop()
address_book_connect.commit()
address_book_connect.close()
