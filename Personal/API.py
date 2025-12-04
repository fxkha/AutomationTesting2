import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL

def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_posts(base_url):
    payload = {"title": "My day", "body": "My post body", "user_id": 1}
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["user_id"] == payload["user_id"]
    assert "id" in data  # API normally generates this

import requests

def test_get_keywords():
    key_url = "https://api.thecatapi.com/v1/images/search"
    auth_key = "live_VXvXbIFX5N91gctqYgG7qDfneVDlS96ODxNpmyZYUXnbsCKUhkBRLoUlZLi82wuR"
    headers = {"x-api-key": auth_key}   # Cat API expects x-api-key, not Bearer

    response = requests.get(key_url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_keywords():
    key_url = "https://api.thecatapi.com/v1/votes"
    auth_key = "live_VXvXbIFX5N91gctqYgG7qDfneVDlS96ODxNpmyZYUXnbsCKUhkBRLoUlZLi82wuR"
    headers = {"x-api-key": auth_key}
    payload = {
        "image_id": "100",  # must match what you want to assert
        "sub_id": "212",  # your custom user/session ID
        "value": -2  # vote value (-1, 0, 1 usually)
    }
    response = requests.post(key_url, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["image_id"] == "100"
    assert data["sub_id"] == "212"
    assert data["value"] == -2


def test_get_post_keywords():
    key_url = "https://api.thecatapi.com/v1/images/search"
    auth_key = "live_VXvXbIFX5N91gctqYgG7qDfneVDlS96ODxNpmyZYUXnbsCKUhkBRLoUlZLi82wuR"  # your real API key
    headers = {"x-api-key": auth_key}   # ✅ use the API key, not the URL

    response = requests.get(key_url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_post_keywords():
    key_url = "https://api.thecatapi.com/v1/votes"
    auth_key = "live_VXvXbIFX5N91gctqYgG7qDfneVDlS96ODxNpmyZYUXnbsCKUhkBRLoUlZLi82wuR"
    headers = {"x-api-key": auth_key}

    # Create a vote
    payload = {
        "image_id": "100",
        "sub_id": "212",
        "value": -2
    }
    post_response = requests.post(key_url, headers=headers, json=payload)
    assert post_response.status_code in [200, 201]
    vote_id = post_response.json()["id"]

    # Delete that vote
    delete_url = f"{key_url}/{vote_id}"
    delete_response = requests.delete(delete_url, headers=headers)

    print("Status Code:", delete_response.status_code)
    print("Response Text:", delete_response.text)

    assert delete_response.status_code in [200, 204]