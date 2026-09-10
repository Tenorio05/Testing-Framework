from ScholarshipEligibilityEvaluator import *
import pytest

# CASO [APPROVED]
def test_approved_case():

    result = evaluate_scholarship(
        age = 18,
        gpa = 8.5,
        attendance_rate = 92.0,
        has_required_courses = True,
        disciplinary_record = False
    )

    assert result.status == Status.APPROVED
    assert result.reasons == ["Applicant meets all scholarship requirements."]

# CASO [MANUAL REVIEW]
def test_manual_review_case():

    result = evaluate_scholarship(
        age = 18,
        gpa = 6.5,
        attendance_rate = 97.0,
        has_required_courses = True,
        disciplinary_record = False
    )

    assert result.status == Status.MANUAL_REVIEW
    assert "GPA is in the manual review range." in result.reasons

# CASOS [REJECTED]
def test_rejected_by_attendance_rate():

    result = evaluate_scholarship(
        age = 20,
        gpa = 9.5,
        attendance_rate = 70.0,
        has_required_courses = True,
        disciplinary_record = False
    )

    assert result.status == Status.REJECTED
    assert "Attendance rate is below the minimum required." in result.reasons

def test_rejected_by_required_courses():

    result = evaluate_scholarship(
        age = 22,
        gpa = 8.8,
        attendance_rate = 96.4,
        has_required_courses = False,
        disciplinary_record = False
    )

    assert result.status == Status.REJECTED
    assert "Required courses have not been completed." in result.reasons

def test_rejected_by_disciplinary_record():

    result = evaluate_scholarship(
        age = 18,
        gpa = 9.0,
        attendance_rate = 92.0,
        has_required_courses = True,
        disciplinary_record = True
    )

    assert result.status == Status.REJECTED
    assert "Applicant has a disciplinary record." in result.reasons

# CASOS DE ENTRADA INVÁLIDA
def test_invalid_gpa():

    with pytest.raises(ValueError, match="GPA must be between 0 and 10."):

        evaluate_scholarship(
            age = 18,
            gpa = 11.0,
            attendance_rate = 92.0,
            has_required_courses = True,
            disciplinary_record = False
        )

def test_invalid_attendance_rate():

    with pytest.raises(ValueError, match="Attendance rate must be between 0 and 100."):

        evaluate_scholarship(
            age = 18,
            gpa = 8.5,
            attendance_rate = -2.0,
            has_required_courses = True,
            disciplinary_record = False
        )

# CASOS DE VALOR LIMITE
def test_age_is_15():

    result = evaluate_scholarship(
        age = 15,
        gpa = 10.0,
        attendance_rate = 100.0,
        has_required_courses = True,
        disciplinary_record = False
    )

    assert result.status == Status.REJECTED
    assert "Applicant is younger than the minimum age." in result.reasons

def test_age_is_16():

    result = evaluate_scholarship(
        age = 16,
        gpa = 9.3,
        attendance_rate = 87.6,
        has_required_courses = True,
        disciplinary_record = False
    )

    assert result.status == Status.MANUAL_REVIEW
    assert "Applicant is under 18 and requires manual review." in result.reasons

def test_age_is_17():

    result = evaluate_scholarship(
        age = 17,
        gpa = 7.9,
        attendance_rate = 82.5,
        has_required_courses = True,
        disciplinary_record = False
    )

    assert result.status == Status.MANUAL_REVIEW
    assert "Applicant is under 18 and requires manual review." in result.reasons

def test_age_is_18():

    result = evaluate_scholarship(
        age = 18,
        gpa = 9.1,
        attendance_rate = 95.4,
        has_required_courses = True,
        disciplinary_record = False
    )

    assert result.status == Status.APPROVED
    assert result.reasons == ["Applicant meets all scholarship requirements."]

