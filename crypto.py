import string

# Table conseillée par l'énoncé
TABLE = string.ascii_letters + string.ascii_punctuation + string.ascii_digits + " "

def crypt(message: str) -> str:
    """Décale chaque caractère d'un cran dans TABLE (wrap inclus)."""
    out = []
    n = len(TABLE)
    idx = {ch: i for i, ch in enumerate(TABLE)}
    for ch in message:
        if ch not in idx:
            raise ValueError(f"Caractère non supporté: {repr(ch)}")
        out.append(TABLE[(idx[ch] + 1) % n])
    return "".join(out)

