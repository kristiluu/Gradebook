#student.py module for student record program
GRADEBOOK = { 'A+': 4.0, 'A': 4.0, 'A-': 3.7,     
              'B+': 3.3, 'B': 3.0, 'B-': 2.7,    
              'C+': 2.3, 'C': 2.0, 'C-': 1.7,     
              'D+': 1.0, 'D': 0.7, 'D-': 0.3, 
              'F': 0.0 } 

class Student:
    '''This is a parent class called Student'''
    def __init__(self, line):
        '''Constructor for Student class. It accepts a line and splits it. Raises errors as necessary.'''
        lineSplit = line.strip("\n").split(",")
            
        tupledLine = []
        for i in range (1, len(lineSplit), 3): 
            tupledLine.append(tuple(lineSplit[i:i+3]))
            
        if ((len(lineSplit)-1) % 3 != 0): 
            raise IndexError

        for i in range (0, len(tupledLine)):
            if not 0.5 <= float(tupledLine[i][1]) <= 5.0:
                raise ValueError("Units must be a float and between 0.5 and 5.0")
            if tupledLine[i][2] not in GRADEBOOK:
                raise ValueError("Grade must be A-F with + or -")
            
        self._name = lineSplit[0].strip("\n")
        classes = lineSplit[1:]
        self._classes = [tuple(lineSplit[i:i+3]) for i in range(1, len(classes), 3)]
        self.__calcGPA(self._classes)
    def __calcGPA(self, classes):
        '''Private method that calculates the GPA of each student'''
        total = 0
        credits = 0
        for data in self._classes: 
            total += float(data[1]) * GRADEBOOK[data[2]]
            credits += float(data[1])
        self._gpa = round(total/credits, 2)
    def print(self):
        '''Prints name, classes, gpa in formatted matter'''
        print(self._name)
        for i in range(0, len(self._classes)):
            print("{:8s}".format(self._classes[i][0]) +  " : " + "{:3s}".format(self._classes[i][1]) + " " + self._classes[i][2])
        print ("GPA: " + "{:.2f}".format(self._gpa))
    def __lt__(self, rhs):
        '''Compares less than for names'''
        return self._name < rhs._name
    def __gt__(self, rhs):
        '''Compares greater than for names'''
        return self._name > rhs._name
    def __eq__(self, rhs): #it's possible someone can have the same exact name
        '''Compares equality for names'''
        return self._name == rhs._name


class IntlStudent(Student):
    '''This is the International Student class, child of parent Student class'''
    def __init__(self, line):
        '''Constructor for International Student class'''
        super().__init__(line)
    def setCountry(self):
        '''Setter function for home country of international students'''
        country = input("\n" + self._name + ": Home country? ").title()
        self._homecountry = country
    def print(self):
        '''Prints country in addition to the name, classes, and GPA'''
        super().print()
        print ("Country: " + self._homecountry + "\n")
    def getCountry(self):
        '''Getter function that returns the home country for each international student'''
        return self._homecountry
        

class StudentEmployee(Student):
    '''This is the Student Employee class, child of parent class Student, sibling of International Student class'''
    def __init__(self, line):
        '''Constructor for Student Employee class'''
        super().__init__(line)
    def setSalary(self):
        '''Setter for salary of student employees'''
        correctPay = False
        while not correctPay: 
            try: 
                pay = float(input("\n" + self._name + ": Pay rate? "))
                correctPay = True
            except ValueError:
                print("Could not convert to float. Try again.")
        correctHours = False
        while not correctHours: 
            try: 
                hours = float(input("Number of hours? "))
                correctHours = True
            except ValueError:
                print("Could not convert to float. Try again.")
        monthsalary = pay * hours
        self._salary = round(monthsalary, 2)
    def print(self):
        '''Prints salary along with name, classes, and GPA'''
        super().print()
        print ("Salary:", "${:.2f} per month".format(self._salary), "\n")
