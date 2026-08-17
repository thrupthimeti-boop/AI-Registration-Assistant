from app import get_intent, check_eligibility


def test_registration_intent():
    assert get_intent("I want to register") == "registration"


def test_eligibility_intent():
    assert get_intent("Am I eligible for this course?") == "eligibility"


def test_course_intent():
    assert get_intent("What courses are available?") == "course_information"


def test_python_eligibility():
    result = check_eligibility("Python", "12th pass")
    assert "eligible" in result.lower()


print("All tests passed!")
