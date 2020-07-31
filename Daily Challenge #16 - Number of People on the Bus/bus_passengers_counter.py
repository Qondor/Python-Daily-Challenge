import json

def bus_counter(filename: str):
    """Bus passengers counter.

    Counts how many passengers get on/off the bus on each stop and calculate how many stays after the last one.
    """
    passengers = 0
    stop_list = {}
    with open(filename, "r", encoding="utf-8") as f:
        stop_list = json.loads(f.read())
    for a in stop_list:
        if a[-1] == "n":
            passengers += stop_list[a]
        else:
            passengers -= stop_list[a]
    return passengers

if __name__ == "__main__":
    bus_counter("bus_stops.json")