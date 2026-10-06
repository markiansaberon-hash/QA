import requests 
import json

def test_product_bulk(base_url, auth_headers):
    products = [
        ({"name": "Nebula Keyboard", "price": 99.99, "category": "Electronics", "stock": 10}),
        ({"name": "Cosmic Mouse", "price": 49.99, "category": "Electronics", "stock": 20}),
        ({"name": "Stellar Monitor", "price": 199.99, "category": "Electronics", "stock": 5}),
        ({"name": "Galactic Chair", "price": 149.99, "category": "Furniture", "stock": 15}),
        ({"name": "Lunar Desk", "price": 299.99, "category": "Furniture", "stock": 8}),
        ]
    body = {"items": products}
    response = requests.post(f"{base_url}/products/bulk", json=body, headers=auth_headers, timeout=10)
    assert response.status_code == 201
    print(json.dumps(response.json(), indent=4))
    data_response = response.json()['data']
    print(f"Response data: {data_response}")

    print("The response time is less than 1000 milliseconds")
    assert response.json()['meta']['responseTimeMs'] < 1000

    print("Each item gets an id")
    items = data_response
    for item in items: 
        assert item['id'] is not None, f"Item {item} does not have an id"

    print("The number of items in the response matches the number of items in the request")
    print(f"Number of items in the response: {len(data_response)}")
    print(f"Number of items in the request: {len(products)}")
    assert len(response.json()['data']) == len(products)