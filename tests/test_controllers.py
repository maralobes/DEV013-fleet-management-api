from app.controllers.taxi import *


def test_get_taxis_by_correct_params():
    taxis = get_taxis()
    