def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

if __name__ == "__main__":
    numbers = [6, 20, 15, 9]

    print(apply_all_func(numbers, max, min))  # Пример с max и min
    print(apply_all_func(numbers, len, sum, sorted))  # Пример с len, sum и sorted

