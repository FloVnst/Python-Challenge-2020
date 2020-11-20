# Processing
def chifoumi(player1Moves, player2Moves):
    scoresTable = {
        "pierre": {
            "pierre": 0,    # Manche nulle
            "papier": -1,   # Manche perdue
            "ciseaux": 1    # Manche gagnée
        },
        "papier": {
            "pierre": 1,
            "papier": 0,
            "ciseaux": -1
        },
        "ciseaux": {
            "pierre": -1,
            "papier": 1,
            "ciseaux": 0
        }
    }

    scoreJ1 = 0
    scoreJ2 = 0
    print("hrr")
    for i in range(0, 3):
        scoreCalc = scoresTable[player1Moves[i]][player2Moves[i]]

        if scoreCalc == 0:
            print("Manche {} : Manche nulle.".format(i + 1))
        elif scoreCalc == 1:
            scoreJ1 += 1
            print("Manche {} : Le joueur 1 remporte la manche.".format(i + 1))
        elif scoreCalc == -1:
            scoreJ2 += 1
            print("Manche {} : Le joueur 2 remporte la manche.".format(i + 1))

    if scoreJ1 == scoreJ2:
        print("Fin du jeu : Partie nulle.")
    elif scoreJ1 > scoreJ2:
        print("Fin du jeu : Le joueur 1 remporte la partie.")
    else:
        print("Fin du jeu : Le joueur 2 remporte la partie.")


# Unit Tests API Input
# chifoumi(lines[0], lines[1])


# Tests

chifoumi(["papier", "papier", "ciseaux"], ["papier", "ciseaux", "ciseaux"])
# Must return :
# Manche 1 : Manche nulle.
# Manche 2 : Le joueur 2 remporte la manche.
# Manche 3 : Manche nulle.
# Fin du jeu : Le joueur 2 remporte la partie.

chifoumi(["ciseaux", "pierre", "ciseaux"], ["papier", "ciseaux", "pierre"])
# Must return :
# Manche 1 : Le joueur 1 remporte la manche.
# Manche 2 : Le joueur 1 remporte la manche.
# Manche 3 : Le joueur 2 remporte la manche.
# Fin du jeu : Le joueur 1 remporte la partie.

chifoumi(["pierre", "papier", "ciseaux"], ["pierre", "ciseaux", "papier"])
# Must return :
# Manche 1 : Manche nulle.
# Manche 2 : Le joueur 2 remporte la manche.
# Manche 3 : Le joueur 1 remporte la manche.
# Fin du jeu : Partie nulle.

chifoumi(["papier", "papier", "ciseaux"], ["pierre", "ciseaux", "papier"])
# Must return :
# Manche 1 : Le joueur 1 remporte la manche.
# Manche 2 : Le joueur 2 remporte la manche.
# Manche 3 : Le joueur 1 remporte la manche.
# Fin du jeu : Le joueur 1 remporte la partie.

chifoumi(["papier", "papier", "pierre"], ["pierre", "ciseaux", "papier"])
# Must return :
# Manche 1 : Le joueur 1 remporte la manche.
# Manche 2 : Le joueur 2 remporte la manche.
# Manche 3 : Le joueur 2 remporte la manche.
# Fin du jeu : Le joueur 2 remporte la partie.
