def friends_list(guests):
    """Guest list sorter.

    Sorts list of friends by last name, if 2 or more people have the same last name, then they are sort by first name.
    """
    result = []
    guests = guests.split(";")
    for guest in guests:
        guest = guest.split(":")
        guest.reverse()
        name = guest[0].upper()
        lastname = guest[1].upper()
        result.append(f'({name}, {lastname})')
    result.sort()
    return result

if __name__ == "__main__":
    print(friends_list("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))