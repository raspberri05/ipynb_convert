import sys
import os

curr_path = os.path.abspath(__file__)

curr_dir = os.path.dirname(curr_path)

root = os.path.dirname(curr_dir)
sys.path.append(root)

from src.ipynb_convert import convert

convert.convert_to_python("to_py.ipynb")

convert.convert_to_ipynb("to_ipynb.py")



