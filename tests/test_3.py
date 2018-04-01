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
        {'player': 'yellow', 'dir': 'W'}],
        {'red': [(2,3),'LIVE','axe',3,1],
        'blue': [(7,0),'LIVE',None,1,1],
        'green': [(7,7),'LIVE',None,1,1],
        'yellow': [(2,4),'LIVE','dagger',2,1],
        'magic_staff': [(5,2),False],
        'helmet': [(5,5),False],
        'dagger': [(2,4),True],
        'axe': [(2,3),True] })
    ]
)
def test_is_equal(moves, expected):
    """Test if red player gets the axe as expected
        and yellow player gets the dagger
    """
    actual = update_state(moves)
    assert actual == expected
