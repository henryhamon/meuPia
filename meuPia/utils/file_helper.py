import os

def read_lines_from_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    return file.readlines()
