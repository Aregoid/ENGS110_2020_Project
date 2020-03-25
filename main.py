import json
import os
import sys
import time
from PIL import Image

with open('problems.json') as json_file:
    problems = json.load(json_file)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    animation_preference = input("Do you want fancy typing animations? Type [yes/no] -->")
    if animation_preference == "yes":
        x = 0.04
        cls()
        break
    else:
        if animation_preference == "no":
            x = 0
            cls()
            break
        else:
            print("Invalid input, please type [yes/no]")
            time.sleep(1)
            cls()


def prettywords():
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(x)
    print(" ")


users = {}
message = "Hello! Welcome to my project!"
prettywords()
time.sleep(0.5)
message = "This app allows you to publish, solve and discuss your favourite science problems."
prettywords()
time.sleep(0.5)
message = "But before we get started, please enter a preferred username."
prettywords()
time.sleep(0.5)
users["username"] = input("Type your answer here -->")

file = open("users.json", "w")
file.write(json.dumps(users))
file.close()

print("Nice to meet you", users["username"], "!")
time.sleep(0.5)
message = "You will be shortly redirected to the main menu"
prettywords()
time.sleep(1)
cls()


def main_menu():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    print("<<MAIN MENU>>")
    print("-------------------------------------------------------")
    time.sleep(0.5)
    message_main = ('''
Please choose an action:

If you want to view the list of problems type [list]
If you want to add a problem to the database type [add]''')
    prettywords()
    time.sleep(0.2)

    def question1():
        answer1 = input("Type your answer here -->").lower()
        if answer1 == "list":
            cls()
            time.sleep(0.2)
            subjects()
        if answer1 == "add":
            cls()
            time.sleep(0.2)
            add()
        if answer1 != "add" and answer1 != "list":
            print("Invalid input. Please try again")
            question1()

    question1()


def add():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    def explanation():
        print("In order to simplify the interaction between the machine and the user, each problem is given a unique "
              "codename. A codename is a shortened, version of the title, that is much easier to type than the title "
              "itself. When choosing the problem, only its codename has to be entered (see the example below)")
        print('''                   Hello World [helloworld]
                     ^^^          ^^^
                    Title       Codename
                ''')

    print("<<ADDITION OF A PROBLEM>>")
    print("-------------------------------------------------------")
    message_main = "From which subject do you wish to add a problem?"
    prettywords()
    for key in problems.keys():
        print(key)
        time.sleep(0.5)
    message_main = "If you want to go back to main menu type [main]"
    prettywords()
    answer3 = input("Type you answer here -->").lower()
    if answer3 != "programming" and answer3 != "physics" and answer3 != "mathematics" and answer3 != "main":
        print("Please type one of the following: mathematics, physics, programming, main ")
        time.sleep(2)
        cls()
        add()

    cls()
    expl = input("Do you wish to see an explanation? [yes/no] >>")
    if expl == "yes":
        explanation()
    title = input("Please enter a title for the problem >>")
    codename = input("Please enter a codename >>").lower()
    requirement = input("Please enter a condition for the problem >>")
    message_main = "Do you need to add an image? Type [yes/no]"
    prettywords()
    image_or_not = input("Type the answer here >>").lower()
    if image_or_not == "yes":
        message_main = "Please rename the image to" + codename + "and move it to the folder containing the " \
                                                                 "application "
        prettywords()
    message_main = "Are you sure you want to add the problem? Type [yes/no]"
    prettywords()
    confirm = input("Type your answer here >>").lower()
    if confirm == "yes":
        if answer3 == "mathematics":
            s = input("stop")
        if answer3 == "physics":
            s = input("stop")
        if answer3 == "programming":
            s = input("stop")
        if answer3 == "main":
            s = input("stop")


def subjects():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    print("<<SUBJECTS>>")
    print("-------------------------------------------------------")
    message_main = "Please choose one of the subjects"
    prettywords()
    time.sleep(0.2)
    for key in problems.keys():
        print(key)
        time.sleep(0.5)
    message_main = "If you want to go back to main menu type [main]"
    prettywords()

    def question2():
        answer2 = input("Type your answer here -->").lower()
        if answer2 == "main":
            cls()
            main_menu()
        if answer2 == "programming":
            cls()
            programming()
        if answer2 == "mathematics":
            cls()
            mathematics()
        if answer2 == "physics":
            cls()
            physics()
        if answer2 != "programming" and answer2 != "physics" and answer2 != "mathematics":
            print("Invalid input. Please try again")
            question2()

    question2()


def programming():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    print("<<PROGRAMMING>>")
    print("-------------------------------------------------------")
    message_main = "Please choose a problem"
    prettywords()
    for key in problems["programming"].keys():
        print(problems['programming'][key]['title'])
        time.sleep(0.5)
    message_main = "If you want to go back to main menu type [main]"
    prettywords()
    message_main = "If you want to go back to subjects type [subjects]"
    prettywords()
    answer3 = input("Please type your answer here -->")
    if answer3 == "subjects":
        cls()
        subjects()
    if answer3 == "main":
        cls()
        main_menu()
    else:
        cls()
        print(problems['programming'][answer3]['title'])
        print("-------------------------------------------------------")
        print(problems['programming'][answer3]['requirement'])
        if problems['programming'][answer3]['image'] == "yes":
            image = Image.open(answer3 + '.png')
            image.show()
        answer_problem_programming = input("stop")


def physics():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    print("<<PHYSICS>>")
    print("-------------------------------------------------------")
    message_main = "Please choose a problem"
    prettywords()
    for key in problems["physics"].keys():
        print(problems["physics"][key]["title"])
        time.sleep(0.5)
    message_main = "If you want to go back to main menu type [main]"
    prettywords()
    message_main = "If you want to go back to subjects type [subjects]"
    prettywords()
    answer3 = input("Please type your answer here -->")
    if answer3 == "subjects":
        cls()
        subjects()
    if answer3 == "main":
        cls()
        main_menu()
    else:
        cls()
        print(problems['physics'][answer3]['title'])
        print("-------------------------------------------------------")
        print(problems['physics'][answer3]['requirement'])
        if problems['physics'][answer3]['image'] == "yes":
            image = Image.open(answer3 + '.png')
            image.show()
        answer_problem_programming = input("stop")


def mathematics():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    print("<<MATHEMATICS>>")
    print("-------------------------------------------------------")
    message_main = "Please choose a problem"
    prettywords()
    for key in problems["mathematics"].keys():
        print(problems["mathematics"][key]["title"])
        time.sleep(0.5)
    message_main = "If you want to go back to main menu type [main]"
    prettywords()
    message_main = "If you want to go back to subjects type [subjects]"
    prettywords()
    answer3 = input("Please type your answer here -->")
    if answer3 == "subjects":
        cls()
        subjects()
    if answer3 == "main":
        cls()
        main_menu()
    else:
        cls()
        print(problems['mathematics'][answer3]['title'])
        print("-------------------------------------------------------")
        print(problems['mathematics'][answer3]['requirement'])
        if problems['mathematics'][answer3]['image'] == "yes":
            image = Image.open(answer3 + '.png')
            image.show()
        answer_problem_programming = input("stop")


main_menu()
