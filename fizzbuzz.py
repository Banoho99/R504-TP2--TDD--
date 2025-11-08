def affiche(n=100):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FrisBee")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return "".join(result)
