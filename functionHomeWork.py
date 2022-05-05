def inputGrades(nm):
    gradeList = []
    for i in range(0, nm, 1):
        grade = float (input('Please enter your grade: '))
        gradeList.append(grade)
    return gradeList

def printGrades(nm, grades):
    for i in range (0, nm, 1):
        print(grades[i])

def AvGrades(nm, grades):
    totlGrade = 0
    for i in range (0, nm, 1):
       totlGrade =  totlGrade + grades[i]
    avgGrades = totlGrade/nm
    return avgGrades 

def highLowValue(nm, grades):
    maxGrade = 0
    minGrade = 1000
    for i in range(0, nm, 1):
        if (maxGrade < grades[i]):
            maxGrade = grades[i]
    
    for i in range (0, nm, 1):
        if(minGrade > grades[i]):
            minGrade = grades[i]
    return maxGrade, minGrade


numbGrade = int(input('Please enter how many grade you want to input: '))
x = inputGrades(numbGrade)
print ('Here is your grades: ')
printGrades(numbGrade, x)

a = AvGrades(numbGrade, x)
print( 'Here is your grade average: ', round(a,1))

y,w = highLowValue (numbGrade, x) 
print('The maximum grade is', y)
print ('The minimun grade is', w)

