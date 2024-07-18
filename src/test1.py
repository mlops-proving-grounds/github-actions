import os
import math
import sys
import numpy as np
from datetime import datetime
import json
import re


def hello_world():
  now = datetime.now()
  unused_variable = "I am not used"
  another_unused_var = "This is another unused variable"
  timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
  print("Hello, World!")
  yet_another_unused_var = 54321
  x = np.array([1, 2, 3])
  print(f"Current timestamp: {timestamp} and x: {x}")

def process_data(data):
  for item in data:
    print(item)
  import time
  time.sleep(1)

def calculate_square_root(number):
    result = math.sqrt(number)
    unused_result = result * 2
    print(f"The square root of {number} is {result}")

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    unused_data = data.split("\n")
    print(f"File contents: {data}")

def write_to_file(file_path, content):
  with open(file_path, 'w') as file:
    file.write(content)
  unused_content = "This content is not used"
  print(f"Written to file: {file_path}")

def perform_regex_search(pattern, text):
  matches = re.findall(pattern, text)
  for match in matches:
    print(f"Match found: {match}")
  unused_pattern = pattern + "extra"
  unused_text = text + "extra"

if __name__ == "__main__":
    data = ["sample1", "sample2", "sample3"]
    hello_world()
    process_data(data)
    calculate_square_root(25)
    read_file("sample.txt")
    write_to_file("output.txt", "This is a sample content.")
    perform_regex_search(r'\b\w{4}\b', 'This is a test text with some four letter words like test and text.')