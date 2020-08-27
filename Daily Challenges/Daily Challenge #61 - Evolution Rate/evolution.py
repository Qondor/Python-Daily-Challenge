def evolution_rate(before, after):
    if before == 0 and after == 0:
        return 'No evolution.'
    elif before == 0:
        return f'A positive evolution of {after * 100}%.'
    elif after == 0:
        return f'A negative evolution of {before * 100}%.'
    else:
        result = (after - before) / before * 100

    if result > 0:
        return f'A positive evolution of {(int(result) + 1)}%.'
    elif result < 0:
        return f'A negative evolution of {(int(result) * -1) + 1}%.'
    else:
        return 'No evolution.'

if __name__ == "__main__":
    print(evolution_rate(11.29, 45.79))