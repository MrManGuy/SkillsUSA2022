from tkinter import *
from tkinter import messagebox

grades = Tk()
grades.title("Grades - 1155")
all_grades = {"Art": [], "History": [], "Math": [], "Programming": [], "Science": []}

def callError(digit):
    messagebox.showwarning(title=None, message=digit + " is invalid\nQuantity must be a float!")

#Input: value of the box that's being edited
#Output: True if the value is an float and not negative, False will throw an error if not an float
def checkIfFloat(value):
    for digit in value:
        if not (digit.isdigit() or digit == "."):
            callError(digit)
            return False
    return True

#Input: All stringvar versions of number of items purchased
#Appends each days total to the all_orders array which is used to create the totals segment of the window
def processGrade(score):
    grade = round(float(score[1].get()))
    for digit in score[1].get():
        if not (digit.isdigit() or digit == "."):
            grade = 0
    all_grades[score[0]].append(grade)
    print(all_grades)


#Creates the main GUI for the student
def createGradesScreen():
    grades = [StringVar(value="0"),StringVar(value="0"),StringVar(value="0"),StringVar(value="0"),StringVar(value="0")]
    #For loop that runs through all the classes and creates labels and entries for them at the row that corresponds with their index
    for i, v in enumerate(["Art", "History", "Math", "Programming", "Science"]):
        newLabel = Label(text=v + " Grade: ")
        newLabel.grid(column=0, row=i, sticky="W")

        newEntry = Entry(validate='key', textvariable=grades[i])
        newEntry["validatecommand"] = (newEntry.register(checkIfFloat),'%P')
        newEntry.grid(column=1, row=i)

    #createTotals()

    btn_calculate = Button(text="Calculate", command= lambda: processGrade([inp_class.get(inp_class.curselection()[0]), grade]))
    btn_calculate.grid(column=0, row=7, columnspan=5, sticky="NWES")

    btn_clear = Button(text="Clear")
    btn_clear.grid(column=0, row=8, columnspan=5, sticky="NWES")

    btn_exit = Button(text="Exit", command=exit)
    btn_exit.grid(column=0, row=9, columnspan=5, sticky="NWES")

def main():
    createGradesScreen()
    grades.mainloop()

if __name__ == "__main__":
    main()