from logging import PlaceHolder
from struct import calcsize
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Food Truck - 1155")
all_orders = []

#Input: value of the box that's being edited
#Output: True if the value is an int and not negative, False will throw an error if not an int
def checkIfInteger(value):
    if value.isnumeric() or value == "":
        return True
    messagebox.showwarning(title=None, message="Quantity must be an integer!")
    return False

#Input: All int values of number of items purchased
#Returns an array with costs of each item for the order
def calculateCosts(dogs, brats, burgers, fries, sodas, waters):
    return [(dogs, (dogs*2.50)), (brats, (brats*3.50)), (burgers, (burgers*5.0)), (fries, (fries*2.0)), (sodas, (sodas*2.0)), (waters, (waters*0.0))]

#Input: All stringvar versions of number of items purchased
def processPurchase(dogs, brats, burgers, fries, sodas, waters):
    dogs = int(dogs.get())
    brats = int(brats.get())
    burgers = int(burgers.get())
    fries = int(fries.get())
    sodas = int(sodas.get())
    waters = int(waters.get())
    order = calculateCosts(dogs, brats, burgers, fries, sodas, waters)
    all_orders.append(order)
    print(order)
    createMainScreen()

#Input: All string vars
#Output: None
#Takes all string vars and turns them back into 0
def resetStringVars(dogs, brats, burgers, fries, sodas, waters):
    dogs.set("0")
    brats.set("0")
    burgers.set("0")
    fries.set("0")
    sodas.set("0")
    waters.set("0")


#Creates the main GUI for the user
def createMainScreen():
    lbl_hot_dogs = Label(text="Hot dogs - $2.50: ")
    lbl_hot_dogs.grid(column=0, row=0)

    lbl_brats = Label(text="Brats - $3.50: ")
    lbl_brats.grid(column=0, row=1)

    lbl_burgers = Label(text="Hamburgers - $5.00: ")
    lbl_burgers.grid(column=0, row=2)

    lbl_fries = Label(text="Fries - $2.00: ")
    lbl_fries.grid(column=0, row=3)

    lbl_sodas = Label(text="Soda - $2.00: ")
    lbl_sodas.grid(column=0, row=4)

    lbl_waters = Label(text="Water - Free: ")
    lbl_waters.grid(column=0, row=5)

    hot_dogs = StringVar(value="0")
    inp_hot_dogs = Entry(validate='all', textvariable=hot_dogs)
    inp_hot_dogs["validatecommand"] = (inp_hot_dogs.register(checkIfInteger),'%P')
    inp_hot_dogs.grid(column=1, row=0)

    brats = StringVar(value="0")
    inp_brats = Entry(validate='all', textvariable=brats)
    inp_brats["validatecommand"] = (inp_brats.register(checkIfInteger),'%P')
    inp_brats.grid(column=1, row=1)
    
    burgers = StringVar(value="0")
    inp_burgers = Entry(validate='all', textvariable=burgers)
    inp_burgers["validatecommand"] = (inp_burgers.register(checkIfInteger),'%P')
    inp_burgers.grid(column=1, row=2)

    fries = StringVar(value="0")
    inp_fries = Entry(validate='all', textvariable=fries)
    inp_fries["validatecommand"] = (inp_fries.register(checkIfInteger),'%P')
    inp_fries.grid(column=1, row=3)

    sodas = StringVar(value="0")
    inp_sodas = Entry(validate='all', textvariable=sodas)
    inp_sodas["validatecommand"] = (inp_sodas.register(checkIfInteger),'%P')
    inp_sodas.grid(column=1, row=4)

    waters = StringVar(value="0")
    inp_waters = Entry(validate='all', textvariable=waters)
    inp_waters["validatecommand"] = (inp_waters.register(checkIfInteger),'%P')
    inp_waters.grid(column=1, row=5)

    btn_calculate = Button(text="Calculate", command= lambda: processPurchase(hot_dogs, brats, burgers, fries, sodas, waters))
    btn_calculate.grid(column=0, row=6, columnspan=2, sticky="NWES")

    btn_clear = Button(text="Clear", command=lambda: resetStringVars(hot_dogs, brats, burgers, fries, sodas, waters))
    btn_clear.grid(column=0, row=7, columnspan=2, sticky="NWES")

    btn_exit = Button(text="Exit", command=exit)
    btn_exit.grid(column=0, row=8, columnspan=2, sticky="NWES")

def main():
    createMainScreen()
    window.mainloop()

if __name__ == "__main__":
    main()