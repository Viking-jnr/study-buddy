import pytest
from app.utils import validators

@pytest.mark.parametrize("name", [
    "Victor", "Victor Kasikwa"
])

def test_valid_student_names(name):
    is_valid, error = validators.validate_student_name(name)
    assert is_valid is True

@pytest.mark.parametrize("name", [
    "", "Vk7", "V", "Victor123", "Victor 123"
])

def test_invalid_student_names(name):
    is_valid, error = validators.validate_student_name(name)
    assert is_valid is False

@pytest.mark.parametrize("course", [
    "Computer Science", "BSE"
])

def test_valid_course(course):
    is_valid, error = validators.validate_course(course)
    assert is_valid is True

@pytest.mark.parametrize("course", [
    "", "T"
])

def test_invalid_course(course):
    is_valid, error = validators.validate_course(course)
    assert is_valid is False