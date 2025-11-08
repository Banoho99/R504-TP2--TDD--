import pytest
import crypto

def test_crypt_pas_1_basique():
    # "aZ0!" -> "b!1\"" puis on ajoute "1" à la fin
    assert crypto.crypt("aZ0!", 1) == 'b!1"1'

def test_crypt_pas_1_wrap_et_espace():
    # "Az9 !" -> "BA a\"" puis on ajoute "1"
    assert crypto.crypt("Az9 !", 1) == 'BA a"1'

def test_crypt_pas_3_cas_simples():
    # a->d, A->D, 9->b (9->' '->a->b), ' '->c ; puis on ajoute "3"
    assert crypto.crypt("aA9 ", 3) == "dDbc3"

def test_crypt_pas_invalide_0_ou_10():
    with pytest.raises(ValueError):
        crypto.crypt("abc", 0)
    with pytest.raises(ValueError):
        crypto.crypt("abc", 10)

def test_crypt_pas_non_entier():
    with pytest.raises(TypeError):
        crypto.crypt("abc", "2")
