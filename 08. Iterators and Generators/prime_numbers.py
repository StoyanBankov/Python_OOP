def get_primes(list_of_ints):
    for number in list_of_ints:
        if number <= 1:
            continue

        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            yield number
