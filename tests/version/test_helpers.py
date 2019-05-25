from poetry.version.helpers import format_python_constraint
from poetry.semver import parse_constraint


def test_format_python_constraint():
    constraint = parse_constraint("~2.7 || ^3.6")

    result = format_python_constraint(constraint)

    assert result == ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*"

    constraint = parse_constraint("~=3.4")

    result = format_python_constraint(constraint)

    assert result == ">=3.4,<4.0"


def test_format_python_constraint_single_version():
    constraint = parse_constraint("3.6")

    result = format_python_constraint(constraint)

    assert result == ">=3.6,<3.7"

    constraint = parse_constraint("3")

    result = format_python_constraint(constraint)

    assert result == ">=3.0,<4.0"
