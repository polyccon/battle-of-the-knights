import pytest

from src.game import update_state

@pytest.mark.parametrize(
    ("moves", "expected"),
    [
        ([ {'player': 'red', 'dir': 'S'},
        {'player': 'red', 'dir': 'S'},
        {'player': 'yellow', 'dir': 'S'},
        {'player': 'yellow', 'dir': 'S'},
        {'player': 'red', 'dir': 'E'},
        {'player': 'red', 'dir': 'E'},
        {'player': 'red', 'dir': 'E'},
        {'player': 'yellow', 'dir': 'W'},
        {'player': 'yellow', 'dir': 'W'},
        {'player': 'yellow', 'dir': 'W'},
        {'player': 'red', 'dir': 'E'}],

        {'red': [(2,4),'LIVE','dagger',5,1],
        'blue': [(7,0),'LIVE',None,1,1],
        'green': [(7,7),'LIVE',None,1,1],
        'yellow': [(2,4),'DEAD',None,0,0],
        'magic_staff': [(5,2),False],
        'helmet': [(5,5),False],
        'dagger': [(2,4),True],
        'axe': [(2,4),False] })
    ]
)
def test_is_equal(moves, expected):
    """Test if red player wins fight as expected
    """
    actual = update_state(moves)
    assert actual == expected
