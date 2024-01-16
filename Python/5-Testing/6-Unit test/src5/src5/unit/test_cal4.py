from calculator import square

#Use pytest on command line
def test_cal4():

    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0