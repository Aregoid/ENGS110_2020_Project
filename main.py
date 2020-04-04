import json
import os
import sys
import time
from PIL import Image
from colorama import Style, Fore, init

init(autoreset=True)

with open('problems.json') as json_file:
    problems = json.load(json_file)

users = {}


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


sample = "Do you want fancy typing animations like this?"
for char in sample:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)

while True:
    animation_preference = input(" Type [yes/no] >>")
    if animation_preference == "yes":
        x = 0.04
        y = 1
        z = 0.5
        t = 0.2
        cls()
        break
    elif animation_preference == "no":
        x = 0
        y = 0
        z = 0
        t = 0
        cls()
        break
    else:
        print(Fore.RED + 'Invalid input, please type [yes/no]')


def prettywords():
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(x)
    print(" ")


message = "Hello! Welcome to my project!"
prettywords()
time.sleep(z)
message = "This app allows you to publish, solve and discuss your favourite science problems."
prettywords()
time.sleep(z)
message = "But before we get started, please enter a preferred username."
prettywords()
time.sleep(z)
username = input("Type your answer here >>")
users["username"] = username

file = open("users.json", "w")
file.write(json.dumps(users))
file.close()

print("Nice to meet you " + username + "!")
time.sleep(z)
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

    message_main = Style.BRIGHT + "<<MAIN MENU>>"
    prettywords()
    message_main = Style.BRIGHT + "-------------------------------------------------------"
    prettywords()
    time.sleep(z)
    message_main = ('''Please choose an action:

If you want to view the list of problems type [list]
If you want to add a problem to the database type [add]
If you want to delete a problem type [del]
''')
    prettywords()
    time.sleep(t)

    while True:
        answer1 = input("Type your answer here >>").lower()
        if answer1 == "list":
            cls()
            time.sleep(t)
            subjects()
            break
        if answer1 == "add":
            cls()
            time.sleep(t)
            add()
            break
        if answer1 == "del":
            cls()
            time.sleep(t)
            delete()
            break
        else:
            print(Fore.RED + "Invalid input! Please try again.")


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

    message_main = Style.BRIGHT + "<<ADDITION OF A PROBLEM>>"
    prettywords()
    message_main = Style.BRIGHT + "-------------------------------------------------------"
    prettywords()
    message_main = "From which subject do you wish to add a problem?"
    prettywords()
    time.sleep(t)
    for key in problems.keys():
        print(key)
        time.sleep(t)
    message_main = "If you want to go back to main menu type " + Style.BRIGHT + "[main]"
    prettywords()
    answer3 = input("Type you answer here >>").lower()
    if answer3 != "programming" and answer3 != "physics" and answer3 != "mathematics" and answer3 != "main":
        print(Fore.RED + "Please type one of the following: mathematics, physics, programming, main ")
        time.sleep(2)
        cls()
        add()
    if answer3 == "main":
        main_menu()
    cls()
    while True:
        expl = input("Do you wish to see an explanation? [yes/no] >>")
        if expl == "yes":
            explanation()
            break
        if expl == "no":
            break
        else:
            print(Fore.RED + "Invalid input! Please try again.")
    title = input("Please enter a title for the problem >>")
    codename = input("Please enter a codename for the problem >>").lower()
    requirement = input("Please enter a condition for the problem >>")
    while True:
        message_main = "Do you need to add an image? Type [yes/no]"
        prettywords()
        image_or_not = input("Type the answer here >>").lower()
        if image_or_not == "yes":
            message_main = "Please rename the image to " + "<" + codename + ".png>" + " and move it to " + os.getcwd()
            prettywords()
            break
        if image_or_not == "no":
            break
        else:
            print(Fore.RED + "Invalid input! Please try again.")
    message_main = "Are you sure you want to add the problem? Type [yes/no]"
    prettywords()
    while True:
        confirm = input("Type your answer here >>").lower()
        if confirm == "yes":
            if answer3 == "mathematics":
                problems['mathematics'][codename] = {}
                problems['mathematics'][codename][
                    'title'] = title
                problems['mathematics'][codename]['requirement'] = requirement
                problems['mathematics'][codename]['image'] = image_or_not
                problems['mathematics'][codename]['contributor'] = username
                with open('problems.json', 'w') as outfile:
                    json.dump(problems, outfile)
                message_main = "Problem addition complete! Returning to Main Menu..."
                prettywords()
                time.sleep(1)
                cls()
                main_menu()
                break
            if answer3 == "physics":
                problems['physics'][codename] = {}
                problems['physics'][codename][
                    'title'] = title
                problems['physics'][codename]['requirement'] = requirement
                problems['physics'][codename]['image'] = image_or_not
                problems['physics'][codename]['contributor'] = username
                with open('problems.json', 'w') as outfile:
                    json.dump(problems, outfile)
                message_main = "Problem addition complete! Returning to Main Menu..."
                prettywords()
                time.sleep(1)
                cls()
                main_menu()
                break
            if answer3 == "programming":
                problems['programming'][codename] = {}
                problems['programming'][codename][
                    'title'] = title
                problems['programming'][codename]['requirement'] = requirement
                problems['programming'][codename]['image'] = image_or_not
                problems['programming'][codename]['contributor'] = username
                with open('problems.json', 'w') as outfile:
                    json.dump(problems, outfile)
                message_main = "Problem addition complete! Returning to Main Menu..."
                prettywords()
                time.sleep(1)
                cls()
                main_menu()
                break
        if confirm == "no":
            print(Style.BRIGHT + Fore.YELLOW + "Problem addition canceled! Returning to Main Menu")
            time.sleep(1)
            cls()
            main_menu()
        else:
            print(Fore.RED + "Invalid input! Please try again.")


def delete():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    message_main = "From which subject do you wish to delete a problem?"
    prettywords()
    time.sleep(t)
    for key in problems.keys():
        print(key)
        time.sleep(t)
    message_main = "If you want to go back to Main Menu type [main]"
    prettywords()
    while True:
        answer3 = input("Type you answer here >>")
        if answer3 == "mathematics":
            message_main = "To delete the problem, please enter its codename."
            prettywords()
            time.sleep(t)
            message_main = "If you want to stop the procedure type [main]"
            prettywords()
            time.sleep(t)
            while True:
                answer4 = input("Type your answer here>>")
                if answer4 == "main":
                    message_main = "Problem deletion cancelled. Returning to Main Menu..."
                    prettywords()
                    time.sleep(1)
                    cls()
                    main_menu()
                    break
                if answer4 in problems['mathematics']:
                    if username == problems['mathematics'][answer4]['contributor']:
                        if problems['mathematics'][answer4]['image'] == "yes":
                            os.remove(answer4 + '.png')
                        del problems['mathematics'][answer4]
                        with open('problems.json', 'w') as outfile:
                            json.dump(problems, outfile)
                        message_main = "Problem deletion complete. Returning to Main Menu..."
                        prettywords()
                        time.sleep(1)
                        cls()
                        main_menu()
                        break
                    if not username == problems['mathematics'][answer4]['contributor']:
                        print(Fore.RED + "You are not the contributor of this problem, therefore you can't delete it.")
                        print(Fore.RED + "Please enter another codename or go back to main menu by typing [main]")
                if answer4 not in problems['mathematics']:
                    print(Fore.RED + "No such problem in the given category")
                    print(Fore.RED + "Please enter another codename or go back to main menu by typing [main]")

        if answer3 == "physics":
            message_main = "To delete the problem, please enter its codename."
            prettywords()
            time.sleep(t)
            message_main = "If you want to stop the procedure type [main]"
            prettywords()
            time.sleep(t)
            while True:
                answer4 = input("Type your answer here>>")
                if answer4 == "main":
                    message_main = "Problem deletion cancelled. Returning to Main Menu..."
                    prettywords()
                    time.sleep(1)
                    cls()
                    main_menu()
                    break
                if answer4 in problems['physics']:
                    if username == problems['physics'][answer4]['contributor']:
                        if problems['physics'][answer4]['image'] == "yes":
                            os.remove(answer4 + '.png')
                        del problems['physics'][answer4]
                        with open('problems.json', 'w') as outfile:
                            json.dump(problems, outfile)
                        message_main = "Problem deletion complete. Returning to Main Menu..."
                        prettywords()
                        time.sleep(1)
                        cls()
                        main_menu()
                        break
                    if not username == problems['physics'][answer4]['contributor']:
                        print(
                            Fore.RED + "You are not the contributor of this problem, therefore you can't delete it.")
                        print(Fore.RED + "Please enter another codename or go back to main menu by typing [main]")
                if answer4 not in problems['physics']:
                    print(Fore.RED + "No such problem in the given category")
                    print(Fore.RED + "Please enter another codename or go back to main menu by typing [main]")

        if answer3 == "programming":
            message_main = "To delete the problem, please enter its codename."
            prettywords()
            time.sleep(t)
            message_main = "If you want to stop the procedure type [main]"
            prettywords()
            time.sleep(t)
            while True:
                answer4 = input("Type your answer here>>")
                if answer4 == "main":
                    message_main = "Problem deletion cancelled. Returning to Main Menu..."
                    prettywords()
                    time.sleep(1)
                    cls()
                    main_menu()
                    break
                if answer4 in problems['programming']:
                    if username == problems['programming'][answer4]['contributor']:
                        if problems['mathematics'][answer4]['image'] == "yes":
                            os.remove(answer4 + '.png')
                        del problems['programming'][answer4]
                        with open('problems.json', 'w') as outfile:
                            json.dump(problems, outfile)
                        message_main = "Problem deletion complete. Returning to Main Menu..."
                        prettywords()
                        time.sleep(1)
                        cls()
                        main_menu()
                        break
                    if not username == problems['physics'][answer4]['contributor']:
                        print(
                            Fore.RED + "You are not the contributor of this problem, therefore you can't delete it.")
                        print(Fore.RED + "Please enter another codename or go back to main menu by typing [main]")
                if answer4 not in problems['physics']:
                    print(Fore.RED + "No such problem in the given category")
                    print(Fore.RED + "Please enter another codename or go back to main menu by typing [main]")

        if answer3 == "main":
            message_main = "Problem deletion cancelled. Returning to Main Menu..."
            prettywords()
            time.sleep(1)
            cls()
            main_menu()
            break
        if not answer3 == "main" and answer3 == "programming" and answer3 == "physics" and "mathematics":
            print(Fore.RED + "Invalid input! Please try again.")


def subjects():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    message_main = Style.BRIGHT + "<<SUBJECTS>>"
    prettywords()
    message_main = Style.BRIGHT + "-------------------------------------------------------"
    prettywords()
    message_main = "Please choose one of the subjects:"
    prettywords()
    time.sleep(t)
    for key in problems.keys():
        print(key)
        time.sleep(t)

    message_main = 'If you want to go back to main menu type ' + Style.BRIGHT + '[main]'
    prettywords()

    def question2():
        answer2 = input("Type your answer here >>").lower()
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
            print(Fore.RED + "Invalid input. Please try again")
            question2()

    question2()


def programming():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    message_main = Style.BRIGHT + "<<PROGRAMMING>>"
    prettywords()
    message_main = Style.BRIGHT + "-------------------------------------------------------"
    prettywords()
    message_main = "Please choose a problem:"
    prettywords()
    time.sleep(t)
    for key in problems['programming']:
        print(problems['programming'][key]['title'] + " [" + key + "]")
        time.sleep(t)
    message_main = "If you want to go back to main menu type " + Style.BRIGHT + "[main]"
    prettywords()
    message_main = "If you want to go back to subjects type " + Style.BRIGHT + "[subjects]"
    prettywords()
    while True:
        answer3 = input("Please type your answer here >>")
        if answer3 == "subjects":
            cls()
            subjects()
            break
        if answer3 == "main":
            cls()
            main_menu()
            break
        else:
            if answer3 in problems['programming'].keys():
                cls()
                message_main = problems['programming'][answer3]['title']
                prettywords()
                message_main = "-------------------------------------------------------"
                prettywords()
                message_main = problems['programming'][answer3]['requirement']
                prettywords()
                if problems['programming'][answer3]['image'] == "yes":
                    image = Image.open(answer3 + '.png')
                    image.show()
                answer_problem_programming = input("stop")
                break
            else:
                print(Fore.RED + "Invalid input! Please try again.")


def physics():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    message_main = Style.BRIGHT + "<<PHYSICS>>"
    prettywords()
    message_main = Style.BRIGHT + "-------------------------------------------------------"
    prettywords()
    message_main = "Please choose a problem:"
    prettywords()
    time.sleep(t)
    for key in problems['physics']:
        print(problems['physics'][key]['title'] + " [" + key + "]")
        time.sleep(t)
    message_main = "If you want to go back to main menu type " + Style.BRIGHT + "[main]"
    prettywords()
    message_main = "If you want to go back to subjects type " + Style.BRIGHT + "[subjects]"
    prettywords()
    while True:
        answer3 = input("Please type your answer here >>")
        if answer3 == "subjects":
            cls()
            subjects()
            break
        if answer3 == "main":
            cls()
            main_menu()
            break
        else:
            if answer3 in problems['physics'].keys():
                cls()
                print(problems['physics'][answer3]['title'])
                print("-------------------------------------------------------")
                print(problems['physics'][answer3]['requirement'])
                if problems['physics'][answer3]['image'] == "yes":
                    image = Image.open(answer3 + '.png')
                    image.show()
                answer_problem_programming = input("stop")
                break
            else:
                print(Fore.RED + "Invalid input! Please try again.")


def mathematics():
    def prettywords():
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(x)
        print(" ")

    message_main = Style.BRIGHT + "<<MATHEMATICS>>"
    prettywords()
    message_main = Style.BRIGHT + "-------------------------------------------------------"
    prettywords()
    message_main = "Please choose a problem:"
    prettywords()
    time.sleep(t)
    for key in problems['mathematics']:
        print(problems['mathematics'][key]['title'] + " [" + key + "]")
        time.sleep(t)
    message_main = "If you want to go back to main menu type " + Style.BRIGHT + "[main]"
    prettywords()
    message_main = "If you want to go back to subjects type " + Style.BRIGHT + "[subjects]"
    prettywords()
    while True:
        answer3 = input("Please type your answer here >>")
        if answer3 == "subjects":
            cls()
            subjects()
            break
        if answer3 == "main":
            cls()
            main_menu()
            break
        else:
            if answer3 in problems['mathematics'].keys():
                cls()
                print(problems['mathematics'][answer3]['title'])
                print("-------------------------------------------------------")
                print(problems['mathematics'][answer3]['requirement'])
                if problems['mathematics'][answer3]['image'] == "yes":
                    image = Image.open(answer3 + '.png')
                    image.show()
                answer_problem_programming = input("stop")
                break
            else:
                print(Fore.RED + "Invalid input! Please try again.")


main_menu()
