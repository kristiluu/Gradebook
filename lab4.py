# Kristi Luu - lab 4
from student import Student, IntlStudent, StudentEmployee

class StudentRecord(Student):
    '''This is the StudentRecord class'''
    def __init__(self):
        '''The constructor for StudentRecord class. It has 2 variables: list of countries for International students
        and dictionary of students, organized by 3 keys: student employees (e), international students (i), and students (s).
        The values of each key is an object (one object = one student)'''
        self.__countryList = []
        try:    
            with open("lab4in.txt") as fh:
                    self.__studentRecord = {} #database
                    count = 1
                    for line in fh: 
                        if count % 2 != 0: #odd lines are student type
                            studType = line.rstrip('\n')
                        if count % 2 == 0: #even lines are the lines
                                if studType == "i":
                                    if "i" not in self.__studentRecord:
                                        self.__studentRecord["i"] = [] #default dictionary
                                    try: 
                                        i = IntlStudent(line)
                                        self.__studentRecord[studType].append(i)
                                    except:
                                        print(line.strip('\n') + " is not valid. Not adding to database.")
                                elif studType == "s":
                                    if "s" not in self.__studentRecord:
                                        self.__studentRecord["s"] = [] #default dictionary
                                    try:
                                        s = Student(line)
                                        self.__studentRecord["s"].append(s)
                                    except:
                                        print(line.strip('\n') + " is not valid. Not adding to database.")   
                                elif studType == "e":
                                    if "e" not in self.__studentRecord:
                                        self.__studentRecord["e"] = [] #default dictionary
                                    try:
                                        e = StudentEmployee(line)
                                        self.__studentRecord["e"].append(e)
                                    except:
                                        print(line.strip('\n') + " is not valid. Not adding to database.")   
                                else:
                                    print(line.strip('\n') + " was removed because type " + studType + " is not in the StudentRecord database.")
                        count += 1
        except FileNotFoundError:
            raise SystemExit("lab4in.txt" + " not found")
    def print(self): 
        '''Function that orints each student type, followed by the list of student records of the corresponding type'''
        if "i" in self.__studentRecord: #key = i
            print ("\nInternational Students" + '\n' + '*' * 22)
            for i in range(0, len(self.__studentRecord["i"])):
                self.__studentRecord["i"].sort()
                self.__studentRecord["i"][i].print()
            print("Countries of origin: ", end="")
            print(", ".join(sorted(set(self.__countryList))))
            print()
        if "e" in self.__studentRecord: #key = e
            print ("Employee Students" + '\n' + '*' * 22)
            for i in range(0, len(self.__studentRecord["e"])):
                self.__studentRecord["e"].sort()
                self.__studentRecord["e"][i].print()
        if "s" in self.__studentRecord: #key = s
            print ("Students" + '\n' + '*' * 22)
            for i in range(0, len(self.__studentRecord["s"])):
                self.__studentRecord["s"].sort()
                self.__studentRecord["s"][i].print()
                print()
    def addSalary(self): 
        '''Function that gets salary for each student in the Student Employee type.
        It prompt the user for the pay rate and the hours worked and store them in the student object'''
        for i in range(0, len(self.__studentRecord["e"])):
            self.__studentRecord["e"][i].setSalary()
    def addCountry(self):
        '''Function that gets home country for each student in the International Student type.
        For each student in the International Student type, it prompts the user for the home country and store it in the student object.
        '''
        for i in range(0, len(self.__studentRecord["i"])):
            self.__studentRecord["i"][i].setCountry()
            self.__countryList.append(self.__studentRecord["i"][i].getCountry())
def main() :    
    r = StudentRecord()    
    r.addSalary()    
    r.addCountry()          
    r.print()

main()