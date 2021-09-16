import random


def rpg():
    print("--------------------------------------------------\n")

    print("       Bienvenue dans Rapscallion\n")

    print("Rapscallion est un jeu textuel de type RPG")
    print("où le joueur incarne un aventurier qui doit")
    print("traverser un donjon rempli de monstres mais ")
    print("aussi d'esprits bienveillants qui vous aideront\n")

    print("Qui osera relever le défi de Rapscallion ?\n")

    print("--------------------------------------------------\n")

    print("Inconnu : Autrefois j'étais aussi jeune que toi, et j'avais l'ambition ")
    print("de traverser le donjon. Malheureusement je n'ai pas réussi et j'ai été ")
    print("le seul survivant de mon groupe. Tous mes camarades sont morts...")
    print("Penses-tu pouvoir réussir ? On raconte qu'après ce donjon se trouve")
    namePlayer = input("une montagne d'or. Comment t'appelles-tu jeune aventurier ?\n")

    print("\n")
    print("Il y a trois portes qui te permettent d'atteindre la cave. Celle de gauche contient")
    print("le chemin le plus simple, celle du milieu un chemin plus difficile et la dernière")
    print("un chemin impossible à traverser. Bien évidemment plus le chemin est difficile")
    print("plus la récompense est grande.\n")

    hasDif = False

    while not hasDif:
        difficulty = input("Quelle chemin voulez-vous prendre ? Facile, Difficile ou Impossible\n")
        difficulty = difficulty.lower()
        if difficulty == "facile":
            print("Vous comptez prendre le chemin facile\n")
            roomNumber = 7
            hasDif = True
        elif difficulty == "difficile":
            print("Vous comptez prendre le chemin difficile\n")
            roomNumber = 15
            hasDif = True
        elif difficulty == "impossible":
            print("Vous comptez prendre le chemin impossible\n")
            roomNumber = 25
            hasDif = True
        else:
            print("Aucunes portes ne correspondent à ce chemin. Choisissez un chemin valide !")

    print()

    print(f"Inconnu : Et bien tu m'as l'air bien motivé pour traverser ce donjon {namePlayer}.")
    print("Il me reste l'ancien équipement de mes camarades prends celui que tu veux")
    print("et bonne chance à toi à l'intérieur\n")

    print("Devant vous se trouve 3 coffres remplis d'équipement\n")

    print("Le premier renferme un ancien équipement d'un Paladin.")
    print("Il est dit que les paladin ont 22 HP et ont un bonus/malus de 1 à l'intérieur\n")

    print("Le deuxième coffre, dévoile une grande hache de guerre d'un défunt Guerrier")
    print("Il est dit que les mages ont 25 HP et ont un bonus/malus de 2 à l'intérieur\n")

    print("Le dernier coffre renferme un équipement magique parfait pour un Mage")
    print("Il est dit que les guerriers ont 25 HP et ont un bonus/malus de 3 à l'intérieur")

    role = (
        {"nom": "Paladin", "life": 22, "gain": 1, "loss": 1, "scream_war": "Parle la lumière tout sera purifié !"},
        {"nom": "Guerrier", "life": 25, "gain": 2, "loss": 2, "scream_war": "Tout se règle par la force !"},
        {"nom": "Mage", "life": 25, "gain": 3, "loss": 3, "scream_war": "La magie contrôle le monde !"}
    )

    hasRole = False
    while not hasRole:
        print("\n")
        rolePlayer = input("Quel équipement voulez-vous prendre entre le 'Paladin', le 'Guerrier' et le 'Mage' ?\n")
        rolePlayer = rolePlayer.lower()
        if rolePlayer == "paladin":
            print("Vous prenez l'équipement que contient le premier coffre et vous vous préparez à rentrer\n")
            rolePlayer = role[0]
            hasRole = True
        elif rolePlayer == "guerrier":
            print("Vous prenez l'équipement que contient le deuxième coffre et vous vous préparez à rentrer\n")
            rolePlayer = role[1]
            hasRole = True
        elif rolePlayer == "mage":
            print("Vous prenez l'équipement que contient le dernier coffre et vous vous préparez à rentrer\n")
            rolePlayer = role[2]
            hasRole = True
        else:
            print(
                "Vous ne pouvez pas vous permettre de reculer, votre honeur en dépend. Choisissez une classe valide !")

    mob = (
        {"name": "Lamalle", "good_spirit": False, "power": -1},
        {"name": "Sileree", "good_spirit": False, "power": -1},
        {"name": "Penot", "good_spirit": False, "power": -2},
        {"name": "Naja", "good_spirit": False, "power": -2},
        {"name": "Fain", "good_spirit": False, "power": -3},
        {"name": "Uka", "good_spirit": False, "power": -3},
        {"name": "Gara", "good_spirit": False, "power": -4},
        {"name": "Gnor", "good_spirit": False, "power": -4},
        {"name": "Lai", "good_spirit": False, "power": -5},
        {"name": "Lisri", "good_spirit": False, "power": -5},
        {"name": "Massy", "good_spirit": False, "power": -6},
        {"name": "Cuara", "good_spirit": False, "power": -6},
        {"name": "Arbus", "good_spirit": False, "power": -6},
        {"name": "Gos", "good_spirit": True, "power": 1},
        {"name": "Sozeo", "good_spirit": True, "power": 1},
        {"name": "Umidrorn", "good_spirit": True, "power": 2},
        {"name": "Jacabra", "good_spirit": True, "power": 2},
        {"name": "Aityr", "good_spirit": True, "power": 3},
        {"name": "Knane", "good_spirit": True, "power": 3},
        {"name": "Thiananti", "good_spirit": True, "power": 4},
        {"name": "Aukia", "good_spirit": True, "power": 4},
        {"name": "Unmo", "good_spirit": True, "power": 5},
        {"name": "Wolperzi", "good_spirit": True, "power": 5},
        {"name": "Drazei", "good_spirit": True, "power": 6},
        {"name": "Ausec", "good_spirit": True, "power": 6},
    )

    currentRoom = 0

    while currentRoom < roomNumber:
        if rolePlayer["life"] < 1:
            print("Ce monstre était trop fort et la blessure qu'il vous a infligé était mortelle ! Encore un "
                  "aventurier mort dans le donjon")
            return 0
        print("Vous êtes dans la salle n°" + str(currentRoom))
        print(f'Vous avez {rolePlayer["life"]} HP\n')
        print("Deux portes se tiennent devant vous.")
        doorChoose = input("Laquelle souhaitez-vous prendre, celle de gauche ou celle de droite\n")
        doorChoose = doorChoose.lower()
        if doorChoose == "gauche" or doorChoose == "droite":
            k = random.randint(0, 24)
            l = random.randint(0, 24)
            while k == l:
                l = random.randint(0, 24)
            if mob[k]["good_spirit"] == False:
                print(
                    "-------------------------------------------------------------------------------------------\n")
                print(f'Vous entrez dans la pièce et tombez nez à nez contre {mob[k]["name"]}.')
                print(f'Un monstre avec une puissance de {mob[k]["power"] - rolePlayer["loss"]}\n')

                print("Après un combat vous arrivez à le vaincre mais vous êtes touché.\n")
                if mob[l]["good_spirit"] == False:
                    print(f'L`autre pièce renfermait {mob[l]["name"]}.')
                    print(f'Un monstre qui vous aurez enlevé {mob[l]["power"] - rolePlayer["loss"]} HP\n')
                else:
                    print(f'L`autre pièce renfermait {mob[l]["name"]}.')
                    print(f'Un esprit qui vous aurez rendu {mob[l]["power"] + rolePlayer["gain"]} HP\n')
                print(
                    "-------------------------------------------------------------------------------------------\n")

                rolePlayer["life"] += mob[k]["power"] - rolePlayer["loss"]

            else:
                print(
                    "-------------------------------------------------------------------------------------------\n")
                print(f'Vous entrez dans la pièce est vous rencontrez {mob[k]["name"]}.')
                print(f'Un esprit qui vous rend {mob[k]["power"] + rolePlayer["gain"]} HP\n')
                if mob[l]["good_spirit"] == False:
                    print(f'L`autre pièce renfermait {mob[l]["name"]}.')
                    print(f'Un monstre qui vous aurez enlevé {mob[l]["power"] - rolePlayer["loss"]} HP\n')
                else:
                    print(f'L`autre pièce renfermait {mob[l]["name"]}.')
                    print(f'Un esprit qui vous aurez rendu {mob[l]["power"] + rolePlayer["gain"]} HP\n')
                print(
                    "-------------------------------------------------------------------------------------------\n")

                rolePlayer["life"] += mob[k]["power"] + rolePlayer["gain"]

            currentRoom += 1
        else:
            print("Vous ne pouvez plus reculer. Choisissez une porte.")
    print("\n")
    print("Vous avez réussi à traverser le donjon et trouvez une cave remplie d'or, de quoi vivre une vie de roi !")
    print(rolePlayer["scream_war"])
    return 0


rpg()
