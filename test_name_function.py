from name_function import get_formatted_name

# must test function start with 'test_' to pytest see it as a test function 
def test_first_last_name():
    formatted_name = get_formatted_name("jan", "kowalski")
    assert formatted_name == "Jan Kowalski" # returned boolean value

def test_first_last_middle_name():
    formatted_name = get_formatted_name("jan", "kowalski", "janusz")
    assert formatted_name == "Jan Janusz Kowalski"  
    