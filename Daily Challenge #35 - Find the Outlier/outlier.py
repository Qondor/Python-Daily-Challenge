def find_outlier(input_list):
    even_counter = 0
    even_outlier = 0
    odd_outlier = 0
    x = 0
    while x < len(input_list):
        if input_list[x] % 2 == 0:
            even_counter += 0
            even_outlier = x
        else:
            odd_outlier = x
        x += 1
    if even_counter > 0:
        return input_list[odd_outlier]
    else:
        return input_list[even_outlier]

if __name__ == "__main__":
    print(find_outlier([3, 3, 9, 12, 17, 23, 21]))