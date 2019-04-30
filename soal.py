import random
#https://gist.github.com/cwil323/9b1bfd25523f75d361879adfed550be2

def display_intro():
    title = "** A Simple Math Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

def display_separator():
    print("-" * 24)

def get_user_solution(solution):
    sol1 = solution
    sol2 = solution + random.randrange(1,10)
    sol3 = solution - random.randrange(1,10)
    sol4 = solution - random.randrange(1,10)
    while (sol4 == sol3 ):
        sol4 = solution - random.randrange(1,10)
    pil1 = random.randrange(1,5)
    pil2 = random.randrange(1,5)
    pil3 = random.randrange(1,5)
    pil4 = random.randrange(1,5)
    if (pil2 == pil1):
        pil2 = random.randrange(1,5)
    while ((pil3 == pil2) or (pil3 == pil1)):
        pil3 = random.randrange(1,5)
    while ((pil4 == pil3) or (pil4 == pil2) or (pil4 == pil1)):
        pil4 = random.randrange(1,5)

    if (pil1 == 1):
        print("1.",sol1)
        pil = 1
    elif (pil1 == 2):
        print("1.",sol2)
    elif (pil1 == 3):
        print("1.",sol3)
    else:
        print("1.",sol4)

    if (pil2 == 1):
        print("2.",sol1)
        pil = 2 
    elif (pil2 == 2):
        print("2.",sol2)
    elif (pil2 == 3):
        print("2.",sol3)
    else:
        print("2.",sol4)

    if (pil3 == 1):
        print("3.",sol1)
        pil = 3
    elif (pil3 == 2):
        print("3.",sol2)
    elif (pil3 == 3):
        print("3.",sol3)
    else:
        print("3.",sol4)

    if (pil4 == 1):
        print("4.",sol1)
        pil = 4
    elif (pil4 == 2):
        print("4.",sol2)
    elif (pil4 == 3):
        print("4.",sol3)
    else:
        print("4.",sol4)
    return pil


def main():
    display_intro()
    display_separator()
    correct = False
    while (correct == False):
        number_one = random.randrange(1, 21)
        number_two = random.randrange(1, 21)
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(solution)
        print("Enter your answer")
        print(problem, end="")
        result = int(input(" = "))
        if user_solution == result:
            print("Correct.")
            correct = True
        else:
            print("Incorrect.")
            correct = False
    print("Exit the quiz.")
    display_separator()
    
main()