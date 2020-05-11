#juguemos al gato!


#Tablero
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#Sigue el juego?
game_is_still_going = True

#Quien gana?
winner = None

#A quien le toca?
current_player = "X"

#Muestra el tablero
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Juega al gato
def play_game():

    #Muestra el tablero
    display_board()

    #Mientras haya juego, aplica este loop
    while game_is_still_going:
        #Le da un turno a un jugador arbitrario
        handle_turn(current_player)

        #Revisa si terminó el juego
        check_if_game_over()

        #Le da el turno al siguiente jugador
        flip_player()

        #Termina el juego si tenemos ganador
    if winner == "X" or winner == "O":
        print(winner + " ganó!")
    elif winner == None:
        print("Empate")

# Le entrega el turno a un jugador preelegido
def handle_turn(player):

    print("Le toca a " + player)
    position = input("Elige un lugar del 1 al 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Elige un lugar del 1 al 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Ese lugar ya está ocupado. Elije otra casilla.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #Llama a la variable global
    global winner

    #Revisa lineas horizontales
    row_winner = check_rows()
    #Revisa líneas verticales
    column_winner = check_columns()
    #Revisa líneas diagonales
    diagonal_winner = check_diagonals()
    #Hay ganador?
    if row_winner:
        #Hay ganador
        winner = row_winner
    elif column_winner:
        #Hay ganador
        winner = column_winner
    elif diagonal_winner:
        #Hay ganador
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():

    global game_is_still_going
    #Revisa las líneas
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():

    global game_is_still_going
    #Revisa las columnas
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #Si alguna columna tiene tres iguales, señala ganador
    if column_1 or column_2 or column_3:
        game_is_still_going = False
    #Entrega ganador (X o O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():

    global game_is_still_going
    #Revisa las disgonales
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    #Si alguna diagonal tiene tres iguales, señala ganador
    if diagonals_1 or diagonals_2:
        game_is_still_going = False
    #Entrega ganador (X o O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return

def check_if_tie():
    global game_is_still_going
    if "-" not in board:
        game_is_still_going = False
    return

def flip_player():

    global current_player
    #Cambia de jugador
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()
