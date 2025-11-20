# Author: - Chathuranga Lakshan
# Date: - 2024-10-05
# Description: - This script simulates the Least Recently Used (LRU) page replacement algorithm.
#              - It processes a sequence of page requests and manages a fixed number of memory frames,
#                tracking hits, page faults, and hit ratio, while providing step-by-step output.
# Assumptions: - The main memory has 3 memory frames (can be changed in the code). 
#              - There are no any modified bits/dirty bits.
#              - The page order and number of main memory frames are hardcoded but can be modified.

from time import sleep
from prettytable import PrettyTable

# Algorithm function
def lru_algorithm(page_order, num_frames):
    memory = []         # Represents the Main Memory frames
    hits = 0            # Counts the number of hits
    page_faults = 0     # Counts the number of page faults
    hit_ratio = 0.0     # Ratio of hits to total page requests

    for page in page_order:
        if page in memory:
            hits += 1
            memory.remove(page) 
            memory.append(page) # Move the current page to the most recently used position
        else:
            page_faults += 1
            if len(memory) < num_frames: # Checking frame availability
                memory.append(page)
            else:
                memory.pop(0)  # Remove the least recently used page
                memory.append(page)  # Add the new page

        hit_ratio = hits / (hits + page_faults) # Number of hits upon number of attempts.
                                                # Hits(N1), Page Faults(N2) => Hit Ratio = N1/(N1+N2)

        print(f"Processing page: {page}")
        print(f"Memory: {memory }")
        print(f"Hits: {hits}, Page Faults: {page_faults}, Hit Ratio: {hit_ratio:.2f}")
        print()

    print("***FInal Result***")
    result_tb(hits, page_faults, hit_ratio)

# Final result table function  
def result_tb(hits, page_faults, hit_ratio):
    result_tb = PrettyTable()
    result_tb.field_names = ["Total Hits", "Total Page Faults", "Final Hit Ratio"]
    result_tb.add_row([hits, page_faults, f"{hit_ratio:.2f}"])
    print(result_tb)

# Page reference order function
def page_input(page_order):
    print("Please enter your page reference. Maximum 10 reference must provide")
    for i in range(10):
        element = input(f"Enter page {i+1}: ")
        page_order.append(element)

# Execution
page_order = [] # Page reference order list

print("=" * 70)
print("Page Replacement Simulation - Least Recently Used (LRU) Algorithm")
print("=" * 70)

page_input(page_order)
page_order = list(map(int, page_order)) # page_order is a string list. Converting it to an integer list
print()

num_frames = input("Enter the number of frames (must be a value 3-5): ")
num_frames = int(num_frames) # num_frames is a string input. Converting it to an integer value

print("-" * 60)
print(f"Your page reference: {page_order} ")
print(f"Number of frames : {num_frames} ")
print(f"Starting simulation...")
sleep(1)
print("-" * 60)

lru_algorithm(page_order, num_frames)
