from tkinter import *
from tkinter import messagebox

grades = Tk()
grades.title("Grades - 1155")
#Arrary created with each class in mind to hold the grades for each class
all_grades = [[], [], [], [], []]

def checkIfInRange(value):
    if value == "":
        value = 0

    if 0 <= float(value) and float(value) <= 100:
        return True
    return False

#Input: value of the box that's being edited
#Output: True if the value is an float and not negative, False will throw an error if not an float
def checkIfFloat(value):
    for digit in value:
        if not (digit.isdigit() or digit == "."):
            messagebox.showwarning(title=None, message=digit + " is invalid\nQuantity must be a float!")
            return False

    if checkIfInRange(value):
        return True
    messagebox.showwarning(title=None, message="Quantity must be between 0 and 100")
    return False

def createOutputs():
    classes_list = ["Art", "History", "Math", "Programming", "Science"]
    
    lbl_spacer = Label(text="\t")
    lbl_spacer.grid(column=2, row=0)

    for i, v in enumerate(all_grades):
        newLabel = Label(text=classes_list[i] + " - Grades Entered: " + str(len(v)) + " - Average Grade: " + str(round(float(sum(v)/len(v)))) + " - High Grade: " + str(max(v)) + " - Low Grade: " + str(min(v)))
        newLabel.grid(column = 3, row=i, sticky="W")
    
#Input: List of grades as stringvars
#Loops through all grades and resets them to 0
def resetStringVars(grades):
    for grade in grades:
        grade.set("0")

#Input: All stringvar versions of number of grades
#Appends each grade to all_grades to create a list of all class's grades
def processGrades(grades):
    for i, grade in enumerate(grades):
        for digit in grade.get():
            if not (digit.isdigit() or digit == "."):
                grade = 0
        grade = float(grade.get())
        
        all_grades[i].append(grade)
    resetStringVars(grades)
    createOutputs()


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

    btn_calculate = Button(text="Calculate", command= lambda: processGrades(grades))
    btn_calculate.grid(column=0, row=7, columnspan=5, sticky="NWES")

    btn_clear = Button(text="Clear", command=lambda: resetStringVars(grades))
    btn_clear.grid(column=0, row=8, columnspan=5, sticky="NWES")

    btn_exit = Button(text="Exit", command=exit)
    btn_exit.grid(column=0, row=9, columnspan=5, sticky="NWES")

    lbl_contestant_number = Label(text="Contestant Number : 1155")
    lbl_contestant_number.grid(column=0, row=10, columnspan=5, sticky="NEWS")

def main():
    createGradesScreen()
    grades.mainloop()

if __name__ == "__main__":
    main()