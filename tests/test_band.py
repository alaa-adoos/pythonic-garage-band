import pytest

from pythonic_garage_band.band import (
   
    Musician,
    Guitarist,
    Drummer,
    Bassist,
   
)


# @pytest.mark.skip("todo")
def test_guitarist_str():
    joan = Guitarist("Joan Jett")
    actual = str(joan)
    expected = "My name is Joan Jett and I play guitar"
    assert actual == expected

# @pytest.mark.skip("todo")
def test_guitarist_repr():
    joan = Guitarist("Joan Jett")
    actual = repr(joan)
    expected = "Guitarist instance. Name = Joan Jett"
    assert actual == expected

# @pytest.mark.skip("todo")
def test_drummer_str():
    sheila = Drummer("Sheila E.")
    actual = str(sheila)
    expected = "My name is Sheila E. and I play drums"
    assert actual == expected

#   @pytest.mark.skip("todo")
def test_drummer_repr():
    sheila = Drummer("Sheila E.")
    actual = repr(sheila)
    expected = "Drummer instance. Name = Sheila E."
    assert actual == expected
# @pytest.mark.skip("todo")
def test_bassist_str():
    meshell = Bassist("Meshell Ndegeocello")
    actual = str(meshell)
    expected = "My name is Meshell Ndegeocello and I play bass"
    assert actual == expected


# @pytest.mark.skip("todo")
def test_bassist_repr():
    meshell = Bassist("Meshell Ndegeocello")
    actual = repr(meshell)
    expected = "Bassist instance. Name = Meshell Ndegeocello"
    assert actual == expected
