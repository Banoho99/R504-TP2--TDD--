import fizzbuzz

def test_affiche_sans_parametre():
    result = fizzbuzz.affiche()
    assert result.startswith("12Fizz4Buzz"), "Le début du résultat est incorrect"

