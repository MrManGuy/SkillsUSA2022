from logging import PlaceHolder
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Food Truck - 1155")

#Input: value of the box that's being edited
#Output: True if the value is an int, False will throw an error if not an int
def checkIfInteger(value):
    if value.isnumeric() or value == "":
        return True
    messagebox.showerror(title=None, message="Quantity must be an integer!")
    return False

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

    hot_dogs = StringVar()
    inp_hot_dogs = Entry(validate='all', textvariable=hot_dogs)
    inp_hot_dogs["validatecommand"] = (inp_hot_dogs.register(checkIfInteger),'%P')
    inp_hot_dogs.grid(column=1, row=0)

    brats = StringVar()
    inp_brats = Entry(validate='all', textvariable=brats)
    inp_brats["validatecommand"] = (inp_brats.register(checkIfInteger),'%P')
    inp_brats.grid(column=1, row=1)
    
    burgers = StringVar()
    inp_burgers = Entry(validate='all', textvariable=burgers)
    inp_burgers["validatecommand"] = (inp_burgers.register(checkIfInteger),'%P')
    inp_burgers.grid(column=1, row=2)

    fries = StringVar()
    inp_fries = Entry(validate='all', textvariable=fries)
    inp_fries["validatecommand"] = (inp_fries.register(checkIfInteger),'%P')
    inp_fries.grid(column=1, row=3)

    sodas = StringVar()
    inp_sodas = Entry(validate='all', textvariable=sodas)
    inp_sodas["validatecommand"] = (inp_sodas.register(checkIfInteger),'%P')
    inp_sodas.grid(column=1, row=4)

    inp_waters = Entry()
    inp_waters.grid(column=1, row=5)

def main():
    createMainScreen()
    window.mainloop()

if __name__ == "__main__":
    main()