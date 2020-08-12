def likes(people):
    """F***book simulator.

    Returns list of people that liked post.
    """
    if len(people) > 3:
        return f'{people[0]}, {people[1]} and {len(people) - 2} others like this'
    elif len(people) == 3:
        return f'{people[0]}, {people[1]} and {people[2]} like this'
    elif len(people) == 2:
        return f'{people[0]} and {people[1]} like this'
    elif len(people) == 1:
        return f'{people[0]} likes this'
    else:
        return f'no one likes this'


if __name__ == "__main__":
    print(likes(["John", "Cezary", "Matt", "Ross", "Monica"]))