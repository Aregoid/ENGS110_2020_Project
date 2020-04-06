import json
import os
import sys
import time
from PIL import Image
from colorama import Style, Fore, init


def main():
    init(autoreset=True)

    with open('problems.json') as json_file:
        problems = json.load(json_file)

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    # Detecting users/registration of new users
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
        password = input("Type your password here >>")
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
        cls()

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
            if answer == "y":
                cls()
                while True:
                    if check == 1:
                        break
                    username = input("Username>>")
                    if username in users['registered'].keys():
                        while True:
                            password = input("Password>>")
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
                password = input("Type your password here >>")

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
                add()
                break
            if answer1 == "speed":
                cls()
                time.sleep(t)
                speed()
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

    def speed():
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
            if answer == "instant":
                set_preference(0, 0, 0, 0)
                prettywords("Preference set! Please log in again to see changes.")
                time.sleep(t)
                prettywords("Returning to main menu...")
                time.sleep(0.5)
                cls()
                main_menu()
                break
            if answer == "fast":
                set_preference(0.02, 0.5, 0.2, 0.1)
                prettywords("Preference set! Please log in again to see changes.")
                time.sleep(t)
                prettywords("Returning to main menu...")
                time.sleep(0.5)
                cls()
                main_menu()
                break
            if answer == "normal":
                set_preference(0.03, 0.75, 0.3, 0.15)
                prettywords("Preference set! Please log in again to see changes.")
                time.sleep(t)
                prettywords("Returning to main menu...")
                time.sleep(0.5)
                cls()
                main_menu()
                break
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

    def add():
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        def explanation():
            print(
                "In order to simplify the interaction between the machine and the user, each problem is given a unique "
                "codename. A codename is a shortened, version of the title, that is much easier to type than the title "
                "itself. When choosing the problem, only its codename has to be entered (see the example below)")
            print('''                   Hello World [helloworld]
                         ^^^          ^^^
                        Title       Codename
                    ''')

        prettywords(Style.BRIGHT + "<<ADDITION OF A PROBLEM>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        prettywords("From which subject do you wish to add a problem?")
        time.sleep(t)
        for key in problems.keys():
            print("--" + key + "--")
            time.sleep(t)
        prettywords("If you want to go back to main menu type " + Style.BRIGHT + "[main]")
        answer3 = input("Type you answer here >>").lower()
        if answer3 != "programming" and answer3 != "physics" and answer3 != "mathematics" and answer3 != "main":
            print(Fore.RED + "Please type one of the following: mathematics, physics, programming, main ")
            time.sleep(1.5)
            cls()
            add()
        if answer3 == "main":
            cls()
            main_menu()
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
        while True:
            codename = input("Please enter a codename for the problem >>").lower()
            if codename in problems[answer3]:
                print(Fore.MAGENTA + "Codename already taken ;_; Please enter another one:")
            else:
                break
        requirement = input("Please enter a condition for the problem >>")
        while True:
            prettywords("Do you need to add an image? Type [yes/no]")
            image_or_not = input("Type the answer here >>").lower()
            if image_or_not == "yes":
                prettywords(
                    "Please rename the image to " + "<" + codename + ".png>" + " and move it to " + os.getcwd() + "\images")
                prettywords(
                    "Please note! The image must be of .png format. If it's not, please convert it to .png before "
                    "moving it to the given directory ")
                answer = input("Do you want to open the directory right now? Type [yes/no] >>")
                if answer == "yes":
                    os.startfile(os.getcwd() + "/images")
                break
            if image_or_not == "no":
                break
            else:
                print(Fore.RED + "Invalid input! Please try again.")
        prettywords("Are you sure you want to add the problem? Type [yes/no]")
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
                    prettywords("Problem addition complete! Returning to Main Menu...")
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
                    prettywords("Problem addition complete! Returning to Main Menu...")
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
                if subject == "programming":
                    if problems['programming'][problem]['image'] == "yes":
                        os.remove("images/" + problem + '.png')
                    del problems['programming'][problem]
                    with open('problems.json', 'w') as outfile:
                        json.dump(problems, outfile)
                    prettywords("Problem deletion complete. Returning to <Programming>...")
                    time.sleep(1)
                    cls()
                    programming()
                    break
                if subject == "mathematics":
                    if problems['mathematics'][problem]['image'] == "yes":
                        os.remove("images/" + problem + '.png')
                    del problems['mathematics'][problem]
                    with open('problems.json', 'w') as outfile:
                        json.dump(problems, outfile)
                    prettywords("Problem deletion complete. Returning to <Mathematics>...")
                    time.sleep(1)
                    cls()
                    mathematics()
                    break
                if subject == "physics":
                    if problems['physics'][problem]['image'] == "yes":
                        os.remove("images/" + problem + '.png')
                    del problems['physics'][problem]
                    with open('problems.json', 'w') as outfile:
                        json.dump(problems, outfile)
                    prettywords("Problem deletion complete. Returning to <Physics>...")
                    time.sleep(1)
                    cls()
                    physics()
                    break
            if answer5 == "no":
                if subject == "programming":
                    prettywords("Problem deletion cancelled. Returning to <Programming>...")
                    time.sleep(1)
                    cls()
                    programming()
                    break
                if subject == "mathematics":
                    prettywords("Problem deletion cancelled. Returning to <Mathematics>...")
                    time.sleep(1)
                    cls()
                    mathematics()
                    break
                if subject == "physics":
                    prettywords("Problem deletion cancelled. Returning to <Physics>...")
                    time.sleep(1)
                    cls()
                    physics()
                    break
            else:
                print(Fore.RED + "Invalid input: Please try again.")

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
        print()
        for key in problems.keys():
            print("--" + key + "--")
            time.sleep(t)
        print()
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
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        breaker = 0
        prettywords(Style.BRIGHT + "<<PROGRAMMING>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        prettywords("Please choose a problem:")
        time.sleep(t)
        print()
        for key in problems['programming']:
            print(problems['programming'][key]['title'] + " [" + key + "]")
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
            elif answer3 in problems['programming'].keys():
                cls()
                if 'contributor' not in problems['programming'][answer3]:
                    prettywords(problems['programming'][answer3]['title'])
                else:
                    prettywords(problems['programming'][answer3]['title'] + " ~ contributed by <" +
                                problems['programming'][answer3][
                                    'contributor'] + ">")
                prettywords("-------------------------------------------------------")
                prettywords(problems['programming'][answer3]['requirement'])
                if problems['programming'][answer3]['image'] == "yes":
                    image = Image.open("images/" + answer3 + '.png')
                    image.show()
                print()
                prettywords('''Choose an action:
Open all comments [open]
Add a comment [com]
Go back to <Programming> [programming]
Go back to <Subjects> [subjects]
Go back to <Main Menu> [main]''')
                if answer3 != "helloworld" and answer3 != "sumofprimes" and problems['programming'][answer3][
                        'contributor'] == username:
                    prettywords("Delete the problem [del]")
                    prettywords("Edit the problem [edit]")
                while True:
                    answer4 = input("Type your answer here >>")
                    if answer4 == "programming":
                        cls()
                        programming()
                        break
                    if answer4 == "subjects":
                        cls()
                        subjects()
                        break
                    if answer4 == "main":
                        cls()
                        main()
                        break
                    if answer4 == "com":
                        add_comment()
                        break
                    if answer4 == "del":
                        if answer3 != "helloworld" and answer3 != "sumofprimes" and problems['programming'][answer3][
                                'contributor'] == username:
                            delete(answer3, "programming")
                            break
                        else:
                            print(Fore.RED + "Invalid input: Please try again.")
                    if answer == "edit":
                        if answer3 != "helloworld" and answer3 != "sumofprimes" and problems['programming'][answer3][
                                'contributor'] == username:
                            # edit function
                            break
                        else:
                            print(Fore.RED + "Invalid input: Please try again.")
                    if answer4 == "open":
                        print("Bla bla bla")
                        break
                    if answer4 != "programming" and answer4 != "subjects" and answer4 != "main" and \
                            answer4 != "com" and answer4 != "open" and answer4 != "del" and answer4 != "add":
                        print(Fore.RED + "Invalid input: Please try again.")
            else:
                print(Fore.RED + "Invalid input! Please try again.")

    def physics():
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        prettywords(Style.BRIGHT + "<<PHYSICS>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        prettywords("Please choose a problem:")
        time.sleep(t)
        print()
        for key in problems['physics']:
            print(problems['physics'][key]['title'] + " [" + key + "]")
            time.sleep(t)
        print()
        prettywords("If you want to go back to main menu type " + Style.BRIGHT + "[main]")
        prettywords("If you want to go back to subjects type " + Style.BRIGHT + "[subjects]")
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
                    if 'contributor' not in problems['physics'][answer3]:
                        prettywords(problems['physics'][answer3]['title'])
                    else:
                        prettywords(
                            problems['physics'][answer3]['title'] + " ~ contributed by <" + problems['physics'][answer3][
                                'contributor'] + ">")
                    prettywords("-------------------------------------------------------")
                    prettywords(problems['physics'][answer3]['requirement'])
                    if problems['physics'][answer3]['image'] == "yes":
                        image = Image.open("images/" + answer3 + '.png')
                        image.show()
                    print()
                    prettywords('''Choose an action:
Open all comments [open]
Add a comment [com]
Go back to <Physics> [physics]
Go back to <Subjects> [subjects]
Go back to <Main Menu> [main]''')
                    if answer3 != "isoatm" and answer3 != "basicc" and problems['physics'][answer3][
                            'contributor'] == username:
                        prettywords("Delete the problem [del]")
                        prettywords("Edit the problem [edit]")
                    while True:
                        answer4 = input("Type your answer here >>")
                        if answer4 == "physics":
                            cls()
                            physics()
                            break
                        if answer4 == "subjects":
                            cls()
                            subjects()
                            break
                        if answer4 == "main":
                            cls()
                            main_menu()
                            break
                        if answer4 == "com":
                            add_comment()
                            break
                        if answer4 == "del":
                            if answer3 != "isoatm" and answer3 != "basicc" and problems['physics'][answer3][
                                    'contributor'] == username:
                                delete(answer3, "physics")
                                break
                            else:
                                print(Fore.RED + "Invalid input: Please try again.")
                        if answer == "edit":
                            if answer3 != "isoatm" and answer3 != "basicc" and problems['physics'][answer3][
                                 'contributor'] == username:
                                # edit function
                                break
                            else:
                                print(Fore.RED + "Invalid input: Please try again.")
                        if answer4 == "open":
                            print("Bla bla bla")
                            break
                        if answer4 != "physics" and answer4 != "subjects" and answer4 != "main" and answer4 != "com" \
                                and answer4 != "open" and answer4 != "del" and answer4 != "add":
                            print(Fore.RED + "Invalid input: Please try again.")
                else:
                    print(Fore.RED + "Invalid input! Please try again.")

    def mathematics():
        def prettywords(message_main):
            for char in message_main:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(x)
            print(" ")

        prettywords(Style.BRIGHT + "<<MATHEMATICS>>")
        prettywords(Style.BRIGHT + "-------------------------------------------------------")
        prettywords("Please choose a problem:")
        time.sleep(t)
        print()
        for key in problems['mathematics']:
            print(problems['mathematics'][key]['title'] + " [" + key + "]")
            time.sleep(t)
        print()
        prettywords("If you want to go back to main menu type " + Style.BRIGHT + "[main]")
        prettywords("If you want to go back to subjects type " + Style.BRIGHT + "[subjects]")
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
                    if 'contributor' not in problems['mathematics'][answer3]:
                        prettywords(problems['mathematics'][answer3]['title'])
                    else:
                        prettywords(problems['mathematics'][answer3]['title'] + " ~ contributed by <" +
                                    problems['mathematics'][answer3][
                                        'contributor'] + ">")
                    prettywords(Style.BRIGHT + "-------------------------------------------------------")
                    print(problems['mathematics'][answer3]['requirement'])
                    if problems['mathematics'][answer3]['image'] == "yes":
                        image = Image.open("images/" + answer3 + '.png')
                        image.show()
                    print()
                    prettywords('''Choose an action:
Open all comments [open]
Add a comment [com]
Go back to <Physics> [physics]
Go back to <Subjects> [subjects]
Go back to <Main Menu> [main]''')
                    if answer3 != "3g" and answer3 != "mbone" and problems['mathematics'][answer3][
                        'contributor'] == username:
                        prettywords("Delete the problem [del]")
                        prettywords("Edit the problem [edit]")
                    while True:
                        answer4 = input("Type your answer here >>")
                        if answer4 == "mathematics":
                            cls()
                            mathematics()
                            break
                        if answer4 == "subjects":
                            cls()
                            subjects()
                            break
                        if answer4 == "main":
                            cls()
                            main_menu()
                            break
                        if answer4 == "com":
                            add_comment()
                            break
                        if answer4 == "del":
                            if answer3 != "3g" and answer3 != "mbone" and problems['mathematics'][answer3][
                                    'contributor'] == username:
                                delete(answer3, "mathematics")
                                break
                            else:
                                print(Fore.RED + "Invalid input: Please try again.")
                        if answer == "edit":
                            if answer3 != "3g" and answer3 != "mbone" and problems['mathematics'][answer3][
                                    'contributor'] == username:
                                # edit function
                                break
                            else:
                                print(Fore.RED + "Invalid input: Please try again.")
                        if answer4 == "open":
                            print("Bla bla bla")
                            break
                        if answer4 != "mathematics" and answer4 != "subjects" and answer4 != "main" and \
                                answer4 != "com" and answer4 != "open" and answer4 != "del" and answer4 != "add":
                            print(Fore.RED + "Invalid input: Please try again.")
                else:
                    print(Fore.RED + "Invalid input! Please try again.")

    def add_comment():
        pass

    main_menu()


main()
