import random
import time
import os

def easy_mode():
    return (999,999999, 3)
def normal_mode():
    return (999999,999999999, 5)
def hard_mode():
    return (999999999, 999999999999, 7)
def check(question,answer):
    diff = []
    result = []
    str_question = list(str(question))
    str_answer = list(str(answer))
    if len(str_answer) != len(str_question):
        print ("WRONG")
    else:
        for j in range(len(str_answer)):
            for i in range(len(str_question)):
                if i == j and int(str_answer[j]) != int(str_question[i]):
                    diff.append(i)
        for j in range(len(str_answer)):
            if j in diff:
                result.append(str_question[j])
            else:
                result.append('*')
        print ("----------------------------------------" +''.join(result)+ "----------------------------------------" + "\n")    
def main():
    print ("Try remember faster and faster you can and write your answer bellow")
    choice = int(input("0 for Easy, 1 for Normal and 2 for Hard: "))
    print (choice)
    if choice == 0:
        min = easy_mode()[0]
        max = easy_mode()[1]
        ts = easy_mode()[2]
    elif choice == 1:
        min = normal_mode()[0]
        max = normal_mode()[1]
        ts = normal_mode()[2]
    elif choice == 2:
        min = hard_mode()[0]
        max = hard_mode()[1]
        ts = hard_mode()[2]
    else:
        min = 0
        max = 10
        ts = 2
    while True:
        question = random.randint(min, max)
        print ("----------------------------------------" + str(question) + "----------------------------------------" )
        print ("                                   Clear after 5s                                    ")
        time.sleep(ts)
        os.system('cls')
        answer = int(input("Write your answer:                      "))
        if answer == question:
            print (answer)
        else:
            check(question,answer)
            print ("                                   Clear after" ,ts,"s")
            time.sleep(5)
            os.system('cls')
main()
             
