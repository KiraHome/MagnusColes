from pymin import create_app


def test_landing_page():
    app = create_app()

    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"kutyaszar" in response.data
