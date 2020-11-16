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
    with open('new_notes.yaml', 'r') as file:
      empty_dict = yaml.full_load(file)
      if len(empty_dict) == 0:
        empty_dict = dict()
        empty_dict['Misc'] = []
      # print(empty_dict)
  # elif os.path.isfile('new_notes.yaml') and my_dict['key']:
  else:
    # with open(r'new_notes.yaml') as file:
    #   empty_dict = yaml.full_load(file)
    empty_dict = dict()
    empty_dict['Misc'] = []
  return empty_dict

# file_name = 'new_notes.yaml'
# location = "/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/"
# path = os.path.join(location, file_name)

def cli():
  make_list = get_args()
  empty_dict = get_yaml()
  #print(make_list)
  if make_list[1] == 'r': # write/remember
    #print(empty_dict['Misc'])
    #print(make_list[2])
    # if 'Misc' not in empty_dict:
    #   empty_dict['Misc'] = []
    #   empty_dict['Misc'].append(make_list[2])
    #   print(f'hm? {empty_dict}')
    # else:
    empty_dict['Misc'].append(make_list[2])
    #print(empty_dict)
  elif make_list[1] == '-c': #create or append
    new_cat = make_list[2]
    if new_cat not in empty_dict:
      empty_dict[new_cat] = []
      empty_dict[new_cat].append(make_list[3])
      #print(empty_dict)
    else:
      empty_dict[new_cat].append(make_list[3])
  elif make_list[1] == 'f':  # forget
    wanna_forget = make_list[2]
    empty_dict[wanna_forget].remove(make_list[3])
    #check that value is in list - to avoid error
      #edit
      #clear
  elif make_list[1] == 'e': #[e]dit a note
    wanna_edit = make_list[2]
    #print(wanna_edit)
    empty_dict[wanna_edit].remove(make_list[3])
    #print(empty_dict)
    empty_dict[wanna_edit].append(make_list[4])
    #print(empty_dict)
  elif make_list[1] == 'clear':
    answer = input('Are you sure you want to clear everything? (y/n): ')
    if answer == 'y':
      # figure out how to remove a file (the yaml file)
      empty_dict.clear()
      os.remove('/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/new_notes.yaml')
      # open('/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/new_notes.yaml','w').close()
      print("Remember file removed successfully")
      #os.remove('/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/new_notes.yaml')
    elif answer == 'n':
      print('Phew! That was close.')
    #empty_dict[wanna_clear].

  with open(r'/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/new_notes.yaml','w') as file:
    Var = yaml.dump(empty_dict, file)
    print(empty_dict)

def get_args():
  return sys.argv
  
# run the main function
#get_yaml()
cli()

# with open(r'/Users/leeg/PyCharmProjects/ntz_just/ntz-note-taker-leegivhan/new_notes.yaml','w') as file:
#   Var = yaml.dump(empty_dict, file)