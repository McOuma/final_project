def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_data = {"mesaage":"Were John"}
    assert response.json == expected_data