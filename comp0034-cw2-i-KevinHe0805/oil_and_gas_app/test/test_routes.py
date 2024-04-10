def test_index_success(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/'
    THEN the status code should be 200
    AND the page should contain the the html <title>Iris Home</title>"
    """

    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Homepage" in response.data


def test_prediction_when_form_submitted(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP POST request is made to '/' with form data
    THEN the page should return a prediction result with the test "Predicted Iris type"
    AND the status code should be 200 OK
    """
    form_data = {
        "year": 2002,
        "month": 8,
        "day": 5,
        "type": 1,
    }
    response = test_client.post("/predict", data=form_data)
    assert response.status_code == 200
    assert b"Predicted price at selected day:" in response.data


def test_error_when_register_form_confirm_password_not_valid(test_client):

    form_data = {"email": "kevin@qq.com", "password": "secret", "confirm_password": "496"}
    response = test_client.post("/register", data=form_data)
    assert response.status_code == 200
    assert "Field must be equal to password." in response.data.decode()


def test_login_successful(test_client):

    form_data = {'email': 'test123@example.com', 'password': 'test456'}
    response = test_client.post('/login', data=form_data, follow_redirects=True)
    assert response.status_code == 200
    print(response.data)
    assert b'Login Successful.' in response.data


def test_logout(test_client):

    form_data = {'email': 'test321@example.com', 'password': 'test654'}
    response = test_client.post('/login', data=form_data, follow_redirects=True)
    assert response.status_code == 200

    # Logout the user
    response = test_client.get('/logout', follow_redirects=True)

    assert response.status_code == 200
    assert b'You have been logged out' in response.data


def test_dash_accessible_when_logged_in(test_client):

    form_data = {'email': 'test123@example.com', 'password': 'test456'}
    test_client.post('/login', data=form_data, follow_redirects=True)
    response = test_client.get('/dashboard/')
    assert response.status_code == 200


def test_error404_handler(test_client):

    response = test_client.get("/Kevinhe")
    assert response.status_code == 404
    assert b"Oops! Page Not Found!" in response.data
