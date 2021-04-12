

from random import randint

    
def drawcards():
    num1 = randint(2,14)
    num2 = randint(2,14)
    if num1 > num2:
        return num1,num2
    else:
        return num2,num1
    
def card2str(card):
    if 2 <= card <=10:
        return str(card)
    elif card == 11:
        return "J"
    elif card == 12:
        return "Q"
    elif card == 13:
        return "K"
    elif card == 14:
        return "A"
   


def printhand(pccard_1,pccard_2,player):
     print(f"[{pccard_1} [{pccard_2}]" + player +"Cards")
    
def printoutcome(p1, p2, c1, c2):
    win = "YOU WIN!"
    lose = "YOU LOSE!"
    tie = "IT'S A TIE!"
    if p1 == p2 and c1 == c2:
        if p1 > c1:
            print(win)
        elif c1 > p1:
            print(lose)
        else:
            print(tie)
    elif p1 == p2 and c1 != c2:
        print(win)
    elif p1 != p2 and c1 == c2:
        print(lose)
    elif p1 != p2 and c1 != c2:
        if p1 > c1:
            print(win)
        elif c1 > p1:
            print(lose)
        elif p1 == c1:
            if p2 > c2:
                print(win)
            elif c2 > p2:
                print(lose)
            else:
                print(tie)
def main():
    a = "Y"
    print("\n** EECS1015 --AMAZING TWO CARD POKER GAME **\n")
    while a == "Y" or a == "y":
         pcard1, pcard2 = drawcards()
         ccard1, ccard2 = drawcards()
         print("[{0}] [{1}] Your Cards\n[{2}] [{3}] Computer's Cards\n".format(card2str(pcard1), card2str(pcard2), card2str(ccard1), card2str(ccard2)))
         printoutcome(pcard1, pcard2, ccard1, ccard2)
         a = input("\nWant to play again? (Y/N):")
    print("\n** Thank you for playing! **\n")
        
if __name__ == "__main__":
    main() 




