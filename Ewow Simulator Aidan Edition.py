import random

class Contestant():
    def __init__(self, num):
        self.name = "Contestant #" + str(num)
        self.lives = 3

    def loseLife(self):
        self.lives -= 1

    def gainLife(self):
        self.lives += 1

while True:
    print("type a number of contestants")
    try:
        contestants = int(input())
        if contestants <= 1:
            print("Not enough contestants")
        else:
            break
    except ValueError:
        print("Not a number")

contestantList = []
deadList = []
notSubmittedMax = .5
notSubmittedMin = .3

for i in range(contestants):
    contestantList.append(Contestant(i))

lives = {}
count = 1
while True:
    print("Round #" + str(count))
    submitted = list(contestantList)
    if count != 1:
        notSubmitted = random.uniform(notSubmittedMin,notSubmittedMax)
        numNotSubmitted = int(notSubmitted * len(contestantList))
        print("Not Submitted: " + str(numNotSubmitted))
        for i in range(numNotSubmitted):
            remove = submitted[random.randint(0,len(submitted)-1)]
            remove.loseLife()
            submitted.remove(remove)

            if remove.lives <= 0:
                contestantList.remove(remove)
                deadList.append(remove)
        notSubmittedMax -= 0.05
        notSubmittedMin -= 0.2

        if notSubmittedMax <= notSubmittedMin:
            notSubmittedMin -= 0.5

        if notSubmittedMin <= 0.05:
            notSubmittedMin = 0.05
        if notSubmittedMax <= 0.1:
            notSubmittedMax = 0.1

    #50% Death
    fifty = int(.5 * len(submitted))
    half = int(.05 * len(submitted))

    #print(len(submitted))
    for i in range(fifty):
        stab = submitted[random.randint(0,len(submitted)-1)]
        stab.loseLife()
        submitted.remove(stab)

        if stab.lives <= 0:
            contestantList.remove(stab)
            deadList.append(stab)

    #5% Extra Life
    for i in range(half):
        gain = submitted[random.randint(0, len(submitted)-1)]
        gain.gainLife()
        submitted.remove(gain)

    print("Contestants Alive: " + str(len(contestantList)))

    if len(contestantList) == 1:
        print("WINNER IS: " + contestantList[0].name)
        break
    
    keys = []
    
    for c in contestantList:
        if c.lives in keys:
            lives[c.lives] += 1
        else:
            lives[c.lives] = 1
            keys.append(c.lives)

    keys.sort()
    
    if len(deadList) > 0:
        print("0:" + str(int(len(deadList) / (len(contestantList) + len(deadList))* 100)) + "%", end=" ")

    for k in keys:
        print(str(k) + ":" + str(int(lives[k] / (len(contestantList) + len(deadList)) * 100)) + "%", end=" ")
        
    count += 1
    print()

    if len(deadList) > 0:
        print("0:" + str(len(deadList)), end = " ")

    for k in keys:
        print(str(k) + ":" + str(lives[k]), end = " ")
    print()
    print()

if len(deadList) >= 99:
    rank = 99
else:
    rank = len(deadList)
    
for i in range(rank):
    print(str(rank - i + 1) + ". " + deadList[len(deadList) - rank + i].name)


