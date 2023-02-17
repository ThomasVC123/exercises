import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    'a',
    'e',
    'i',
    'o',
    'u',
    'aaaa',
    'aeiou',
    'x',
    'y',
    'aebou',
])
def test_function(string):
    function_name = 'only_vowels'
    assert hasattr(student, function_name), f"Missing function {function_name}"

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"