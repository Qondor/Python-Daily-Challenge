def time_converter(input_seconds):
    """Time converter.

    Converts second to years, days, hours and minutes.
    """

    output_minutes = 0
    output_hours = 0
    output_days = 0
    output_years = 0

    year_in_seconds = 31536000
    day_in_seconds = 86400
    hour_in_seconds = 3600
    minute_in_seconds = 60

    while input_seconds >= year_in_seconds:
        output_years += 1
        input_seconds -= year_in_seconds
    while input_seconds >= day_in_seconds:
        output_days += 1
        input_seconds -= day_in_seconds
    while input_seconds >= hour_in_seconds:
        output_hours += 1
        input_seconds -= hour_in_seconds
    while input_seconds >= minute_in_seconds:
        output_minutes += 1
        input_seconds -= minute_in_seconds

    return f'{output_years} years, {output_days} days, {output_hours} days, {output_minutes} minutes and {input_seconds} seconds' # Small change to the ouptut string, this program always returns all possible time formats even if they are empty

if __name__ == "__main__":
    print(time_converter(62222490))