import pytest

from app.extensions.api import paginate

"""
In order to test behavior of paginate function
"""


def test_paginate_400_initial_default():

    d = paginate(1, 20, 400, list(range(0, 400)))
    print(d["items"])
    print(list(range(0, 20)))
    assert d["items"] == list(range(0, 20))


def test_paginate_400_10th_page():

    d = paginate(10, 20, 400, list(range(0, 400)))
    print(d["items"])
    print(list(range(180, 200)))
    assert d["items"] == list(range(180, 200))


def test_paginate_400_start_0():

    d = paginate(19, 20, 400, list(range(0, 400)), start_page_as_1=False)
    print(d["items"])
    print(list(range(380, 400)))
    assert d["items"] == list(range(380, 400))


def test_paginate_400_start_1():

    d = paginate(20, 20, 400, list(range(0, 400)))
    print(d["items"])
    print(list(range(380, 400)))
    assert d["items"] == list(range(380, 400))


def test_paginate_400_set_start_1_equals_True_and_init_as_pagenumber_as_0():
    """Exception case
    """
    with pytest.raises(Exception, match=r".* starts > 0. *"):
        d = paginate(0, 20, 400, list(range(0, 400)))
