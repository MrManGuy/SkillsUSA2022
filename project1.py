from tkinter import *
from tkinter import messagebox

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

#Input: Array with all stringvars
#Output: None
#Iterates through items and resets their values
def resetStringVars(items):
    for item in items:
        item.set("0")

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

        for i, v in enumerate(["Hot Dogs", "Brats", "Hamburgers", "Fries", "Sodas", "Waters"]):
            newLabel = Label(text=v + ": " + str(condensed_orders[i][0]) + " - Total Cost: $" + str(condensed_orders[i][1]))
            newLabel.grid(column=3, row=i, sticky="W")
        
        lbl_total = Label(text="Total Cost: $" + str(sum([condensed_orders[i][1] for i in range(6)])))
        lbl_total.grid(column=3, row=6, sticky="W")


#Creates the main GUI for the user
def createRegisterScreen():
    items = [StringVar(value="0"), StringVar(value="0"), StringVar(value="0"), StringVar(value="0"), StringVar(value="0"), StringVar(value="0")]
    for i, v in enumerate(["Hot dogs - $2.50: ", "Brats - $3.50: ", "Hamburgers - $5.00: ", "Fries - $2.00: ", "Sodas - $2.00: ", "Waters - Free:"]):
            newLabel = Label(text=v)
            newLabel.grid(column=0, row=i, sticky="W")

            newEntry = Entry(validate='key', textvariable=items[i])
            newEntry["validatecommand"] = (newEntry.register(checkIfInteger),'%P')
            newEntry.grid(column=1, row=i)

    createTotals()

    btn_calculate = Button(text="Calculate", command= lambda: processPurchase(items))
    btn_calculate.grid(column=0, row=7, columnspan=5, sticky="NWES")

    btn_clear = Button(text="Clear", command=lambda: resetStringVars(items))
    btn_clear.grid(column=0, row=8, columnspan=5, sticky="NWES")

    btn_exit = Button(text="Exit", command=exit)
    btn_exit.grid(column=0, row=9, columnspan=5, sticky="NWES")

def main():
    createRegisterScreen()
    register.mainloop()

if __name__ == "__main__":
    main()