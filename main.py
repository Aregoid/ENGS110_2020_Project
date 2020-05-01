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


# Clear function
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# No users detected: First sign up
def start_up():
    sample = "Do you want fancy typing animations like this?"
    for char in sample:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(0.5)
    while True:
        animation_preference = input(" Type [yes/no] >>")
        if animation_preference == "yes":
            text_speed_set = 0.04
            long_pause_set = 0.5
            short_pause_set = 0.2
            cls()
            break
        elif animation_preference == "no":
            text_speed_set = 0
            long_pause_set = 0
            short_pause_set = 0
            cls()
            break
        else:
            print(Fore.RED + 'Invalid input, please type [yes/no]')

    def prettywords(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed_set)
        print(" ")

    users = {}

    prettywords("Hello! Welcome to my project!")
    time.sleep(short_pause_set)
    prettywords(
        "With the help of this app you can publish, solve and discuss problems from your favourite subject!")
    time.sleep(short_pause_set)
    prettywords("But before we get started, please enter a preferred username and a password.")
    time.sleep(short_pause_set)
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
    users['registered'][username]['animation'] = [text_speed_set, long_pause_set, short_pause_set]

    file = open("users.json", "w")
    file.write(json.dumps(users))
    file.close()

    print("Nice to meet you " + username + "!")
    time.sleep(short_pause_set)
    prettywords("You will be shortly redirected to the main menu")
    time.sleep(1)
    cls()
    return [text_speed_set, long_pause_set, short_pause_set, username]


# Users detected: Sign up new user
def sign_up():
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
            text_speed_set = 0.04
            long_pause_set = 0.5
            short_pause_set = 0.2
            cls()
            break
        elif animation_preference == "no":
            text_speed_set = 0
            long_pause_set = 0
            short_pause_set = 0
            cls()
            break
        else:
            print(Fore.RED + 'Invalid input, please type [yes/no]')

    def prettywords(message1):
        for char in message1:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed_set)
        print(" ")

    with open("users.json") as outfile:
        users = json.load(outfile)
    prettywords("Hello! Welcome to my project!")
    time.sleep(short_pause_set)
    prettywords("With the help of this app you can publish,solve and discuss problems from your favourite subject!")
    time.sleep(short_pause_set)
    prettywords("But before we get started, please enter a preferred username and a password.")
    time.sleep(short_pause_set)
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
    users['registered'][username]['animation'] = [text_speed_set, long_pause_set, short_pause_set]

    file = open("users.json", "w")
    file.write(json.dumps(users))
    file.close()

    print("Nice to meet you " + username + "!")
    time.sleep(short_pause_set)
    prettywords("You will be shortly redirected to the main menu")
    time.sleep(1)
    cls()
    return [text_speed_set, long_pause_set, short_pause_set, username]


# Users detected: Log a registered user in
def log_in():
    with open("users.json") as outfile:
        users = json.load(outfile)
    check = 0
    password_incorrect_counter = 6

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
                    text_speed_set = users['registered'][username]['animation'][0]
                    long_pause_set = users['registered'][username]['animation'][1]
                    short_pause_set = users['registered'][username]['animation'][2]
                    check = 1
                    cls()
                    return [text_speed_set, long_pause_set, short_pause_set, username]
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


# the main page, where the user accesses all the main actions
def main_menu(text_speed, long_pause, short_pause, username, problems):
    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
        print(" ")

    prettywords(Style.BRIGHT + "<<MAIN MENU>>")
    prettywords(Style.BRIGHT + "-------------------------------------------------------")
    time.sleep(short_pause)
    prettywords('''Please choose an action:
If you want to view the list of problems type [list]
If you want to add a problem to the database type [add]
If you want to change the animation speed type [speed]
If you want to log out from the app [logout]
If you want to exit the app type [exit]
''')
    time.sleep(short_pause)

    while True:
        answer1 = input("Type your answer here >>").lower()
        if answer1 == "list":
            cls()
            time.sleep(short_pause)
            subjects(text_speed, long_pause, short_pause, username, problems)
            break
        if answer1 == "add":
            cls()
            time.sleep(short_pause)
            add_problem(text_speed, long_pause, short_pause, username, problems)
            break
        if answer1 == "speed":
            cls()
            time.sleep(short_pause)
            configure_speed(text_speed, long_pause, short_pause, username, problems)
            break
        if answer1 == "logout":
            cls()
            time.sleep(short_pause)
            main()
            break
        if answer1 == "exit":
            prettywords("Exiting the application...")
            time.sleep(long_pause)
            sys.exit()
        else:
            print(Fore.RED + "Invalid input! Please try again.")


# Sets animation preference. Used in configure_speed
def set_preference(a, b, c, username):
    with open("users.json") as new_file:
        users = json.load(new_file)
        users['registered'][username]['animation'][0] = a
        users['registered'][username]['animation'][1] = b
        users['registered'][username]['animation'][2] = c
        file = open("users.json", "w")
        file.write(json.dumps(users))
        file.close()


# typing speed configuration page
def configure_speed(text_speed, long_pause, short_pause, username, problems):
    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
        print(" ")

    prettywords(Style.BRIGHT + "<<ANIMATION SPEED CONFIGURATION>>")
    prettywords(Style.BRIGHT + "-------------------------------------------------------")
    time.sleep(short_pause)
    prettywords("Please select one of the following presets: [instant] ~ [fast] ~ [normal] ~ [slow]")
    time.sleep(short_pause)
    prettywords("If you want to go back to Main Menu type [main]")
    while True:
        answer = input("Type your answer here >>")
        if answer != "main":
            if answer == "instant":
                set_preference(0, 0, 0, username)
            if answer == "fast":
                set_preference(0.02, 0.5, 0.2, username)
            if answer == "normal":
                set_preference(0.03, 0.75, 0.3, username)
            if answer == "slow":
                set_preference(0.04, 1, 0.5, username)
            prettywords("Preference set! Please log in again to see changes.")
            time.sleep(short_pause)
            prettywords("Returning to main menu...")
            time.sleep(0.5)
            cls()
            main_menu(text_speed, long_pause, short_pause, username, problems)
            break
        if answer == "main":
            prettywords("Speed configuration cancelled.")
            prettywords("Returning to main menu...")
            time.sleep(0.5)
            cls()
            main_menu(text_speed, long_pause, short_pause, username, problems)
            break
        else:
            print(Fore.RED + "Invalid input. Please try again.")


# problem addition page
def add_problem(text_speed, long_pause, short_pause, username, problems):
    global file_path

    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
        print(" ")

    prettywords(Style.BRIGHT + "<<ADDITION OF A PROBLEM>>")
    prettywords(Style.BRIGHT + "-------------------------------------------------------")
    prettywords("From which subject do you wish to add a problem?")
    time.sleep(short_pause)
    print()
    for key in problems.keys():
        print("--" + key + "--")
        time.sleep(short_pause)
    print()
    prettywords("If you want to go back to main menu type " + Style.BRIGHT + "[main]")
    while True:
        answer3 = input("Type you answer here >>").lower()
        if answer3 != "programming" and answer3 != "physics" and answer3 != "mathematics" and answer3 != "main":
            print(Fore.RED + "Invalid input! Please try again.")
        elif answer3 == "main":
            cls()
            main_menu(text_speed, long_pause, short_pause, username, problems)
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
            main_menu(text_speed, long_pause, short_pause, username, problems)
            break
        if confirm == "no":
            print(Style.BRIGHT + Fore.YELLOW + "Problem addition canceled! Returning to Main Menu")
            time.sleep(1)
            cls()
            main_menu(text_speed, long_pause, short_pause, username, problems)
        else:
            print(Fore.RED + "Invalid input! Please try again.")


# problem deletion page
def delete(problem, subject, text_speed, short_pause, problems):
    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
        print(" ")

    prettywords("Are you sure you want to delete this problem? Type [yes/no]")
    time.sleep(short_pause)
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
def subjects(text_speed, long_pause, short_pause, username, problems):
    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
        print(" ")

    prettywords(Style.BRIGHT + "<<SUBJECTS>>")
    prettywords(Style.BRIGHT + "-------------------------------------------------------")
    prettywords("Please choose one of the subjects:")
    time.sleep(short_pause)
    print()
    for key in problems.keys():
        print("--" + key + "--")
        time.sleep(short_pause)
    print()
    prettywords('If you want to go back to main menu type ' + Style.BRIGHT + '[main]')

    def question2():
        answer2 = input("Type your answer here >>").lower()
        if answer2 == "main":
            cls()
            main_menu(text_speed, long_pause, short_pause, username, problems)
        if answer2 == "programming":
            cls()
            view_subject("programming", text_speed, long_pause, short_pause, username, problems)
        if answer2 == "mathematics":
            cls()
            view_subject("mathematics", text_speed, long_pause, short_pause, username, problems)
        if answer2 == "physics":
            cls()
            view_subject("physics", text_speed, long_pause, short_pause, username, problems)
        if answer2 != "programming" and answer2 != "physics" and answer2 != "mathematics":
            print(Fore.RED + "Invalid input. Please try again")
            question2()

    question2()


# Checks if there is a user that has commented
def check_if_users_have_commented(subject_name, problem, problems):
    if "comments" not in problems[subject_name][problem] or not problems[subject_name][problem]['comments']:
        return False
    else:
        for value in problems[subject_name][problem]['comments']:
            if problems[subject_name][problem]['comments'][value]:
                return True


# The page that lists problems in the chosen subject
def view_subject(subject_name, text_speed, long_pause, short_pause, username, problems):
    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
        print(" ")

    label = subject_name.upper()
    breaker = 0
    prettywords(Style.BRIGHT + "<<" + label + ">>")
    prettywords(Style.BRIGHT + "-------------------------------------------------------")
    prettywords("Please choose a problem:")
    time.sleep(short_pause)
    print()
    for key in problems[subject_name]:
        print(problems[subject_name][key]['title'] + " [" + key + "]")
        time.sleep(short_pause)
    print()
    prettywords("If you want to go back to main menu type " + Style.BRIGHT + "[main]")
    prettywords("If you want to go back to subjects type " + Style.BRIGHT + "[subjects]")
    while True:
        if breaker == 1:
            break
        answer3 = input("Please type your answer here >>")
        if answer3 == "subjects":
            cls()
            subjects(text_speed, long_pause, short_pause, username, problems)
            break
        if answer3 == "main":
            cls()
            main_menu(text_speed, long_pause, short_pause, username, problems)
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
                    view_subject(subject_name, text_speed, long_pause, short_pause, username, problems)
                    break
                if answer4 == "subjects":
                    cls()
                    subjects(text_speed, long_pause, short_pause, username, problems)
                    break
                if answer4 == "erase":
                    delete_comments(answer3, subject_name, text_speed, problems, username)
                    prettywords("What to do now? Use the commands on the top of the page.")
                if answer4 == "main":
                    cls()
                    main_menu(text_speed, long_pause, short_pause, username, problems)
                    break
                if answer4 == "comment":
                    add_comment(answer3, subject_name, problems, text_speed, username)
                    cls()
                    view_subject(subject_name, text_speed, long_pause, short_pause, username, problems)
                    break
                # The following 4 "if"s check if the person viewing the problem is its creator. If yes, they can access
                # "edit" and "delete" functions
                if answer4 == "del" and 'contributor' in problems[subject_name][answer3] and problems[subject_name][
                    answer3]['contributor'] == username:
                    delete(answer3, subject_name, text_speed, short_pause, problems)
                    view_subject(subject_name, text_speed, long_pause, short_pause, username, problems)
                    break
                if answer4 == "del" and ('contributor' not in problems[subject_name][answer3] or problems[
                    subject_name][answer3]['contributor'] != username):
                    print(Fore.RED + "Invalid input! Please try again.")
                if answer4 == "edit" and 'contributor' in problems[subject_name][answer3] and \
                        problems[subject_name][answer3]['contributor'] == username:
                    edit_problem(answer3, subject_name, problems)
                    cls()
                    view_subject(subject_name, text_speed, long_pause, short_pause, username, problems)
                    break
                if answer4 == "edit" and ('contributor' not in problems[subject_name][answer3] or problems[
                    subject_name][answer3]['contributor'] != username):
                    print(Fore.RED + "Invalid input! Please try again.")

                if answer4 == "list":
                    print()
                    if check_if_users_have_commented(subject_name, answer3, problems):
                        for value in problems[subject_name][answer3]['comments']:
                            for value1 in problems[subject_name][answer3]['comments'][value]:
                                print("-", value1)
                                time.sleep(short_pause)
                                print()
                        prettywords("What to do now? Use the commands on the top of the page.")
                    else:
                        prettywords("No comments yet...")
                        print()
                        prettywords("What to do now? Use the commands on the top of the page.")
                if answer4 != subject_name and answer4 != "subjects" and answer4 != "main" and answer4 != "comment" \
                        and answer4 != "list" and answer4 != "del" and answer4 != "add" and answer4 != "edit" and answer4 != "erase":
                    print(Fore.RED + "Invalid input: Please try again.")
        else:
            print(Fore.RED + "Invalid input! Please try again.")


# Comment addition function. Appears only when users view a problem that they have created.
def add_comment(problem, subject, problems, text_speed, username):
    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
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
def edit_problem(problem, subject, problems):
    print()
    new_title = input("Enter a new title here >>")
    new_requirement = input("Enter a new condition here >>")
    while True:
        confirm = input("Save changes? Type [y/n] >>")
        if confirm == "y":
            problems[subject][problem]['title'] = new_title
            problems[subject][problem]['requirement'] = new_requirement
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
def delete_comments(problem, subject, text_speed, problems, username):
    def prettywords(message_main):
        for char in message_main:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(text_speed)
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
            time.sleep(0.2)
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


def main():
    init(autoreset=True)

    with open('problems.json') as json_file:
        problems = json.load(json_file)

    # No users are detected: default startup
    if os.stat("users.json").st_size == 0:
        user_data = start_up()

    # If users are detected: login or sign up
    else:
        print("Have you previously been registered? Type [y/n]")
        while True:
            answer = input("Type your answer here>>").lower()
            if answer != "y" and answer != "n":
                print(Fore.RED + "Invalid input: type [y] or [n]")
            # User registered: log in
            if answer == "y":
                cls()
                user_data = log_in()
                break
            # User not registered: sign up
            if answer == "n":
                cls()
                user_data = sign_up()
                break

    text_speed = user_data[0]
    long_pause = user_data[1]
    short_pause = user_data[2]
    username = user_data[3]

    main_menu(text_speed, long_pause, short_pause, username, problems)


main()
