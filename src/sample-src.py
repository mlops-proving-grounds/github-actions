import json

import requests


def foo(x, y):
    return x + y


def bar(z):
    print("Value: ", z)
    return z * 2


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_method(self):
        print(f"Name: {self.name} and Age: {self.age}")


def get_data_from_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully")
            return data
        else:
            print("Failed to fetch data")
            return None
    except requests.exceptions.RequestException as e:
        print("Error during requests to {0} : {1}".format(url, str(e)))
        return None


def process_data(data):
    if not data:
        print("No data to process")
        return []
    processed = []
    for item in data:
        processed.append({"id": item["id"], "value": item.get("value", None)})
    return processed


def save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)
    print("Data saved to", filename)


def main():
    url = "http://example.com/api/data"
    data = get_data_from_api(url)
    processed_data = process_data(data)
    save_to_file(processed_data, "output.json")
    x = 10
    y = 20
    result = foo(x, y)
    bar(result)
    obj = MyClass("Bob", 25)
    obj.my_method()
    print("Done")


if __name__ == "__main__":
    main()
