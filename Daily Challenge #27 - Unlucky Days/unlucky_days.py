import calendar

def unlucky_days(year):
    """Friday 13th counter.

    Counts number of Black Fridays in given year.
    """
    friday13th = 0
    cal = calendar.Calendar()
    for month in range(1,13):
        for day, week_day in cal.itermonthdays2(year, month):
            if day == 13 and week_day == 4:
                friday13th += 1
    return friday13th

if __name__ == "__main__":
    print(unlucky_days(2015))