from my_package1.Greetings import greet


def test_greet():
    result = greet("Areeb")
    assert result == "Good day Areeb"
