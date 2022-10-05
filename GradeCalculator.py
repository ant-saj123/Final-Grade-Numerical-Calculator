

def option(number):

    print("")
    if(number == 1):
            numClasses = int(input(("How many classes would you like include in your numerical calculation? ")))
            honors = float(input("What is the multiplier for honors classes? "))
            ap = float(input("What is the multiplier for AP classes? "))
            dual = float(input("What is the multiplier for dual credit classes? "))
            regular = float(input("What is the multiplier for regular classes? "))
            return calculate_Num_Grade(numClasses,honors,ap,dual,regular)
    if(number == 2):
        curGrade = float(input("What is your current grade in the class?"))
        weight = float(input("What percent of your grade is your final?"))
        target = float(input("What grade is your target grade?"))
        return calculate_Final_Grade(curGrade,weight,target)
    if (number == 3):
        curGrade = float(input("What is your current grade in the class?"))
        weight = float(input("What percent of your grade is your final?"))
        hypgrade = float(input("What hypothetical final exam grade do you want to use?"))
        return calculate_Hyp_Grade(curGrade,weight,hypgrade)
    if (number == 4):
        numClasses = int(input(("How many different categories does this class have? ")))
        return calculate_Class_Grade(numClasses)

def calculate_Class_Grade(numClasses):
    print("")
    i = 0
    n= 0
    grade = 0
    myPercents = [numClasses]
    myGrades = [numClasses]

    while i < numClasses:
        myPercents.append(float(input("What percent of the class grade is category " + str(i))))
        myGrades.append(float(input("What average grade do you have in that category ")))
        i = i+1


    while n < len(myPercents):
        grade = grade + float((float(myPercents[n]/100) * myGrades[n]))
        n = n+1

    return grade




def calculate_Hyp_Grade(curGrade,weight,hypgrade):
    final = float(curGrade*float((100-weight)/100) + float(hypgrade*float(weight/100)))
    return final

def calculate_Final_Grade(curGrade,weight,target):
    percent = float((100-weight)/100)
    curr = float(percent * curGrade)
    final = float(((target-curr))/(weight/100))
    return final




def calculate_Num_Grade(numClasses,honors,ap,dual,regular):


        print("")
        print("1.  Honors")
        print("2.  AP")
        print("3.  Dual Credit")
        print("4.  Regular")
        i = 0
        numerical = 0

        print("")


        while i < numClasses:
           choice = int(input("Enter the number of the type of class grade you would like to enter. "))
           grade = float(input("What was your grade in the class? "))
           if(choice == 1):
                numerical = numerical + float(honors * grade)
           if (choice == 2):
                numerical = numerical + float(ap * grade)
           if (choice == 3):
                numerical = numerical + float(dual * grade)
           if (choice == 4):
                numerical = numerical + float(regular * grade)
           i = i+1
           print("")





        return  (numerical/numClasses)






def main():
    print("Calculate Weighted Numerical or Final Grade")

    print("Which type of grade would you like to calculate?")
    print("1.  Weighted Numerical Grade?")
    print("2.  Final Exam Score necessary to reach a Target Grade?")
    print("3.  Hypothetical Final Grade after a hypothetical Final Exam Score?")
    print("4.  Class Grade With Differently Weighted Categories?")
    print("")

    number = int(input("Pick one of the option numbers!! "))



    if number ==1:
      print("")
      print("Your numerical is: ", option(number))
    if number ==2:
      print("")
      print("To reach your target, you will need to get a: ", option(number))
    if number ==3:
      print("")
      print("Your Hypothetical Final Grade will be: ", option(number))
    if number ==4:
      print("")
      print("Your class grade is: ", option(number))


main()





