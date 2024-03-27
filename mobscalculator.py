import random
import itertools
from alive_progress import alive_bar

#color definitions
class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

for _ in itertools.count():
    items = 0
    mobs = 0
    tryNumber = 0           # resets these values when the user restarts
    totalMobs = 0
    highest = 0
    lowest = 1000000000

    askNumber = input(f"\n{bcolors.BOLD}how many runs? (higher number = higher accuracy): {bcolors.ENDC}")
    itemNumber = input(f"\n{bcolors.BOLD}how many items do you need?: {bcolors.ENDC}")
    chance = input(f"\n{bcolors.BOLD}What is the chance to get this item? (in percent): {bcolors.ENDC}")
    itemVar1 = input(f"\n{bcolors.BOLD}lower range of items gotten: {bcolors.ENDC}")
    itemVar2 = input(f"{bcolors.BOLD}upper range of items gotten: {bcolors.ENDC}")

    try:
        askNumber = int(askNumber)
        itemNumber = int(itemNumber)
        chance = float(chance)
        chance /= 100                   # chance is divided by 100 because it needs to be a float from 0-1
        itemVar1 = int(itemVar1)
        itemVar2 = int(itemVar2)
    except:
        print(f"\n{bcolors.FAIL}[Input error]\n{bcolors.ENDC}")
        continue

    if askNumber > 50000:
        if input(f"\n{bcolors.WARNING}[are you sure? this is a large number of runs and might take a while!](Y to continue)\n{bcolors.ENDC}") != "Y":
            continue

    if askNumber < 100:
        if input(f"\n{bcolors.WARNING}[are you sure? this is a low number of runs and might not grant an accurate result. 100 runs is the minimum recommended](Y to continue)\n{bcolors.ENDC}") != "Y":
            continue

    with alive_bar(askNumber) as bar:   # makes a progress bar with the amount of asked runs as the goal
        while tryNumber < askNumber:    # while the number of runs is less than the asked number it loops
            if items >= itemNumber:     # if the asked amount of items has been reached (when a run completes)

                if mobs > highest:      # updates the highest and lowest recorded mob counts if the amount is higher/lower on this run
                    highest = mobs
                if mobs < lowest:
                    lowest = mobs
                
                totalMobs += mobs       # adds the mobs from this run to the total for later
                items = 0              # resets the values for the next run and increments the amount of runs completed
                mobs = 0
                tryNumber += 1
                bar()                  # also for the progress bar

            if random.random() < chance:                    # if a random float (0-1) is within the chance set by the user, this will add
                items += random.randint(itemVar1,itemVar2)  # an amount of items within the variation also set by the user

            mobs += 1

    try:
        avgMobs = round(totalMobs / tryNumber, 2)       # calculates the average amount of mobs per run by dividing
    except:                                             # the mobs of every run added together by the amount of runs
        print(f"\n{bcolors.FAIL}[Math error]\n{bcolors.ENDC}")
        continue

    print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}it took {avgMobs} mobs/blocks on average to get {itemNumber} items (lowest recorded: {lowest}, highest recorded: {highest}, total: {totalMobs}){bcolors.ENDC}")
    input(f"{bcolors.BOLD}press enter to continue\n{bcolors.ENDC}")