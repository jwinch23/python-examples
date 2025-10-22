import sys
from encoder import run_length_encode

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].strip():
        input_str = sys.argv[1]
        print(run_length_encode(input_str))
    else: 
        print("Invalid: Please provide a string to analyze.")