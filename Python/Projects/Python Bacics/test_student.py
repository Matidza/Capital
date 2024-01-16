import pytest
from Student_Card import Student  # Replace 'your_module_name' with the actual module name where your Student class is defined

def test_create_student():
    student = Student("John", "Doe", 43243029, "Computer Science", ["Python", "Java"], "Main Campus")
    assert student.name == "John"
    assert student.surname == "Doe"
    assert student.code == 43243029
    assert student.degree == "Computer Science"
    assert student.skills == ["Python", "Java"]
    assert student.campus == "Main Campus"

def test_invalid_name_type():
    with pytest.raises(TypeError, match="Names/Surnames must be in letters"):
        student = Student(123, "Doe", 43243029, "Computer Science", ["Python", "Java"], "Main Campus")

def test_invalid_surname_type():
    with pytest.raises(TypeError, match="Names/Surnames must be in letters"):
        student = Student("John", 123, 43243029, "Computer Science", ["Python", "Java"], "Main Campus")

def test_invalid_code_type():
    with pytest.raises(ValueError, match="Code must be integers."):
        student = Student("John", "Doe", "123", "Computer Science", ["Python", "Java"], "Main Campus")

def test_invalid_degree_type():
    with pytest.raises(TypeError, match="Degree must be in letters!"):
        student = Student("John", "Doe", 43243029, 123, ["Python", "Java"], "Main Campus")

def test_invalid_campus_type():
    with pytest.raises(TypeError, match="Campus must be in letters!"):
        student = Student("John", "Doe", 43243029, "Computer Science", ["Python", "Java"], 123)

def test_get_card():
    # You can use pytest's built-in 'monkeypatch' fixture to mock user input during testing
    with pytest.raises(ValueError, match="invalid literal for int() with base 10: 'NotANumber'"):
        with pytest.MonkeyPatch.context() as m:
            m.setattr('builtins.input', lambda _: "John\nDoe\nComputer Science\nNotANumber\nPython Java\nMain Campus")
            student_card = get_card()
