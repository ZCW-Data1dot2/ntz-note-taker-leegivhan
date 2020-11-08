# add your code in this file
import os
import yaml
import sys


# main function

empty_dict = {}

def get_yaml():
  if os.path.isfile('new_notes.yaml'):
    with open(r'new_notes.yaml') as file:
      empty_dict = yaml.full_load(file)
  else:
    empty_dict = {}
    return empty_dict

def cli():
  make_list = get_args()
  print(make_list)
  if make_list[1] == 'r':
    empty_dict['Misc'] = make_list[2]
    print(empty_dict)
  elif make_list[1] == '-c':
    new_cat = make_list[2]
    empty_dict[new_cat] = make_list[3]
    print(empty_dict)
  elif make_list[1] == 'f':  # need to change category
    wanna_forget = make_list[2]
    empty_dict[wanna_forget] = make_list[3]
  
def get_args():
  return sys.argv
  
# run the main function
get_yaml()
cli()

with open(r'/Users/leeg/PyCharmProjects/new_notes.yaml','w') as file:
  Var = yaml.dump(new_dict, file)