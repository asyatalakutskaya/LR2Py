import random
from dll.warrior import Warrior

def main():
    
    warriors = [
        Warrior("W1"),
        Warrior("W2")
    ]
    while(warriors[0].status and warriors[1].status):
        r = int(random.uniform(0, 2))
        if(r==0):
            warriors[0].attack()
            warriors[1].damage()
            print(warriors[0].info(),warriors[1].info(),sep=" <-> ")           
        else:
            warriors[1].attack()
            warriors[0].damage()
            print(warriors[0].info(),warriors[1].info(),sep=" <-> ")           

    if(warriors[0].status):
        print(f"Победил {warriors[0].name}")
    else:
        print(f"Победил {warriors[1].name}")

if __name__ == "__main__":
    main()