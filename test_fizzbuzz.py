import fizzbuzz

def test_affiche_intervalle_5_10():
    # affiche(5, 10) -> BuzzFizz78FizzBuzz
    assert fizzbuzz.affiche(5, 10) == "BuzzFizz78FizzBuzz"

def test_affiche_intervalle_10_16():
    # affiche(10, 16) -> Buzz11Fizz1314FrisBee16
    assert fizzbuzz.affiche(10, 16) == "Buzz11Fizz1314FrisBee16"
