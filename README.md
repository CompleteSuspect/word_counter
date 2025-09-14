# Word Counter 

A simple Python program that reads a text file, normalises the words (case-insensitive, removes punctuation), and counts word frequencies.  
The results are written to an output file, sorted by frequency and word length.  

---

## Features 
- Normalises input text (case-insensitive, strips punctuation).  
- Uses Python's built-in **`re`** module for text cleaning.  
- Counts word frequency with **`collections.Counter`**.  
- Sorted output (by frequency, then word length).  
- Input and output files configurable via **command-line arguments**.  

---

## Usage 

### Run with Python

python Word_Counter.py input.txt results.txt
