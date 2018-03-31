import pytest

from src.game import update_state

@pytest.mark.parametrize(
    ("moves", "expected"),
    [
        ([{'player': 'red', 'dir': 'S'},
        {'player': 'red', 'dir': 'S'},
        {'player':'blue', 'dir': 'E'},
        {'player': 'green', 'dir': 'N'},
        {'player': 'yellow', 'dir':'N'}],
        {
            'red': [(2,0),'LIVE',None,1,1],
            'blue': [(7, 1), 'LIVE', None, 1, 1],
            'green': [(6,7),'LIVE',None,1,1],
            'yellow': [(-1, 7), 'DROWNED', None, 0, 0],
            'magic_staff': [(5,2),False],
            'helmet': [(5,5),False],
            'dagger': [(2,5),False],
            'axe': [(2,2),False],
        })
    ]
)
def test_is_equal(moves, expected):
    """Test if comparison of moves with
        expected is equal
    """
    actual = update_state(moves)
    assert actual == expected
