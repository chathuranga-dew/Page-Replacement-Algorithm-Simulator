# Page Replacement Algorithm Simulator

This project is a simple simulator for the **Least Recently Used (LRU)** page replacement algorithm.  
It was created as a mini project for the EEX5563 subject.

## Features

- Simulates the LRU page replacement algorithm step by step
- Accept user inputs for page replacement string and number of pages
- Displays memory state, hits, page faults, and hit ratio after each page request
- Shows results in a formatted table

## Assumptions

- The main memory has **3 memory frames** (can be changed in the code)
- There are no any modified bits/dirty bits
- This simulation process limited to 10 pages and number of frames from 3-5, not much as a real environment

## Requirements

- Python 3.8
- [prettytable](https://pypi.org/project/prettytable/) (`pip install prettytable`)

## How to Run

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/Page-Replacement-Algorithm-Simulator.git
    cd Page-Replacement-Algorithm-Simulator
    ```

2. **Install dependencies:**
    ```sh
    pip install prettytable
    ```

3. **Run the simulator:**
    ```sh
    python app.py
    ```

## File Structure

- `app.py` — Main Python script for LRU simulation
- `LICENCE` — Project Licences
- `README.md` — Project documentation

**Created for EEX5563 Mini Project**
