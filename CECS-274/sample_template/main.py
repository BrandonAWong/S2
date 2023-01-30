from Spider import Spider
from Ant import Ant
from Board import Board
import time


def main():
    print("Welcome to Hungry Critter!")
    board = Board()
    choice = input("Choose your critter:\n1 - ANT\n2 - SPIDER\nQ - QUIT\n\nYour selection: ")

    while choice.upper() != 'Q':
        if choice != '1' and choice != '2' and choice.upper() != 'Q':
            print("Invalid selection.  Please try again.")
            choice = input("Choose your critter:\n1 - ANT\n2 - SPIDER\nQ - QUIT.\n\nYour selection: ")
        elif choice.upper() == 'Q':
            print("Not even one round? Okay, goodbye! :(")
        else:
            if choice == '1':
                critter = Ant()
                print(
                    u"\nYou have selected ANT \u1F41C.\nANT moves 1 unit when moving RIGHT/LEFT, but 2 units when "
                    u"moving UP/DOWN.\nLeaf count:",
                    critter.get_leaves())

            elif choice == '2':
                critter = Spider()
                print(
                    u"\nYou have selected SPIDER  \u1F577.\nSPIDER moves 1 unit RIGHT/UP, but 2 units when moving "
                    u"LEFT/DOWN.\nLeaf count:",
                    critter.get_leaves())

            collected_leaf, hit_boundary = board.place_critter(critter)
            if collected_leaf:
                print("Your critter got lucky and collected a leaf at the starting point!\nNew Leaf Count:",
                      critter.get_leaves())
            print("\nLoading game...")
            time.sleep(3)
            board.display(critter)
            break

    if choice.upper() != 'Q':
        print("\nTo play, move your critter so that it collects as many leaves as possible.")
        time.sleep(4)
        print("Your critter can only collect a leaf if it lands on the exact location of the  leaf.")
        time.sleep(4)
        print("Be careful! If your critter touches or crosses a border, it's GAME OVER!\n\t\tLET\'S PLAY!")
        time.sleep(4)
        choice = input("\n\nSelect a direction to move in:\n1 - RIGHT\t2 - LEFT\t3 - UP\t4 - DOWN\tQ - QUIT\n\nYour "
                       "selection: ")

        while choice.upper() != 'Q':
            if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice.upper() != 'Q':
                print('Invalid selection.  Please try again.')
            else:
                if choice == '1':
                    critter.move_right()
                elif choice == '2':
                    critter.move_left()
                elif choice == '3':
                    critter.move_up()
                elif choice == '4':
                    critter.move_down()

                collected_leaf, hit_boundary = board.place_critter(critter)

                if hit_boundary:
                    print("\n\nYour critter HIT A BOUNDARY!!!\n\nGAME OVER!!!!\n\nFinal score:", critter.get_leaves())
                    choice = 'Q'
                    continue
                if collected_leaf:
                    print("\n\nYour critter COLLECTED A LEAF!!!\nNew Score:", critter.get_leaves(), "\n\n")
                    time.sleep(2)

                board.display(critter)
                print("\nYour critter\'s new position:", str(critter.get_position()), "\nCurrent leaves:",
                      critter.get_leaves())
                choice = input(
                    "\n\nSelect a direction to move in:\n1 - RIGHT\t2 - LEFT\t3 - UP\t4 - DOWN\tQ - QUIT\n\nYour "
                    "selection: ")

        print("\n\nGOODBYE!!!!\n\nFinal score:", critter.get_leaves())
    else:
        print("\n\nGOODBYE!!!")


main()
