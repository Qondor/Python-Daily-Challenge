def boardgame_fight(attacker, defender):
    """Boardgame Fight Resolver.

    Engage in simulation of real life combat. Fighter with bigger number wins and Cavalry wins wih Archers, if numbers are not realated then attackers always win.
    """

    fighters = {
        "Archers" : 3,
        "Swordsmen" : 2,
        "Pikemen" : 1,
        "Cavalry" : 0
    }

    key_list = list(fighters.keys())
    val_list = list(fighters.values())
    
    if fighters[attacker] - fighters[defender] == 3 or fighters[attacker] - fighters[defender] == -3:
        return "Cavalry"
    elif fighters[attacker] - fighters[defender] == 1 or fighters[attacker] - fighters[defender] == -1:
        return key_list[val_list.index(max(fighters[attacker], fighters[defender]))]
    else:
        return attacker

if __name__ == "__main__":
    print(boardgame_fight("Archers", "Cavalry"))
