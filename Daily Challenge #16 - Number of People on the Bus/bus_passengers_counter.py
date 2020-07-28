import json

def bus_counter(filename: str):
    """Bus passengers counter.

    Counts how many passengers get on/off the bus on each stop and calculate how many stays after the last one.
    """
    stop_list = ()
    with open(filename, "r", encoding="utf-8") as f:
        stop_list = json.loads(f.read())
    # return stop_list
    print(stop_list)

if __name__ == "__main__":
    print(bus_counter("bus_stops.json"))