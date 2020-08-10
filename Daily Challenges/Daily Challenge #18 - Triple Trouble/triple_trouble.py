def tripledouble(num1, num2):
    """Triple doubler.

    Checks for a number and... just read the decription in txt file please.
    """
    num1 = str(num1)
    num1 = list(num1)
    num2 = str(num2)
    num2 = list(num2)
    first_number = []
    second_number = []
    final = []
    i = 0
    while i < len(num1) - 1:
        if num1[i] == num1[i+1] and num1[i+1] == num1[i+2]:
            first_number.append(num1[i])
            i += 3
        else:
            i += 1
    i = 0
    while i < len(num2) - 1:
        if num2[i] == num2[i+1]:
            second_number.append(num2[i])
            i += 2
        else:
            i += 1
    for first in first_number:
        for second in second_number:
            if first == second:
                final.append(first)

    if final != []:        
        return final
    else:
        return 0
            
if __name__ == "__main__":
    print(tripledouble(11226660009321, 44555060669))