from main import calculate_average, find_highest_scorer

def test_calculate_average():
    students= [
        {"ID": "1", "Name": "Abhishek", "Marks": "80"},
        {"ID": "2", "Name": "Rahul", "Marks": "90"},
        {"ID": "3", "Name": "Priya", "Marks": "70"}
    ]
    assert calculate_average(students)==80

def test_find_highest_scorer():
    students = [
        {"ID": "1", "Name": "Abhishek", "Marks": "80"},
        {"ID": "2", "Name": "Rahul", "Marks": "90"},
        {"ID": "3", "Name": "Priya", "Marks": "70"}
    ]
    assert find_highest_scorer(students)=="Rahul"