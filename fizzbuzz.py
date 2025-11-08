def _fb_token(i: int) -> str:
    if i % 15 == 0:
        return "FrisBee"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)

def affiche(*args):
    """
    - affiche()        -> concatène 1..100
    - affiche(n)       -> concatène 1..n
    - affiche(n1, n2)  -> concatène n1..n2 (inclus)
    """
    if len(args) == 0:
        start, end = 1, 100
    elif len(args) == 1:
        n = args[0]
        start, end = 1, int(n)
    elif len(args) == 2:
        n1, n2 = args
        start, end = int(n1), int(n2)
        if start > end:
            raise ValueError("affiche(n1, n2): n1 doit être <= n2")
    else:
        raise TypeError("affiche() accepte 0, 1 ou 2 arguments")

    return "".join(_fb_token(i) for i in range(start, end + 1))
