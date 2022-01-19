PYTHONPATH=/new_fold  python different_path.py
#PYTHONPATH=/30-Days-Of-Python python different_path.py



#PYTHONPATH=/foo python game.py
import first_import
#from second_import import second
from second_import import *

def first123():
    print('This is First function from Main function ')
def main_func():
    first_import.first()
    first()
    second()
print('Main function')    
main_func()