from app.app import app as flask_app

def test_health_route():
    client = flask_app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

