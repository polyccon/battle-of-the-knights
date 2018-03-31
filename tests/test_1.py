import pytest

from src.game import update_state

@pytest.mark.parametrize(
    ("moves", "expected"),
    [
        ([{'player': 'red', 'dir': 'S'},
        {'player': 'red', 'dir': 'S'},
        {'player': 'red', 'dir': 'E'},
        {'player': 'red', 'dir': 'E'}],
        {
            'red': [(2,2),'LIVE','axe',3,1],
            'blue': [(7, 0), 'LIVE', None, 1,1],
            'green': [(7,7),'LIVE',None,1,1],
            'yellow': [(0, 7), 'LIVE', None, 1, 1],
            'magic_staff': [(5,2),False],
            'helmet': [(5,5),False],
            'dagger': [(2,5),False],
            'axe': [(2,2),True],
        })
    ]
)
def test_is_equal(moves, expected):
    """Test if red player gets the axe as expected
    """
    actual = update_state(moves)
    assert actual == expected
