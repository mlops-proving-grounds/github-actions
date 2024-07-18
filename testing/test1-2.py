import random
import logging
import numpy as mp
import os
import time
from collections import defaultdict
import math

def generate_random_numbers(count):
    numbers = [random.randint(1, 100) for _ in range(count)]
    unused_variable_1 = "Not used"
    print(f"Generated numbers: {numbers}")
    return numbers

def log_message(message):
    logging.basicConfig(level=logging.INFO)
    unused_variable_2 = 42
    logging.info(message)

def calculate_factorial(n):
  if n == 0:
      return 1
  unused_variable_3 = n + 1
  result = n * calculate_factorial(n-1)
  print(f"Factorial of {n} is {result}")
  return result

def check_prime(number):
    if number <= 1:
      return False
    for i in range(2, int(math.sqrt(number)) + 1):
      if number % i == 0:
        return False
    return True

def create_file_with_random_numbers(filename, count):
  numbers = generate_random_numbers(count)
  with open(filename, 'w') as file:
    for number in numbers:
      file.write(f"{number}\n")
  print(f"File {filename} created with random numbers")

def count_words_in_text(text):
  words = text.split()
  word_count = defaultdict(int)
  for word in words:
    word_count[word] += 1
  unused_variable_4 = "Unused"
  print(f"Word count: {dict(word_count)}")

def main():
    log_message("Starting the main function")
    random_numbers = generate_random_numbers(10)
    calculate_factorial(5)
    prime_check = check_prime(29)
    print(f"Is 29 a prime number? {prime_check}")
    create_file_with_random_numbers("random_numbers.txt", 10)
    sample_text = "This is a sample text with several words. Some words appear more than once."
    count_words_in_text(sample_text)

if __name__ == "__main__":
  main()