
def test_home(client):
    response = client.get('/')
    expected_data = {"messsage":"Welcome to Homepage"}
    assert response.json == expected_data
