from flask import Flask, request

app = Flask(__name__)


stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]

# The endpoint decorator
@app.get("/store")
def get_stores():
    return {"stores": stores}

# simple POST example
@app.post("/store")
def create_store():
    request_data = request.get_json()  #retrieve the JSON content of our request.
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    # print('here', stores)
    return new_store, 201   # it also returns json data, new store unit


#  POST data to dynamic URL
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404



# if __name__ == "__main__":
#     # Run Flask on a specific port, e.g., 8080
#     app.run(host="127.0.0.1", port=5006)

# flask run -p 5006
