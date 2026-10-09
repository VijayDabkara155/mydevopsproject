from app.app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"DevOps Task Manager" in response.data


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={"title": "Learn Terraform"},
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Learn Terraform"
    assert data["status"] == "pending"


def test_create_task_without_title():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "title is required"}
