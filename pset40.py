#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu
    
def computeScore(answers):
    counter = 0
    if (answers[0] == 1):
        counter += 1
    if (answers[0] == 2):
        counter += 2
    if (answers[0] == 3):
        counter += 3
    if (answers[0] == 4):
        counter += 4
    if (answers[1] >= 23):
        counter  += 1
    if (answers[2] == "Yes"):
        counter -= 1
    if (answers[3] == 1):
        counter += 1
    if (answers[4] >= 3.5):
        counter += 1
    return counter

def main():
    a = []
    first = int(input("What year are you?"))
    a.append(first)
    second = int(input("How old are you?"))
    a.append(second)
    third = input("Are you on probation? Yes or no.")
    a.append(third)
    fourth = int(input("Are you Part time or full time? 0 or 1"))
    a.append(fourth)
    fifth = float(input("What is your GPA?"))
    a.append(fifth)
    print("Your housing score is", computeScore(a))

if __name__ == "__main__":
     main()
