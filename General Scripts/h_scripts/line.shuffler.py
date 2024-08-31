# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:33:13 2024

@author: sucre
"""
import random

def randomize_file_lines(file_path, num_randomizations):
    # Read the lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Perform the specified number of randomizations
    for _ in range(num_randomizations):
        random.shuffle(lines)

    # Write the shuffled lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Example usage:
file_path = 'C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\r_visualization.improvement.txt'
num_randomizations = 5
randomize_file_lines(file_path, num_randomizations)