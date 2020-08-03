def time_converter(input_seconds):
    """Time converter.

    Converts second to years, days, hours and minutes.
    """

    output_minutes = 0
    output_hours = 0
    output_days = 0
    output_years = 0

    if input_seconds <= 59:
        return f'{input_seconds} seconds'

    elif input_seconds <= 3599:
        while input_seconds >= 60:
            output_minutes += 1
            input_seconds -= 60
        return f'{output_minutes} minutes and {input_seconds} seconds'

    elif input_seconds <= 86400:
        while input_seconds >= 3600:
            output_hours += 1
            input_seconds -= 3600
        while input_seconds >= 60:
            output_minutes += 1
            input_seconds -= 60
        return f'{output_hours} hours, {output_minutes} minutes and {input_seconds} seconds'

    elif input_seconds <= 31536000:
        while input_seconds >= 86400:
            output_days += 1
            input_seconds -= 86400
        while input_seconds >= 3600:
            output_hours += 1
            input_seconds -= 3600
        while input_seconds >= 60:
            output_minutes += 1
            input_seconds -= 60
        return f'{output_days} days, {output_hours} days, {output_minutes} minutes and {input_seconds} seconds'

    else:
        while input_seconds >= 31536000:
            output_years += 1
            input_seconds -= 31536000
        while input_seconds >= 86400:
            output_days += 1
            input_seconds -= 86400
        while input_seconds >= 3600:
            output_hours += 1
            input_seconds -= 3600
        while input_seconds >= 60:
            output_minutes += 1
            input_seconds -= 60
        return f'{output_years} years, {output_days} days, {output_hours} days, {output_minutes} minutes and {input_seconds} seconds'

if __name__ == "__main__":
    print(time_converter(64920192))