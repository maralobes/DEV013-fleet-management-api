from app.controllers.taxi import *
from flask import request, json


def test_get_taxis_by_correct_params():
    url = 'https://run.mocky.io/v3/4f0ce8bf-5e2c-431c-a645-cf5a38a252b2'
    response = request.get(url)

    #Verify status code
    assert response.status_code == 200

    #Verify content-type
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8'
    
    #Verify response structure (id and plate)
    taxis = response.json()
    assert response.s