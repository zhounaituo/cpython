#!/usr/bin/env python

"""
file: rst_to_ipynb.py
"""
import re
import os

rst_files_list = os.popen('ls *.rst').read().split('\n')
rst_files_list.pop()

pattern = re.compile("(.*)\.rst")
base_path = os.getcwd()

if rst_files_list:
    if not os.path.exists('ipynbs/'):
        os.mkdir('ipynbs')
    for file in rst_files_list:
        file_name = re.match(pattern, file).group(1)
        os.popen(f'pandoc {file_name}.rst -o {file_name}.ipynb')  # e.g pandoc appendix.rst -o appendix.ipynb
        # os.rename(os.path.join(base_path, f'{file_name}.ipynb'),
        #         os.path.join(base_path, 'ipynbs'))
