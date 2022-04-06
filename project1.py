from tkinter import *
from tkinter import messagebox
from turtle import width

register = Tk()
register.title("Register - 1155")
all_orders = []

#Input: value of the box that's being edited
#Output: True if the value is an int and not negative, False will throw an error if not an int
def checkIfInteger(value):
    if value.isnumeric() or value == "":
        return True
    messagebox.showwarning(title=None, message=value + " is invalid\nQuantity must be an integer!")
    return False

#Input: All int values of number of items purchased
#Returns an array with costs of each item for the order
def calculateCosts(values):
    return [[values[0], (values[0]*2.50)], [values[1], (values[1]*3.50)], [values[2], (values[2]*5.0)], [values[3], (values[3]*2.0)], [values[4], (values[4]*2.0)], [values[5], (values[5]*0.0)]]

#Input: All stringvar versions of number of items purchased
#Appends each days total to the all_orders array which is used to create the totals segment of the window
def processPurchase(values):
    for i, value in enumerate(values):
        if value.get().isnumeric() == False:
            values[i] = 0
        else:
            values[i] = int(value.get())
    order = calculateCosts(values)
    all_orders.append(order)
    print(order)
    createRegisterScreen()

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

#Creates the screen which will display totals
def createTotals():
    if all_orders == []:
        return
    else:
        #Loops over all items in all orders across all days an totals the values.
        condensed_orders = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        for day in all_orders:
            for pos, item in enumerate(day):
                condensed_orders[pos][0] += item[0]
                condensed_orders[pos][1] += item[1]

        lbl_spacer = Label(text="\t")
        lbl_spacer.grid(column=2, row=0)

        lbl_hot_dogs = Label(text="Hot Dogs: " + str(condensed_orders[0][0]) + " - Total Cost: $" + str(condensed_orders[0][1]))
        lbl_hot_dogs.grid(column=3, row=0, sticky="W")

        lbl_brats = Label(text="Brats: " + str(condensed_orders[1][0]) + " - Total Cost: $" + str(condensed_orders[1][1]))
        lbl_brats.grid(column=3, row=1, sticky="W")

        lbl_burgers = Label(text="Hamburgers: " + str(condensed_orders[2][0]) + " - Total Cost: $" + str(condensed_orders[2][1]))
        lbl_burgers.grid(column=3, row=2, sticky="W")

        lbl_fries = Label(text="Fries: " + str(condensed_orders[3][0]) + " - Total Cost: $" + str(condensed_orders[3][1]))
        lbl_fries.grid(column=3, row=3, sticky="W")

        lbl_sodas = Label(text="Soda: " + str(condensed_orders[4][0]) + " - Total Cost: $" + str(condensed_orders[4][1]))
        lbl_sodas.grid(column=3, row=4, sticky="W")

        lbl_waters = Label(text="Water: " + str(condensed_orders[5][0]) + " - Total Cost: $" + str(condensed_orders[5][1]))
        lbl_waters.grid(column=3, row=5, sticky="W")
        
        lbl_total = Label(text="Total Cost: $" + str(sum([condensed_orders[i][1] for i in range(6)])))
        lbl_total.grid(column=3, row=6, sticky="W")


#Creates the main GUI for the user
def createRegisterScreen():
    lbl_hot_dogs = Label(text="Hot dogs - $2.50: ")
    lbl_hot_dogs.grid(column=0, row=0, sticky="W")

    lbl_brats = Label(text="Brats - $3.50: ")
    lbl_brats.grid(column=0, row=1, sticky="W")

    lbl_burgers = Label(text="Hamburgers - $5.00: ")
    lbl_burgers.grid(column=0, row=2, sticky="W")

    lbl_fries = Label(text="Fries - $2.00: ")
    lbl_fries.grid(column=0, row=3, sticky="W")

    lbl_sodas = Label(text="Soda - $2.00: ")
    lbl_sodas.grid(column=0, row=4, sticky="W")

    lbl_waters = Label(text="Water - Free: ")
    lbl_waters.grid(column=0, row=5, sticky="W")

    hot_dogs = StringVar(value="0")
    inp_hot_dogs = Entry(validate='key', textvariable=hot_dogs)
    inp_hot_dogs["validatecommand"] = (inp_hot_dogs.register(checkIfInteger),'%P')
    inp_hot_dogs.grid(column=1, row=0)

    brats = StringVar(value="0")
    inp_brats = Entry(validate='key', textvariable=brats)
    inp_brats["validatecommand"] = (inp_brats.register(checkIfInteger),'%P')
    inp_brats.grid(column=1, row=1)
    
    burgers = StringVar(value="0")
    inp_burgers = Entry(validate='key', textvariable=burgers)
    inp_burgers["validatecommand"] = (inp_burgers.register(checkIfInteger),'%P')
    inp_burgers.grid(column=1, row=2)

    fries = StringVar(value="0")
    inp_fries = Entry(validate='key', textvariable=fries)
    inp_fries["validatecommand"] = (inp_fries.register(checkIfInteger),'%P')
    inp_fries.grid(column=1, row=3)

    sodas = StringVar(value="0")
    inp_sodas = Entry(validate='key', textvariable=sodas)
    inp_sodas["validatecommand"] = (inp_sodas.register(checkIfInteger),'%P')
    inp_sodas.grid(column=1, row=4)

    waters = StringVar(value="0")
    inp_waters = Entry(validate='key', textvariable=waters)
    inp_waters["validatecommand"] = (inp_waters.register(checkIfInteger),'%P')
    inp_waters.grid(column=1, row=5)

    createTotals()

    btn_calculate = Button(text="Calculate", command= lambda: processPurchase([hot_dogs, brats, burgers, fries, sodas, waters]))
    btn_calculate.grid(column=0, row=7, columnspan=5, sticky="NWES")

    btn_clear = Button(text="Clear", command=lambda: resetStringVars(hot_dogs, brats, burgers, fries, sodas, waters))
    btn_clear.grid(column=0, row=8, columnspan=5, sticky="NWES")

    btn_exit = Button(text="Exit", command=exit)
    btn_exit.grid(column=0, row=9, columnspan=5, sticky="NWES")

def main():
    createRegisterScreen()
    register.mainloop()

if __name__ == "__main__":
    main()