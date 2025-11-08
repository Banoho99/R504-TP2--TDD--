import crypto

def test_crypt_decalage_1_basique():
    # Table: ascii_letters + ascii_punctuation + ascii_digits + " "
    # "aZ0!" -> "b!1\"" (a->b, Z->!, 0->1, !->")
    assert crypto.crypt("aZ0!") == 'b!1"'

def test_crypt_avec_espace_et_wrap():
    # "Az9 !" -> "BA a\"" (A->B, z->A, 9->(espace), (espace)->a, !->")
    assert crypto.crypt("Az9 !") == 'BA a"'

