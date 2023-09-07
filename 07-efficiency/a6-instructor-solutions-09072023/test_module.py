import module

# Show both full test mode: pytest -v
# And single test mode: pytest -vk compute_matching_1

def test_compute_matching_1():
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    expected = [True, True, True]
    assert module.compute_matching(lst1, lst2) == expected, \
            "Equal lists should evaluate list of all True vals"

def test_compute_matching_2():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    expected = [False, False, False]
    assert module.compute_matching(lst1, lst2) == expected, \
            "Unequal lists should evaluate list of all False vals"

def test_compute_matching_3():
    lst1 = ["a", "b"]
    lst2 = ["a", "B"]
    expected = [True, False]
    assert module.compute_matching(lst1, lst2) == expected, \
            "Should work for strings of different case too"

def test_compute_matching_indices_1():
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    assert module.compute_matching_indices(lst1, lst2) == [0, 1, 2]

def test_compute_matching_indices_2():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    assert module.compute_matching_indices(lst1, lst2) == []

def test_compute_matching_indices_3():
    lst1 = []
    lst2 = []
    assert module.compute_matching_indices(lst1, lst2) == []

def test_lowest_temperature_1():
   data = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
           ["20081114", "Detroit", "45.2", "30.3", "33.4"]]
   assert module.lowest_temperature(data, "20081114") == "Chicago"

def test_lowest_temperature_2():
   data = [["20081114", "Chicago", "50.1", "30.0", "35.7"]]
   assert module.lowest_temperature(data, "20081114") == "Chicago"

def test_lowest_temperature_3():
   data = [["20081114", "Chicago", "50.1", "30.0", "35.7"]]
   assert module.lowest_temperature(data, "20081115") == ""

# Run same tests on Copilot generated function from A5, Q3:

def test_copilot_1():
   data = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
           ["20081114", "Detroit", "45.2", "30.3", "33.4"]]
   assert module.lowest_temperature_alt_1(data, "20081114") == "Chicago"
   assert module.lowest_temperature_alt_2(data, "20081114") == "Chicago"
   assert module.lowest_temperature_alt_3(data, "20081114") == "Chicago"

def test_copilot_2():
   data = [["20081114", "Chicago", "50.1", "30.0", "35.7"]]
   assert module.lowest_temperature_alt_1(data, "20081114") == "Chicago"
   assert module.lowest_temperature_alt_2(data, "20081114") == "Chicago"
   assert module.lowest_temperature_alt_3(data, "20081114") == "Chicago"


def test_copilot_3():
   data = [["20081114", "Chicago", "50.1", "30.0", "35.7"]]
   assert module.lowest_temperature_alt_1(data, "20081115") == ""
   assert module.lowest_temperature_alt_2(data, "20081115") == ""
   assert module.lowest_temperature_alt_3(data, "20081115") == ""
