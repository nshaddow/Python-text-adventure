import os

run = True
menu = True
play = False
rules = False
key = False

hp = 50
atk = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

map = [[],
       [],
       []]

def clear():
    os.system("cls")

def draw():
    print("#############################")

def save():
    list = [
        name,
        str(hp),
        str(atk),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt", "w")
    for item in list:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        clear()
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. RULES")
        print("4. QUIT GAME")
        draw()
        if rules:
            print("I'm the creator of this game and here are the rules!")
            rules = False
            choice = ""
            input("# ")
        else:
          choice = input("# ")
        if choice == "1":
            clear()
            name = input("# What is your name, hero? ")
            draw()
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    hp = int(load_list[1][:-1])
                    atk = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    print(name, hp, atk, pot, elix, gold, x, y, key)
                    clear()
                    print("Welcome back," + name)
                    draw()
                    input("# ")
                    menu = False
                    play = True
                else:
                    print("corrupt save file...")
                    input("# ")
            except OSError:
                print("No loadable save file.")
                input("# ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()
    while play:
        save() #autosave
        print("# NAME: ", name)
        dest = input("# ")
        if dest == "0":
            play = False
            menu = True