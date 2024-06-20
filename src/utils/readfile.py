import os

def read_file(file_path, separator='\t'):
  productList = {}
  with open(os.path.join(os.getcwd(), file_path),"r") as file:
    lines = file.readlines()
    for line in lines:
      key, value = line.strip().split(separator)
      productList[key] = value
  return productList
