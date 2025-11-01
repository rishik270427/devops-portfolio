import app as app_module

def test_health_route():
    app = app_module.app.test_client()
    resp = app.get("/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"
