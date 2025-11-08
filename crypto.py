import string

# Table conseillée par l'énoncé
TABLE = string.ascii_letters + string.ascii_punctuation + string.ascii_digits + " "
_INDEX = {ch: i for i, ch in enumerate(TABLE)}
_N = len(TABLE)

def crypt(message: str, pas: int) -> str:
    """
    Chiffre `message` en décalant chaque caractère de `pas` positions dans TABLE,
    puis concatène le chiffre `pas` à la fin du résultat.
    Contraintes : pas est un entier entre 1 et 9 inclus.
    """
    if not isinstance(pas, int):
        raise TypeError("`pas` doit être un entier")
    if pas < 1 or pas > 9:
        raise ValueError("`pas` doit être compris entre 1 et 9 inclus")

    out = []
    for ch in message:
        if ch not in _INDEX:
            raise ValueError(f"Caractère non supporté: {repr(ch)}")
        out.append(TABLE[(_INDEX[ch] + pas) % _N])

    return "".join(out) + str(pas)

def decrypt(message: str) -> str:
    """
    Déchiffre un message produit par `crypt(message, pas)`.
    Le dernier caractère du message chiffré est le pas (un chiffre entre 1 et 9).
    """
    if not message:
        raise ValueError("Message vide")

    pas_char = message[-1]
    if pas_char not in "123456789":
        raise ValueError("Suffixe invalide: `pas` doit être un chiffre entre 1 et 9")
    pas = int(pas_char)

    cipher = message[:-1]
    out = []
    for ch in cipher:
        if ch not in _INDEX:
            raise ValueError(f"Caractère non supporté: {repr(ch)}")
        out.append(TABLE[(_INDEX[ch] - pas) % _N])

    return "".join(out)
