# Kristi Luu - Lab 3 
# Worked by myself 

def getData(filename):
    '''Read in each line of the file and store it in a dictionary
    
    Arguments:
        studentDict {dictionary} -- dictionary of keys and values
        key {list} -- list of all keys
    
    Returns:
        {tuple} -- returns a tuple of the dictionary and key list
    '''
    try :    
        with open (filename) as infile: 
            studentDict = dict()
            key = []

            lines = [line.strip().split(",") for line in infile]

            for i in range(0,len(lines)): 
                key.append(lines[i][0])
                studentDict[key[i]] = [] #default dictionary

            for j in range (0, len(lines)): 
                for i in range (1, len(lines[j]), 3): #counts number of elements in list (of the line), goes by 3's, tuples every 3, adds it to dictionary
                    studentDict[key[j]].append(tuple(lines[j][i:i+3]))
            return (studentDict, key)
    except IOError :    
        print("Error: file not found.")

def addData(studentDict, key):
    '''Loop to prompt the user until you have a valid student record to add to your database of student records.
    
    Arguments:
        studentDict {dictionary} 
        key {list} 
    
    Returns:
        {tuple}
    '''
    correctInput = True
    list = []

    name = input('Enter student name: ')
    key.append(name)
    studentDict[name] = []

    num = int(input('Enter an integer for number of class: '))
    
    while num != 0: 
        course = input('Enter comma separated class name, units, grade: ')
        comma_check = commaCheck(course)
        lines = course.lstrip().split(',')
        list = []
        float_check = False
        grade_check = False
        if comma_check:
            for i in range (0, len(lines)):
                list.append(lines[i].strip(' '))
            float_check = floatCheck(list[1])
            grade_check = gradeCheck(list[2])
        if comma_check and float_check and grade_check: 
            studentDict[name].append(tuple(list[0:3]))
            num -= 1
        else:
            if not comma_check:
                print ('Format: class name, units, grade')
    print()
    if num == 0:
        pass
    return (studentDict, key)

def printFile(studentDict, key, gpaDict):
    '''Print all data in the same format as the printData function, but to the file lab3out.txt
    
    Arguments:
        studentDict {dictionary} 
        key {list} 
        gpaDict {dictionary}
    '''
    with open ('lab3out.txt', 'w') as outfile:
        for key in sorted(studentDict): 
            outfile.write(key)
            outfile.write('\n')
            for list_value in studentDict[key]:
                list(list_value)
                outfile.write('{:8s}'.format(list_value[0]))
                outfile.write(' : ')
                outfile.write('{:3s}'.format(list_value[1]))
                outfile.write(' ')
                outfile.write(list_value[2])
                outfile.write('\n')
            for list_value in sorted(gpaDict[key]):
                list(list_value)
                outfile.write(list_value[0])
                outfile.write(': ')
                outfile.write('{:.2f}'.format(float(list_value[1])))
                outfile.write('\n')
            outfile.write('\n')

def printData(studentDict, key):
    '''Calculates GPA and appends to an entirely new GPA dictionary with the same key.
    Then, it prints the student name (key) and class name, unit, grade (values) with the GPA
    in a formatted matter.
    
    Arguments:
        studentDict {dictionary} 
        key {list} 
    
    Returns:
        {tuple} -- returns a tuple of the student dictionary, list of keys, and the new GPA dictionary
    '''
    gpa = 0.0
    gpaDict = {}

    for i in range(0, len(key)):
        gpa = calcGPA(studentDict, key, i)
        gpaDict[key[i]] = []
        if len(gpaDict[key[i]]) != 1:
            gpaDict[key[i]].append(('GPA',gpa))

    for key in sorted(studentDict): 
        print (key)
        for list_value in studentDict[key]:
            list(list_value)
            print ('{:8s}'.format(list_value[0]) +  ' : ' + '{:3s}'.format(list_value[1]) + ' ' + list_value[2])
        for list_value in sorted(gpaDict[key]):
            list(list_value)
            print (list_value[0] + ': ' + '{:.2f}'.format(float(list_value[1])))
        print()
    return (studentDict, key, gpaDict)

def calcGPA(studentDict, key, index): 
    '''Calculate the GPA for one student record. It uses a look-up table (dictionary)
    
    Arguments:
        studentDict {dictionary} 
        key {list} 
        index {int} 
    
    Returns:
        {string} -- returns the number of the gpa in string type
    '''
    gradeBook = { 'A+': [4.0], 'A': [4.0], 'A-': [3.7],     
                  'B+': [3.3], 'B': [3.0], 'B-': [2.7],    
                  'C+': [2.3], 'C': [2.0], 'C-': [1.7],     
                  'D+': [1.0], 'D': [0.7], 'D-': [0.3], 
                  'F': [0.0] } 
    
    unitList = []
    letterList = [] 
    gradeList = []
    total = 0.0
    gpaNum = 0.0
    unitSum = 0.0

    for i in range(0, len(studentDict[key[index]])):
        unitList.append(float(studentDict[key[index]][i][1].strip(' '))) #unitList = list of all unit numbers
        letterList.append(studentDict[key[index]][i][2].strip(' ')) #letterList = list of all letter grades
        if letterList[i] in gradeBook:
            gradeList.append(gradeBook[letterList[i]][0])
        
    for i in range(0, len(gradeList)):
        total += gradeList[i] * unitList[i]
        unitSum += unitList[i]
        gpaNum = round((total / unitSum), 2)
    return str(gpaNum)
    
def floatCheck(userInput):
    '''Accepts user input, which should be just the unit field of every tuple in the dictionary. 
    It will check if the float is appropriate (within range) or is a float in the first place.
    
    Arguments:
        userInput {string} 
    
    Returns:
        boolean -- true if float is ok, false otherwise
    '''
    try:
        val = float(userInput)
        if val < 0.5 or val > 5.0:
            print("Units must be a float and between 0.5 and 5.0")
            return False
        return True
    except TypeError:
        print ("Enter a float instead of" + userInput)
    except ValueError:
        print ("Enter a float instead of" + userInput)
    return False

def commaCheck(userInput): 
    '''Counts the number of commas in the string of the user input. 
    
    Arguments:
        userInput {string}
    
    Returns:
        boolean -- true if comma count is 2 (such that a tuple with 3 fields has 2 commas), false otherwises
    '''
    comma = ','
    count = 0
    
    for char in userInput: 
        if comma == char:
            count += 1
    if count == 2:
        return True
    return False

def gradeCheck(userInput):
    '''Accesses the 3rd field of every tuple in the dictionary. This will check if the grade is appropriate (correct alphabet and sign).
    
    Arguments:
        userInput {string} 
    
    Returns:
        boolean -- true if string meets all requirements, false otherwise
    '''
    sign = '+- '
    grade = 'AaBbCcDdEeFf'
    length = len(userInput)
    
    if length > 3 or length < 0: #letter and sign
        print ('Grade must be A-F and optional + or -')
        return False
    else:
        for i in range(0, length):
            if userInput[i] in grade:
                return True
            if userInput[i] in sign:
                return True
        print ('Grade must be A-F and optional + or -')
    return False

def classNumCheck(userInput):
    '''Checks to make sure that the input by user is an integer for number of classes to add for a new student.
    
    Arguments:
        userInput {string}
    
    Returns:
        boolean -- true if the number is an integer, otherwise, returns false
    '''
    try:
        num = int(userInput)
        return True
    except TypeError:
        print ("Enter an integer instead of" + numOfClass)
        return False
    except ValueError:
        print ("Enter an integer instead of" + numOfClass)
        return False

def main():  
    infilename = 'lab3in.txt'
    (dictionary, key) = getData(infilename)
    printData(dictionary, key)
    (newDict, newKey) = addData(dictionary, key)
    (newDict, newKey, gpaDict) = printData(newDict, newKey)
    printFile(newDict, newKey, gpaDict)

main()
