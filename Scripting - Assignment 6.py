"""
Intro to Scripting
Assignment 6
Carl Hilliard
March 7, 2022
"""

##Question 1: Student class

## Question 1, Part 1: Create a class "student which holds firstname(string), lastname(string), email(string), all_course(list of numbers)
class Student:
    ## define the __init__ method
    def __init__(self, firstName, lastName, email, allGrades):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.allGrades = allGrades

        









## define main
def main():
    allStudents = []
    ## create a read in object
    with open("students.txt", "r") as studentsFile: ## while students.txt is reading, assign the file to the variable studentsFile
        next(studentsFile) ## skip the first line
        ## read in from the file using a for loop
        for line in studentsFile:
            splitLine = line.split() ## split the strings on spaces
            splitGrades = splitLine[3].split(",") ## split the grades on commas
            student = Student(splitLine[0], splitLine[1], splitLine[2], splitGrades) ## create a student object using the strings as arguments
            allStudents.append(student) ## append the student object to the allStudents list

    for s in allStudents:
        print(s.firstName)
        ##DELET BELOW BEFROE SUBMISSION
    allStudents.sort(key=lambda x: x.firstName)
    print("Sorted: \n")
    for s in allStudents:
        print(s.firstName)
main()
    

    #Take data from 25 student file and append it to original file of the 10 students (./students.txt)
    ##with open("previousStudents.txt", "
"""def secondFileProcessing():
    file1 = open("students.txt", 'a+')
    file2 = open("previousStudents.txt", 'r')
    file1.write(file2.read())
    for line in file1:
        #print(line)
        #do same process as before but eith previousStudents
        #sort based on first name
        allPreviousStudents.sort(_.firstName)"""
    
        












































