import random
def game():
    print("Youn are playing game")
    score = random.randint(1,62)
    with open("hiscore.txt", "w") as f:
        hiscore = f.read()
        if(hiscore != " "):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        print(f"your score : {score}")
        if(score>hiscore):
            with open("hiscrore.txt", "w") as f:
                f.write(str(score))
                return score
game()                      