from app.controllers.taxi import *
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

def test_get_trajectories():
    url = 'https://run.mocky.io/v3/39e6591e-46d8-441a-a82c-692ba254f7a5'
    response = requests.get(url)

    #Verify status code
    assert response.status_code == 200

    #Verify content-type
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8'
    
    #Verify response structure (id and plate)
    trajectories = response.json()
    assert isinstance(trajectories, list)
    for trajectory in trajectories:
        assert isinstance(trajectory, dict)
        assert "date" in trajectory
        assert "id" in trajectory
        assert "latitude" in trajectory
        assert "longitude" in trajectory
        assert "taxi_id" in trajectory
        
def test_get_latest():
    url = 'https://run.mocky.io/v3/a35a1af7-b4ed-4570-8a51-288c617acc28'
    response = requests.get(url)

    #Verify status code
    assert response.status_code == 200

    #Verify content-type
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8'
    
    #Verify response structure ()
    latest_trajectories = response.json()
    assert isinstance(latest_trajectories, list)
    for latest_trajectory in latest_trajectories:
        assert isinstance(latest_trajectory, dict)
        assert "taxi_id" in latest_trajectory
        assert "plate" in latest_trajectory
        assert "date" in latest_trajectory
        assert "latitude" in latest_trajectory
        assert "longitude" in latest_trajectory
    
def test_taxis_pagination_with_negative_page(client):
    response = client.get('/taxis?page=-1&limit=10')
    assert response.status_code == 400
    assert b"Page and limit must be positive integers." in response.data