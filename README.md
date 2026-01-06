chmodgen
A lightweight Python CLI tool to quickly convert between octal (e.g., 755) and symbolic (e.g., rwxr-xr-x) Linux file permissions.

Features
Bidirectional Conversion: Handles both octal-to-symbolic and symbolic-to-octal transformations.

Input Validation:

Strictly validates symbolic characters (r, w, x, -).

Validates octal ranges (0–7).

Ensures correct input lengths (3 digits or 9 characters).

Convenience: Automatically prefixes octal results with the chmod command for easy copy-pasting.

Usage
Run the script from your terminal using Python 3.

1. Symbolic to Octal
Convert a 9-character permission string into a chmod command.

Bash

python chmodgen.py rwxr-xr-x
# Output: chmod 755
2. Octal to Symbolic
Convert a 3-digit octal code into its representative string.

Bash

python chmodgen.py 644
# Output: rw-r--r--
3. Help
View command-line arguments and descriptions.

Bash

python chmodgen.py --help
Installation
Clone the repository:

Bash

git clone https://github.com/yourusername/chmodgen.git
cd chmodgen
Ensure Python is installed: This script requires Python 3.x and uses no external dependencies.

Logic Overview
The script processes permissions based on standard Unix bitweights:

Read (r): 4

Write (w): 2

Execute (x): 1

It splits 9-character strings into three chunks (User, Group, Others) and calculates the sum of the bitweights for each to generate the octal result.
