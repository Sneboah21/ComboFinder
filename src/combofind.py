import random as r
from utils.readfile import read_file

def result(input_path,upper_limit,lower_limit):
  product_list = read_file(input_path) #product_list is a dictionary
  combo_list = set()
  numItr = 1000
  for i in range(numItr):
    length = r.randint(2,len(product_list))
    subset = r.sample(list(product_list.keys()),length)
    comboSum = sum([int(product_list[j]) for j in subset])
    if lower_limit<=comboSum<=upper_limit:
      combo_list.add(tuple(subset))  
    list_len = len(combo_list)
  #print(combo_list)
  return combo_list,list_len
  
  




