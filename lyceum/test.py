expected_response = {"produts": [{"title": "tea", "count": 3}]}


def test_available_tee_response_dict(response):
    assert isinstance(response, dict)


def test_available_tee_products_in_response(response):
    assert "products" in response, f"fields in response {list(response.keys())}"

    #
    assert len(response) == 1
    assert isinstance(response["products"], list)
    products = response["products"]
    assert len(products) == 1
    product = products[0]
    assert isinstance(product, dict)
    assert product["tittle"] == "tea"
    assert product["count"] == 3
    assert len(product) == 2
