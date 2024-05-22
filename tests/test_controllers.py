from app.controllers.taxi import *
from flask import json
import requests


def test_get_taxis():
    url = 'https://run.mocky.io/v3/2268ee9a-cd4d-4efb-b916-04de79127b4d'
    response = requests.get(url)

    #Verify status code
    assert response.status_code == 200

    #Verify content-type
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8'
    
    #Verify response structure (id and plate)
    taxis = response.json()
    assert isinstance(taxis, list)
    for taxi in taxis:
        assert isinstance(taxi, dict)
        assert "id" in taxi
        assert "plate" in taxi