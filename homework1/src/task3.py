def check_number(value):
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "zero"


def prime():
    result = []
    current = 2

    while len(result) < 10:
        prime_check = True

        for divisor in range(2, current):
            if current % divisor == 0:
                prime_check = False
                break

        if prime_check:
            result.append(current)

        current += 1

    return result




def sum_numbers():
    total = 0
    count = 1

    while count <= 100:
        total += count
        count += 1

    return total
