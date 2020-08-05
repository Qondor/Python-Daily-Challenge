def killMonsters(hp, m, dm):
    """Little monster slayer game.

    Calculates how many times character will get hit and how many HP will be left after fight.
    """
    hits = 0
    received_damage = 0

    if m <= 3:
        return f'hits: 0, damage: 0, health: {hp}'
    else:
        while m > 3: # not "m > 0", because then it would iterate one more time
            m -= 3
            hp -= dm
            hits += 1
            received_damage += dm
            if hp <= 0:
                return "Hero died."
        return f'hits: {hits}, damage: {received_damage}, health: {hp}'

if __name__ == "__main__":
    print(killMonsters(50, 70, 10))