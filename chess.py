import random


def gen_board(br):
    list1 = []
    for i in range(8):
        for j in range(8):
            list1.append(0)
        br.append(list1)
        list1 = []
    return br


def pawn_place(br):
    x1 = random.randrange(0, 8)
    y1 = random.randrange(0, 8)
    if br[x1][y1] == 0:
        br[x1][y1] = 'P'
        list1 = [x1 + 1, y1 + 1]
        pawn.append(list1)
    else:
        pawn_place(br)


def queen_place(br, k):
    while k > 0:
        x2 = random.randrange(0, 8)
        y2 = random.randrange(0, 8)
        if br[x2][y2] == 0:
            br[x2][y2] = 'H'
            list2 = [x2+1, y2+1]
            queen.append(list2)
            k = k-1
        else:
            continue


def check(pawn, queen, k):
        print("Czy pionek zostanie zbity przez któregoś z hetmanow?")
        checking = 0
        for i in range(0, k):
            for j in range(0, 2):
                if pawn[0][0] == queen[i][0]:
                    checking = 1
                    list = [queen[i][j], queen[i][j + 1]]
                    print("Hetman, ktory zbija w poziomie", list)
                    break
                elif pawn[0][1] == queen[i][1]:
                    checking = 1
                    list = [queen[i][j], queen[i][j + 1]]
                    print("Hetman, ktory zbija w pionie", list)
                    break
        for i in range(0, k):
            I, J = pawn[0][0], pawn[0][1]
            P, Q = queen[i][0], queen[i][1]
            if P - Q == I - J or P + Q == I + J:
                checking = 1
                list = [P, Q]
                print("Hetman, ktory zbija po skosie:", list)
        if checking == 1:
            print("Tak, pionek może być zbity przez powyższych hetmanów.")
        else:
            print("Nie.")


def show_board(br):
    for y in range(0, len(br)):
        for x in range(0, len(br[y])):
            print(br[y][x], end=" ")
        print(" \r")


def questions(k):
    z = 0
    while z != 5:
        z = int(input('''Co robimy dalej?
        1. Losowanie nowej pozycji pionka
        2. Usuwanie danego hetmana
        3. Ponowna weryfikacja bić
        4. Pokaż aktualne ułożenie pola gry
        5. Wyjdź
        '''))
        if z == 5:
            break
        elif z == 4:
            show_board(board)
        elif z == 3:
            check(pawn, queen, k)
        elif z == 2:

            x3 = int(input("Podaj nr. wiersza : "))
            y3 = int(input("Podaj nr. kolumny: "))
            list3 = [x3, y3]
            print(list3)
            for i in range(0, 5):
                if list3 == queen[i]:
                    del (queen[i])
                    print("Hetmani po usunieciu: ", queen)
                    board[x3 - 1][y3 - 1] = 0
                    k = k - 1
                    break
                elif list3 == pawn[0]:
                    print("Nie usuwamy pionka!")
                    break
                elif board[x3 - 1][y3 - 1] == 0:
                    print("W tym miejscu nic nie ma.")
                    break
        elif z == 1:
            board[pawn[0][0] - 1][pawn[0][1] - 1] = 0
            del (pawn[0])
            pawn_place(board)
            print("Pozycja pionka zostala zmieniona!")


k = random.randrange(0,6)
board = []
pawn = []
queen = []

gen_board(board)
pawn_place(board)

print("Ilość hetmanów na mapie:", k)
print("Pozycja pionka:", pawn)

if k != 0:
    queen_place(board, k)
    print("Pozycje hetmanów:", queen)
    show_board(board)
    check(pawn, queen, k)
else:
    print("Brak hetmanów")
questions(k)

