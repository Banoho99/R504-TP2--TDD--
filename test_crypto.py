import pytest
import crypto

def test_decrypt_exemples_pas_1():
    assert crypto.decrypt('b!1"1') == "aZ0!"
    assert crypto.decrypt('BA a"1') == "Az9 !"

def test_decrypt_exemple_pas_3():
    assert crypto.decrypt("dDbc3") == "aA9 "

def test_decrypt_inverse_de_crypt():
    m = "Hello, World! 9Zz"
    for p in range(1, 10):
        c = crypto.crypt(m, p)
        assert crypto.decrypt(c) == m

def test_decrypt_suffix_invalide():
    with pytest.raises(ValueError):
        crypto.decrypt("abc0")   # pas=0 interdit
    with pytest.raises(ValueError):
        crypto.decrypt("abcX")   # pas non numérique
    with pytest.raises(ValueError):
        crypto.decrypt("abc10")  # pas>9 non supporté (suffixe doit être 1 chiffre)

def test_decrypt_caractere_non_supporte():
    # Introduit un caractère non présent dans TABLE (ex: '€')
    with pytest.raises(ValueError):
        crypto.decrypt("€1")
