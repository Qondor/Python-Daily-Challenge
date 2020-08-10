def change_counter(money):
    """

    """

    fifty = 0
    twenty = 0
    ten = 0
    five = 0
    two = 0
    one = 0
    leftovers = 0
    result = ""

    if money % 50 > 0:
        leftovers = money % 50
        fifty += (money - leftovers) / 50
        money = leftovers
        result += f'50 => {fifty} '

    if money % 20 > 0:
        leftovers = money % 20
        twenty += (money - leftovers) / 20
        money = leftovers
        result += f'20 => {twenty} '

    if money % 10 > 0:

        leftovers = money % 10
        ten += (money - leftovers) / 10
        money = leftovers
        result += f'10 => {ten} '

    if money % 5 > 0:
        leftovers = money % 5
        five += (money - leftovers) / 5
        money = leftovers
        result += f'5 => {five} '

    if money % 2 > 0:
        leftovers = money % 5
        two += (money - leftovers) / 2
        money = leftovers
        result += f'2 => {two} '

    if money >= 1:
        result += f'1 => {money}'

    return result

if __name__ == "__main__":
    print(change_counter(231))