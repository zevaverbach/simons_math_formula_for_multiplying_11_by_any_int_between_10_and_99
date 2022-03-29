
def simons_11_times_formula(num: int) -> int:
    if num < 10 or num > 99:
        raise Exception("number must be between 10 and 99")
    string_of_num_twice = f"{num}{num}"
    first, second, third, fourth = string_of_num_twice
    second_int = int(second)
    third_int = int(third)
    sum_of_middle_nums = second_int + third_int
    return int(f"{first}{sum_of_middle_nums}{fourth}")

ten_to_99 = list(range(10, 100))
for num in ten_to_99:
    print(num, simons_11_times_formula(num))
