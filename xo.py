is_x_turn = True
is_game_on = True
x_score = o_score = 0
current_status = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_status():
    print()
    status = f' {current_status[0]} | {current_status[1]} | {current_status[2]} \n' \
           f'-----------\n' \
           f' {current_status[3]} | {current_status[4]} | {current_status[5]} \n' \
           f'-----------\n' \
           f' {current_status[6]} | {current_status[7]} | {current_status[8]} \n'
    print(status)

def ask_for_input():
    if is_x_turn:
        pick = input("X na redu. Unesi broj polja: ")
    else:
        pick = input("Y na redu. Unesi broj polja: ")
    return pick

def check_input(user_input):
    global is_x_turn

    try:
        input_int = int(user_input)
    except ValueError:
        print("Ups, krivi unos.")
    else:
        if input_int in current_status:
            if is_x_turn:
                current_status[input_int-1] = "X"
            else:
                current_status[input_int-1] = "O"
            is_x_turn = not is_x_turn
        elif input_int > 9 or input_int < 1:
            print(f"Izbor mora biti izmedju 1 i 9")
        else:
            print(f"Pozicija {input_int} vec zauzeta.")

def check_is_there_a_winner():
    if current_status[0] == current_status[1] == current_status[2] or \
        current_status[3] == current_status[4] == current_status[5] or \
        current_status[6] == current_status[7] == current_status[8] or \
        current_status[0] == current_status[4] == current_status[8] or \
        current_status[6] == current_status[4] == current_status[2]:
        # we have winner
        global o_score, x_score
        show_status()

        if is_x_turn:
            o_score = o_score + 1
            print("Imamo pobjednika! 0 is winner")
        else:
            x_score = x_score + 1
            print("Imamo pobjednika! X is winner")
        want_more()
    else:
        # might be a draw..
        # brzo rjesenje. imamo li brojeva u stanju
        for char in current_status:
            if isinstance(char, int):
                # igra se nastavlja
                return
        # ako dodjemo do ovdje, nismo nasli broj u stanju
        print("izjednaceno...")
        show_status()
        want_more()


def want_more():
    global current_status, is_x_turn, o_score, x_score

    if input("\nUpisi jos, ako zelis ponoviti igru: ") == "jos":
        current_status = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("idemo ponovno...\n")
        print(f"Trenutni rezultat je X:{x_score} | O:{o_score}")
    

while is_game_on:
    show_status()
    user_ask = ask_for_input()
    check_input(user_ask)
    check_is_there_a_winner()

    

