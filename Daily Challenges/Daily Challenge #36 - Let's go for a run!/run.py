def running_pace(distance, time):
    time = time.split(":")
    time = int(time[0]) + (int(time[1]) / 60)

    pace = distance / time
    pace = round(pace, 3)
    pace = str(pace)
    pace = pace.split(".")
    pace[1] = round(int(pace[1]) * 0.6)


    return f'{pace[0]}:{pace[1]}'


if __name__ == "__main__":
    print(running_pace(6, "5:26"))