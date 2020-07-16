import random
import sys
import time

print("Hello. Welcome to the 21 arena.")
time.sleep(3)

playerscore = 0
dealerscore = 0
card = random.randint(2,10)
card1 = random.randint(2,11)
card2 = random.randint(5,10)
card3 = random.randint(5,11)
card4 = random.randint(2, 11)
card5 = random.randint(3, 7)
card7 = random.randint(3, 7)
card6 = random.randint(2, 11)
card8 = random.randint(2, 11)
card9 = random.randint(3, 7)

while True:
    n = input("Do you want to play? ")
    if n.lower() == "no":
        print("Okay. Bye!")
        sys.exit()
    elif n.lower() == "yes":
        print("Well, I guess, let's get started!")
        time.sleep(3)
        print("You will be playing against me, the dealer.")
        time.sleep(3)
        if card1 <= 10:
            print(f"You drew a {card} and a {card1}, for a total of {card + card1}.")
            time.sleep(3)
        if card1 == 11:
            print(f"You drew a {card} and an ace for a score of {11 + card}")
            time.sleep(3)
        playerscore = playerscore + card + card1
        if playerscore == 21:
            print("Ugh. You win.")
            sys.exit()
        if card3 <= 10:
            print(f"I drew a {card2} and a {card3}, for a total of {card2 + card3}.")
            time.sleep(3)
        if card3 == 11:
            print(f"I drew a {card2} and an ace for a score of {11 + card2}")
            time.sleep(3)
        dealerscore = dealerscore + card2 + card3
        if dealerscore == 21:
            print("HA! I win, loser.")
            sys.exit()

        x = input("Hit or stand? ")
        while True:
            if x.lower() == "hit":
                playerscore = playerscore + card4
                print(f"You drew a {card4}. Your score is now {playerscore}")
                time.sleep(3)
                while True:
                    if dealerscore <= 15:
                        dealerscore = dealerscore + card5
                        print("Hit")
                        time.sleep(3)
                        print(f"I drew a {card5}. My score is now {dealerscore}.")
                        time.sleep(3)
                        break
                    if dealerscore > 15:
                        print("Stand")
                        time.sleep(3)
                        print(f" My final score is {dealerscore}")
                        time.sleep(3)
                        break
                if dealerscore > 21:
                    print("Ugh. You win")
                if dealerscore == 21:
                    print("HA! I win, loser.")
                x = input("Hit or stand? ")
                if x.lower() == "hit":
                    playerscore = playerscore + card6
                    print(f"You drew a {card6}. Your score is now {playerscore}")
                    time.sleep(3)
                if playerscore > 21:
                    print("HA! I win, loser.")
                    sys.exit()
                if playerscore == 21:
                    print("Ugh. You win.")
                    sys.exit()
                    while True:
                        if dealerscore <= 15:
                            dealerscore = dealerscore + card5
                            print("Hit")
                            time.sleep(3)
                            print(f"I drew a {card5}. My score is now {dealerscore}.")
                            time.sleep(3)
                            break
                        if dealerscore > 15:
                            print("Stand")
                            time.sleep(3)
                            print(f" My final score is {dealerscore}")
                            time.sleep(3)
                            break
                    if dealerscore > 21:
                        print("Ugh. You win")
                    if dealerscore == 21:
                        print("HA! I win, loser.")
                    if x.lower() == "stand" and dealerscore > 16 and playerscore > dealerscore:
                        print("Ugh. You win.")
                        break
                    if x.lower() == "stand" and dealerscore > 16 and playerscore < dealerscore:
                        print("HA! I win, loser.")
                        break
                    x = input("Hit or stand? ")
                    if x.lower() == "hit":
                        playerscore = playerscore + card8
                        print(f"You drew a {card8}. Your score is now {playerscore}")
                        time.sleep(3)
                    if playerscore > 21:
                        print("HA! I win, loser.")
                        break
                    if playerscore == 21:
                        print("Ugh. You win.")
                        break
                    if playerscore < 21:
                        print("Ugh. You win.")
                        break
                    while True:
                        if dealerscore <= 15:
                            dealerscore = dealerscore + card5
                            print("Hit")
                            time.sleep(3)
                            print(f"I drew a {card5}. My score is now {dealerscore}.")
                            time.sleep(3)
                            break
                        if dealerscore > 15:
                            print("Stand")
                            time.sleep(3)
                            print(f" My final score is {dealerscore}")
                            time.sleep(3)
                            break
                    if dealerscore > 21:
                        print("Ugh. You win")
                    if dealerscore == 21:
                        print("HA! I win, loser.")
                    if x.lower() == "stand" and dealerscore > 16 and playerscore > dealerscore:
                        print("Ugh. You win.")
                        break
                    if x.lower() == "stand" and dealerscore > 16 and playerscore < dealerscore:
                        print("HA! I win, loser.")
                        break
                break
            elif x.lower() == "stand":
                print(f"Your final score is {playerscore}")
                break
            else:
                print("Try again")
                continue
        if playerscore > 21:
            print("HA! I win, loser.")
            sys.exit()
        if playerscore == 21:
            print("Ugh. You win.")
            sys.exit()
        while True:
            if dealerscore <= 15:
                dealerscore = dealerscore + card5
                print("Hit")
                time.sleep(3)
                print(f"I drew a {card5}. My score is now {dealerscore}.")
                time.sleep(3)
                if dealerscore <= 15:
                    dealerscore = dealerscore + card7
                    print("Hit")
                    time.sleep(3)
                    print(f"I drew a {card7}. My score is now {dealerscore}.")
                    time.sleep(3)
                    if dealerscore <= 15:
                        dealerscore = dealerscore + card9
                        print("Hit")
                        time.sleep(3)
                        print(f"I drew a {card9}. My score is now {dealerscore}.")
                        time.sleep(3)
                    if dealerscore > 15:
                        print("Stand")
                        time.sleep(3)
                        print(f" My final score is {dealerscore}")
                        time.sleep(3)
                    if dealerscore > 21:
                        print("Ugh. You win")
                    if dealerscore == 21:
                        print("HA! I win, loser.")
                    if dealerscore < 21:
                        print("HA! I win, loser")
                        sys.exit()
                    if x.lower() == "stand" and dealerscore > 16 and playerscore > dealerscore:
                        print("Ugh. You win.")
                        sys.exit()
                    if x.lower() == "stand" and dealerscore > 16 and playerscore < dealerscore:
                        print("HA! I win, loser.")
                        sys.exit()
                if dealerscore > 15:
                    print("Stand")
                    time.sleep(3)
                    print(f" My final score is {dealerscore}")
                    time.sleep(3)
                if dealerscore > 21:
                    print("Ugh. You win")
                    sys.exit()
                if dealerscore == 21:
                    print("HA! I win, loser.")
                    sys.exit()
                if x.lower() == "stand" and dealerscore > 16 and playerscore > dealerscore:
                    print("Ugh. You win.")
                    sys.exit()
                if x.lower() == "stand" and dealerscore > 16 and playerscore < dealerscore:
                    print("HA! I win, loser.")
                    sys.exit()
            if dealerscore > 15:
                print("Stand")
                time.sleep(3)
                print(f" My final score is {dealerscore}")
                time.sleep(3)
            if dealerscore > 21:
                print("Ugh. You win")
            if dealerscore == 21:
                print("HA! I win, loser.")
            if x.lower() == "stand" and dealerscore > 16 and playerscore > dealerscore:
                print("Ugh. You win.")
                sys.exit()
            if x.lower() == "stand" and dealerscore > 16 and playerscore < dealerscore:
                print("HA! I win, loser.")
                sys.exit()

        if dealerscore > 21:
                print("Ugh. You win")
        if dealerscore == 21:
                print("HA! I win, loser.")
        if x.lower() == "stand" and dealerscore > 16 and playerscore > dealerscore:
            print("Ugh. You win.")
            sys.exit()
        if x.lower() == "stand" and dealerscore > 16 and playerscore < dealerscore:
            print("HA! I win, loser.")
            sys.exit()

    else:
        print("YES OR NO?")
        continue
