# This tool is slapped together with some digital duct tape
# Improvements will be done when I feel like it
# Which is probably never

import sys

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage:\n    main.py input_file output_file [cutoff_length=80]")
        return

    maxlen = 80 if len(args) < 4 else int(args[3])
    delimeter = " "

    with open(args[1], "r") as infile:
        # Get text and split by line
        text = infile.read()
        lines = text.splitlines()

        # Detect newline type
        breaker = "\r\n" if "\r\n" in text else "\n"

        # Split each line and save to output file
        with open(args[2], "w") as outfile:
            for line in lines:
                outfile.write(split_line(line, maxlen, delimeter, breaker))

def split_line(line, maxlen, delimeter, breaker):
    # Check if line can be split
    if len(line) > maxlen and delimeter in line:
        splitlen = maxlen
        # Find where to split
        while not line[splitlen] == delimeter:
            splitlen -= 1
        
        # Copy leading whitespace from soruce line
        leads = line[:len(line)-len(line.lstrip())]

        # Split again if second part is still too long
        remainder = split_line(leads + line[splitlen+1:], maxlen, delimeter, breaker)

        # Construct and return result
        newlined_str = line[:splitlen] + breaker + remainder
        return newlined_str
    else:
        return line + breaker


if __name__ == "__main__":
    main()
