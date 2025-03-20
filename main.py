import random, os

def clear():
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def get_raw():
    # get raw data as lines
    with open("data.txt", "r", encoding="utf-8") as f:
        raw = f.readlines()
    f.close()

    return raw


def main():
    clear()

    raw = get_raw()
    data = []

    for r in raw:
        data.append(r.split(" ... "))

    for p in data:
        p[1] = p[1].strip("\n")

    # shuffle for random order with every use
    random.shuffle(data)

    c = 0
    for p in data:
        print(f"-- {c+1}/{len(data)} --")       # progress counter
        print(p[0], end="")                     # word
        input()                                 # wait for "continue"
        print(p[1], end="")                     # reveal
        input()
        c += 1
        clear()                                 # clear screen for next word

if __name__ == "__main__":
    main()