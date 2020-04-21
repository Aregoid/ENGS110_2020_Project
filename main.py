import json
import os
import shutil
import sys
import time
import stdiomask
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from colorama import Style, Fore, init
from datetime import datetime


def main():
    init(autoreset=True)

    with open('problems.json') as json_file:
        problems = json.load(json_file)

    # Clear function
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    # No users are detected: default startup
    if os.stat("users.json").st_size == 0:
        sample = "Do you want fancy typing animations like this?"
        for char in sample:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)
        time.sleep(0.5)
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

        def prettywords(message):
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        users = {}

        prettywords("Hello! Welcome to my project!")
        time.sleep(z)
        prettywords(
            "With the help of this app you can publish, solve and discuss problems from your favourite subject!")
        time.sleep(z)
        prettywords("But before we get started, please enter a preferred username and a password.")
        time.sleep(z)
        username = input("Type your username here >>")
        while True:
            password = input("Type your password here >>")
            if len(password) < 4:
                print(Fore.MAGENTA + "The password must be at least 4 letters long. Please try again.")
            else:
                break
        users['registered'] = {}
        users['registered'][username] = {}
        users['registered'][username]['password'] = password
        users['registered'][username]['animation'] = [x, y, z, t]

        file = open("users.json", "w")
        file.write(json.dumps(users))
        file.close()

        print("Nice to meet you " + username + "!")
        time.sleep(z)
        prettywords("You will be shortly redirected to the main menu")
        time.sleep(1)
        cls()  #

    # if users are detected: login or sign up
    else:
        with open("users.json") as outfile:
            users = json.load(outfile)
        check = 0
        password_incorrect_counter = 6
        print("Have you been previously registered? Type [y/n]")
        while True:
            if check == 1:
                break
            answer = input("Type your answer here>>").lower()
            if answer != "y" and answer != "n":
                print(Fore.RED + "Invalid input: type [y] or [n]")
            # login procedure
            if answer == "y":
                cls()
                while True:
                    if check == 1:
                        break
                    username = input("Username>>")
                    if username in users['registered'].keys():
                        while True:
                            password = stdiomask.getpass(prompt="Password>>")
                            # password = input("Password>>")
                            if password == users['registered'][username]['password']:
                                print(Fore.GREEN + 'Login successful! Opening main menu...')
                                time.sleep(0.5)
                                x = users['registered'][username]['animation'][0]
                                y = users['registered'][username]['animation'][1]
                                z = users['registered'][username]['animation'][2]
                                t = users['registered'][username]['animation'][3]
                                check = 1
                                cls()
                                break
                            if not password == users['registered'][username]['password']:
                                password_incorrect_counter = password_incorrect_counter - 1
                                print(Fore.RED + 'Login failed: Invalid password. You have ' + str(
                                    password_incorrect_counter)
                                      + ' attempt(s) left.')
                                if password_incorrect_counter == 0:
                                    print(Fore.RED + "Password entered incorrectly 5 times in a row. Closing the "
                                                     "application...")
                                    time.sleep(1)
                                    sys.exit(0)
                    if username not in users['registered'].keys():
                        print(Fore.RED + 'No such user exists. Please reenter the username...')
            # Sign-up procedure
            if answer == "n":
                cls()
                sample = "Do you want fancy typing animations like this?"
                for char in sample:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.04)
                time.sleep(0.5)
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

                def prettywords(message1):
                    for char in message1:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(x)
                    print(" ")

                with open("users.json") as outfile:
                    users = json.load(outfile)
                prettywords("Hello! Welcome to my project!")
                time.sleep(z)
                prettywords(
                    "With the help of this app you can publish,solve and discuss problems from your favourite subject!")
                time.sleep(z)
                prettywords("But before we get started, please enter a preferred username and a password.")
                time.sleep(z)
                while True:
                    username = input("Type your username here >>")
                    if username in users['registered']:
                        print(
                            Fore.MAGENTA + "Unfortunately, this username has already been taken :( Please try another "
                                           "one...")
                    else:
                        break
                while True:
                    password = input("Type your password here >>")
                    if len(password) < 4:
                        print(Fore.MAGENTA + "The password must be at least 4 letters long. Please try again.")
                    else:
                        break
                users['registered'][username] = {}
                users['registered'][username]['password'] = password
                users['registered'][username]['animation'] = [x, y, z, t]

                file = open("users.json", "w")
                file.write(json.dumps(users))
                file.close()

                print("Nice to meet you " + username + "!")
                time.sleep(z)
                prettywords("You will be shortly redirected to the main menu")
                time.sleep(1)
                cls()
                break

    # the main page, where the user accesses all the main actions
    def main_menu():
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        prettywords(Style.BRIGHT + "<<MAIN MENU>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        time.sleep(z)
        prettywords('''Please choose an action:

If you want to view the list of problems type [list]
If you want to add a problem to the database type [add]
If you want to change the animation speed type [speed]
If you want to log out from the app [logout]
If you want to exit the app type [exit]
''')
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
                add_problem()
                break
            if answer1 == "speed":
                cls()
                time.sleep(t)
                configure_speed()
                break
            if answer1 == "logout":
                cls()
                time.sleep(t)
                main()
                break
            if answer1 == "exit":
                prettywords("Exiting the application...")
                time.sleep(0.5)
                sys.exit()
            else:
                print(Fore.RED + "Invalid input! Please try again.")

    # typing speed configuration page
    def configure_speed():
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        prettywords(Style.BRIGHT + "<<ANIMATION SPEED CONFIGURATION>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        time.sleep(z)

        def set_preference(a, b, c, d):
            with open("users.json") as new_file:
                users = json.load(new_file)
                users['registered'][username]['animation'][0] = a
                users['registered'][username]['animation'][1] = b
                users['registered'][username]['animation'][2] = c
                users['registered'][username]['animation'][3] = d
                file = open("users.json", "w")
                file.write(json.dumps(users))
                file.close()

        prettywords("Please select one of the following presets: [instant] ~ [fast] ~ [normal] ~ [slow]")
        time.sleep(t)
        prettywords("If you want to go back to Main Menu type [main]")
        while True:
            answer = input("Type your answer here >>")
            if answer != "main":
                if answer == "instant":
                    set_preference(0, 0, 0, 0)
                if answer == "fast":
                    set_preference(0.02, 0.5, 0.2, 0.1)
                if answer == "normal":
                    set_preference(0.03, 0.75, 0.3, 0.15)
                if answer == "slow":
                    set_preference(0.04, 1, 0.5, 0.2)
                prettywords("Preference set! Please log in again to see changes.")
                time.sleep(t)
                prettywords("Returning to main menu...")
                time.sleep(0.5)
                cls()
                main_menu()
                break
            if answer == "main":
                prettywords("Speed configuration cancelled.")
                prettywords("Returning to main menu...")
                time.sleep(0.5)
                cls()
                main_menu()
                break
            else:
                print(Fore.RED + "Invalid input. Please try again.")

    # problem addition page
    def add_problem():
        global file_path

        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        prettywords(Style.BRIGHT + "<<ADDITION OF A PROBLEM>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        prettywords("From which subject do you wish to add a problem?")
        time.sleep(t)
        print()
        for key in problems.keys():
            print("--" + key + "--")
            time.sleep(t)
        print()
        prettywords("If you want to go back to main menu type " + Style.BRIGHT + "[main]")
        while True:
            answer3 = input("Type you answer here >>").lower()
            if answer3 != "programming" and answer3 != "physics" and answer3 != "mathematics" and answer3 != "main":
                print(Fore.RED + "Invalid input! Please try again.")
            elif answer3 == "main":
                cls()
                main_menu()
                break
            else:
                break
        print()
        title = input("Please enter a title for the problem >>")
        requirement = input("Please enter a condition for the problem >>")

        if answer3 == "physics":
            check_number = 3
            while True:
                if "phys" + str(check_number) in problems['physics']:
                    check_number = check_number + 1
                else:
                    codename = "phys" + str(check_number)
                    break
        if answer3 == "programming":
            check_number = 3
            while True:
                if "pr" + str(check_number) in problems['programming']:
                    check_number = check_number + 1
                else:
                    codename = "pr" + str(check_number)
                    break
        if answer3 == "mathematics":
            check_number = 3
            while True:
                if "math" + str(check_number) in problems['mathematics']:
                    check_number = check_number + 1
                else:
                    codename = "math" + str(check_number)
                    break

        while True:
            prettywords("Do you need to add an image? Type [yes/no]")
            image_or_not = input("Type the answer here >>").lower()
            if image_or_not != "yes" and image_or_not != "no":
                print(Fore.RED + "Invalid input! Please try again.")
            if image_or_not == "yes":
                prettywords("Please select the file from the pop-up prompt.")
                time.sleep(0.5)
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename()

                def add_image(path):
                    filename = os.path.basename(path)
                    shutil.copy(path, os.getcwd() + "/images")
                    os.rename(os.getcwd() + "/images/" + filename, os.getcwd() + "/images/" + codename + ".png")

                break
            else:
                break
        prettywords("Are you sure you want to add the problem? Type [yes/no]")
        while True:
            confirm = input("Type your answer here >>").lower()
            if confirm == "yes":
                if image_or_not == "yes":
                    add_image(file_path)
                problems[answer3][codename] = {}
                problems[answer3][codename]['title'] = title
                problems[answer3][codename]['requirement'] = requirement
                problems[answer3][codename]['image'] = image_or_not
                problems[answer3][codename]['contributor'] = username
                with open('problems.json', 'w') as outfile:
                    json.dump(problems, outfile)
                prettywords("Problem addition complete! Returning to Main Menu...")
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

    # problem deletion page
    def delete(problem, subject):
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        prettywords("Are you sure you want to delete this problem? Type [yes/no]")
        time.sleep(t)
        while True:
            answer5 = input("Type your answer here>>")
            if answer5 == "yes":
                if problems[subject][problem]['image'] == "yes":
                    os.remove("images/" + problem + '.png')
                del problems[subject][problem]
                with open('problems.json', 'w') as outfile:
                    json.dump(problems, outfile)
                prettywords("Problem deletion complete. Returning to <" + subject + ">...")
                time.sleep(0.5)
                cls()
                break
            if answer5 == "no":
                prettywords("Problem deletion cancelled. Returning to <" + subject + ">...")
                time.sleep(0.5)
                cls()
                break
            else:
                print(Fore.RED + "Invalid input: Please try again.")

    # The page that lists the subjects
    def subjects():
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        prettywords(Style.BRIGHT + "<<SUBJECTS>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        prettywords("Please choose one of the subjects:")
        time.sleep(t)
        print()
        for key in problems.keys():
            print("--" + key + "--")
            time.sleep(t)
        print()
        prettywords('If you want to go back to main menu type ' + Style.BRIGHT + '[main]')

        def question2():
            answer2 = input("Type your answer here >>").lower()
            if answer2 == "main":
                cls()
                main_menu()
            if answer2 == "programming":
                cls()
                view_subject("programming")
            if answer2 == "mathematics":
                cls()
                view_subject("mathematics")
            if answer2 == "physics":
                cls()
                view_subject("physics")
            if answer2 != "programming" and answer2 != "physics" and answer2 != "mathematics":
                print(Fore.RED + "Invalid input. Please try again")
                question2()

        question2()

    # The page that lists problems in the chosen subject
    def view_subject(subject_name):
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        label = subject_name.upper()
        breaker = 0
        prettywords(Style.BRIGHT + "<<" + label + ">>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        prettywords("Please choose a problem:")
        time.sleep(t)
        print()
        for key in problems[subject_name]:
            print(problems[subject_name][key]['title'] + " [" + key + "]")
            time.sleep(t)
        print()
        prettywords("If you want to go back to main menu type " + Style.BRIGHT + "[main]")
        prettywords("If you want to go back to subjects type " + Style.BRIGHT + "[subjects]")
        while True:
            if breaker == 1:
                break
            answer3 = input("Please type your answer here >>")
            if answer3 == "subjects":
                cls()
                subjects()
                break
            if answer3 == "main":
                cls()
                main_menu()
                break
            elif answer3 in problems[subject_name].keys():
                cls()
                if 'contributor' not in problems[subject_name][answer3]:
                    prettywords(problems[subject_name][answer3]['title'])
                else:
                    prettywords(problems[subject_name][answer3]['title'] + " ~ contributed by <" +
                                problems[subject_name][answer3][
                                    'contributor'] + ">")
                prettywords("-------------------------------------------------------")
                prettywords(problems[subject_name][answer3]['requirement'])
                if problems[subject_name][answer3]['image'] == "yes":
                    image = Image.open("images/" + answer3 + '.png')
                    image.show()
                print()
                prettywords('''Choose an action:
Open all comments [list]
Add a comment [comment]
Erase a comment [erase]
Go back to ''' + subject_name + ''' [''' + subject_name + ''']
Go back to subjects [subjects]
Go back to main menu [main]''')
                if 'contributor' in problems[subject_name][answer3] and problems[subject_name][answer3][
                    'contributor'] == username:
                    prettywords("Delete the problem [del]")
                    prettywords("Edit the problem [edit]")
                    print()
                while True:
                    answer4 = input("Type your answer here >>")
                    if answer4 == subject_name:
                        cls()
                        view_subject(subject_name)
                        break
                    if answer4 == "subjects":
                        cls()
                        subjects()
                        break
                    if answer4 == "erase":
                        delete_comments(answer3, subject_name)
                        prettywords("What to do now? Use the commands on the top of the page.")
                    if answer4 == "main":
                        cls()
                        main_menu()
                        break
                    if answer4 == "comment":
                        add_comment(answer3, subject_name)
                        cls()
                        view_subject(subject_name)
                        break
                    # The following 4 "if"s check if the person viewing the problem is its creator. If yes, they view
                    # "edit" and "delete" funtions
                    if answer4 == "del" and 'contributor' in problems[subject_name][answer3] and problems[subject_name][
                        answer3]['contributor'] == username:
                        delete(answer3, subject_name)
                        view_subject(subject_name)
                        break
                    if answer4 == "del" and ('contributor' not in problems[subject_name][answer3] or problems[
                        subject_name][answer3]['contributor'] != username):
                        print(Fore.RED + "Invalid input! Please try again.")
                    if answer4 == "edit" and 'contributor' in problems[subject_name][answer3] and \
                            problems[subject_name][answer3]['contributor'] == username:
                        edit_problem(answer3, subject_name)
                        cls()
                        view_subject(subject_name)
                        break
                    if answer4 == "edit" and ('contributor' not in problems[subject_name][answer3] or problems[
                        subject_name][answer3]['contributor'] != username):
                        print(Fore.RED + "Invalid input! Please try again.")

                    if answer4 == "list":
                        print()
                        if "comments" not in problems[subject_name][answer3]:
                            prettywords("No comments yet...")
                            print()
                            prettywords("What to do now? Use the commands on the top of the page.")
                        elif bool(problems[subject_name][answer3]['comments']):
                            prettywords("No comments yet...")
                            print()
                            prettywords("What to do now? Use the commands on the top of the page.")
                        else:
                            for value in problems[subject_name][answer3]['comments']:
                                for value1 in problems[subject_name][answer3]['comments'][value]:
                                    print("-", value1)
                                    time.sleep(t)
                                    print()
                            prettywords("What to do now? Use the commands on the top of the page.")
                    if answer4 != subject_name and answer4 != "subjects" and answer4 != "main" and answer4 != "comment" \
                            and answer4 != "list" and answer4 != "del" and answer4 != "add" and answer4 != "edit" and answer4 != "erase":
                        print(Fore.RED + "Invalid input: Please try again.")
            else:
                print(Fore.RED + "Invalid input! Please try again.")

    # Comment addition function. Appears only when users view a problem that they have created.
    def add_comment(problem, subject):
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        print()
        comment = input("Enter the comment >> ")
        while True:
            confirmation = input("Submit comment? Type [yes/no] >> ")
            if confirmation == "yes":
                now = datetime.now()
                date_time = now.strftime("%d/%m/%Y %H:%M:%S")
                if 'comments' in problems[subject][problem]:
                    if username in problems[subject][problem]['comments']:
                        problems[subject][problem]['comments'][username].append(
                            comment + " [" + username + " , " + date_time + "]")
                    if username not in problems[subject][problem]['comments']:
                        problems[subject][problem]['comments'][username] = []
                        problems[subject][problem]['comments'][username].append(
                            comment + " [" + username + " , " + date_time + "]")
                else:
                    problems[subject][problem]['comments'] = {}
                    problems[subject][problem]['comments'][username] = []
                    problems[subject][problem]['comments'][username].append(
                        comment + " [" + username + " , " + date_time + "]")
                file1 = open("problems.json", "w")
                file1.write(json.dumps(problems))
                file1.close()
                prettywords("Comment added! Returning to <" + subject + ">...")
                time.sleep(0.5)
                break
            elif confirmation == "no":
                prettywords("Comment addition cancelled. Returning to <" + subject + ">...")
                time.sleep(0.5)
                break
            else:
                print(Fore.RED + "Invalid input! Please try again.")  #

    # Comment edition function. Appears only when users view a problem that they have created.
    def edit_problem(problem, subject):
        print()
        new_title = input("Enter a new title here >>")
        new_requirement = input("Enter a new condition here >>")
        while True:
            confirm = input("Save changes? Type [y/n] >>")
            if confirm == "y":
                problems[subject][problem]['title'] = new_title
                problems[subject][problem]['requirement'] = new_requirement
                del problems[subject][problem]
                file1 = open("problems.json", "w")
                file1.write(json.dumps(problems))
                file1.close()
                print("Problem edited! Returning to <" + subject + ">")
                time.sleep(0.5)
                break
            elif confirm == "n":
                print("Process cancelled. Returning to <" + subject + ">")
                time.sleep(0.5)
                break
            else:
                print(Fore.RED + "Invalid input! Please try again...")

    # Comment deletion function
    def delete_comments(problem, subject):
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        def is_number(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        if 'comments' not in problems[subject][problem]:
            print()
            print("No comments yet...")
            print()
        elif username in problems[subject][problem]['comments'] and bool(problems[subject][problem]['comments'][username]):
            i = 1
            prettywords("Here are all your comments.")
            print()
            for comment in problems[subject][problem]['comments'][username]:
                print(str(i) + ":" + comment)
                i = i + 1
                time.sleep(t)
                print()
            print("Type the number of the comment you want to delete. (You can cancel the process by typing [cancel])")
            while True:
                answer10 = input("Type your answer here >>")
                if answer10 == "cancel":
                    prettywords("Process cancelled...")
                    print()
                    break
                elif is_number(answer10) is True:
                    if int(answer10) < i:
                        del problems[subject][problem]['comments'][username][int(answer10) - 1]
                        file1 = open("problems.json", "w")
                        file1.write(json.dumps(problems))
                        file1.close()
                        print("Comment deleted!")
                        print()
                        break
                    else:
                        print(Fore.RED + "Invalid input! Please try again.")
                if answer10 != "cancel" and is_number(answer10) is False:
                    print(Fore.RED + "Invalid input! Please try again.")
        else:
            print()
            print("You haven't commented on this problem yet.")
            print()

    main_menu()


main()
