from adventure.story import step
import pytest

@pytest.mark.parametrize(
    # fmt: off
    "input_str, expected_output",
    [
        ('right', 'right'),
        ('left', 'left'),
        ('hello', 'still'),
    ],
    # fmt: on
)
def test_step(input_str, expected_output):
    result = step(input_str, ["event1", "event2"])
    assert expected_output in result.lower()

