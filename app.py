from time import sleep
from prettytable import PrettyTable

def lru_algorithm(page_order, num_frames):
    memory = []
    hits = 0
    page_faults = 0
    hit_ratio = 0.0

    for page in page_order:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
        else:
            page_faults += 1
            if len(memory) < num_frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        hit_ratio = hits / (hits + page_faults)

        print(f"Processing page: {page}")
        sleep(1)  # Simulate processing time
        print(f"Memory: {memory } Hits: {hits}, Page Faults: {page_faults}, Hit Ratio: {hit_ratio:.2f}")
        print()
        sleep(1)  # Simulate time delay for visualization

    result_tb(hits, page_faults, hit_ratio)

    
def result_tb(hits, page_faults, hit_ratio):
    result_tb = PrettyTable()
    result_tb.field_names = ["Total Hits", "Total Page Faults", "Final Hit Ratio"]
    result_tb.add_row([hits, page_faults, f"{hit_ratio:.2f}"])
    print(result_tb)

# Example usage
page_order = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
num_frames = 3

print("=" * 60)
print("Starting LRU Page Replacement Simulation...")
print("=" * 60)

print(f"Page Order: {page_order}")
print(f"Number of Frames in Main Memory: {num_frames}\n")
lru_algorithm(page_order, num_frames)
