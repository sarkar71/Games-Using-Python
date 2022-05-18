# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    q_num = 1

    for k in questions:
        print("-------------------------")
        print(k)
        for i in options[q_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(k), guess)
        q_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who invented Bulb?: ": "C",
 "How many Laws of Motion are there?" : "C",
 "Who invented Radio?: ": "A",
 "Einstein won the Nobel Prize in which year?:" : "B",
    
}

options = [["A. Tesla", "B. Einstein", "C. Thomas A. Edison ", "D. Maxwell"],
          ["A. 1", "B. 2", "C. 3", "D. 4"],
          ["A. G. Marconi", "B. Jagdish Chandra Bose", "C. Tesla", "D. CV Raman"],
          ["A. 1912","B. 1922", "C. 1915", "D. 1914"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")

# -------------------------