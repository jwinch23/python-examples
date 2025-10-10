import sys
from encoder import run_length_encode

if __name__ == "__main__":
    input_str = sys.argv[1]
    print(run_length_encode(input_str))