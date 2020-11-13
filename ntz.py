# add your code in this file
import os
import yaml
import sys
# ntz has four commands.
# * [r]emember
#  * [-c] creates or appends to a category
# * [f]orget a note
# * [e]dit a note
# * clear

# main function

# empty_dict = {
# }

def get_yaml():
  if os.path.isfile('new_notes.yaml'):
    with open(r'new_notes.yaml') as file:
      empty_dict = yaml.full_load(file)
      print(empty_dict)
  else:
    empty_dict = dict()
    empty_dict['Misc'] = []
  return empty_dict

def cli():
  make_list = get_args()
  empty_dict = get_yaml()
  print(make_list)
  if make_list[1] == 'r':# write/remember
    print(empty_dict['Misc'])
    print(make_list[2])
    # if 'Misc' not in empty_dict:
    #   empty_dict['Misc'] = []
    #   empty_dict['Misc'].append(make_list[2])
    #   print(f'hm? {empty_dict}')
    # else:
    empty_dict['Misc'].append(make_list[2])
    print(empty_dict)
    #print(empty_dict)
  elif make_list[1] == '-c': #create or append
    new_cat = make_list[2]
    if new_cat not in empty_dict:
      empty_dict[new_cat] = []
      empty_dict[new_cat].append(make_list[3])
      print(empty_dict)
    else:
      empty_dict[new_cat].append(make_list[3])
  elif make_list[1] == 'f':  # forget
    wanna_forget = make_list[2]
    empty_dict[wanna_forget].remove(make_list[3])
    #check that value is in list - to avoid error
      #edit
      #clear
  with open(r'/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/new_notes.yaml','w') as file:
    Var = yaml.dump(empty_dict, file)

def get_args():
  return sys.argv
  
# run the main function
#get_yaml()
cli()

# with open(r'/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/new_notes.yaml','w') as file:
#   Var = yaml.dump(empty_dict, file)