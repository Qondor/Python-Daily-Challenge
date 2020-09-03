def grade(first, second, third):
    """Grade calculator.

    Takes scores from 3 exams and calculates grade.
    """
    score = round((first + second + third) / 3, 1)
    score_secondary = str(score)
    plusminus = int(score_secondary[1])
    if score > 100:
        return "Wrong input, friend."
    else:
        if score >= 90:
            if plusminus >= 5:
                return "A+"
            else:
                return "A-"
        elif score >= 80:
            if plusminus >= 5:
                return "B+"
            else:
                return "B-"
        elif score >= 70:
            if plusminus >= 5:
                return "C+"
            else:
                return "C-"
        elif score >= 60:
            if plusminus >= 5:
                return "D+"
            else:
                return "D-"
        else:
            return "F"

if __name__ == "__main__":
    print(grade(99, 89, 93))