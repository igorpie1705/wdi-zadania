from math import sqrt


def algorytm():
    result = sqrt(0.5)
    last_element = result
    for i in range(10000):
        last_element = sqrt(0.5 + last_element * 0.5)
        new_result = result * last_element
        result = new_result
    return 2/result


print(algorytm())
