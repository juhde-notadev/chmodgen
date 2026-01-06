import argparse
import sys

def permissions_to_octal(perm_str):
    """Convert 9-char string (rwxr-xr-x) to octal string (755)."""
    # Strict validation: Only allow r, w, x, -
    valid_chars = set("rwx-")
    if not set(perm_str).issubset(valid_chars):
        raise ValueError("Input contains invalid characters. Use only r, w, x, -")

    mapping = {'r': 4, 'w': 2, 'x': 1, '-': 0}
    octal_result = ""
    
    for i in range(0, 9, 3):
        chunk = perm_str[i:i+3]
        val = sum(mapping.get(c, 0) for c in chunk)
        octal_result += str(val)
        
    return f"chmod {octal_result}"

def octal_to_permissions(octal_str):
    """Convert octal string (755) to 9-char string (rwxr-xr-x)."""
    perms = ""
    for digit in octal_str:
        d = int(digit)
        if d > 7: raise ValueError("Octal digits must be 0-7")
        perms += 'r' if d & 4 else '-'
        perms += 'w' if d & 2 else '-'
        perms += 'x' if d & 1 else '-'
    return perms

def main():
    parser = argparse.ArgumentParser(
        prog='chmodgen',
        description='Convert between octal (755) and symbolic (rwxr-xr-x) permissions.'
    )
    parser.add_argument(
        'permission', 
        help='The permission string (e.g., 755 or rwxr-xr-x)'
    )
    
    # Parse arguments
    args = parser.parse_args()
    inp = args.permission

    try:
        # Detect input type: Digits (Octal)
        if inp.isdigit() and len(inp) == 3:
            print(octal_to_permissions(inp))
            
        # Detect input type: Letters (Symbolic)
        elif len(inp) == 9:
            print(permissions_to_octal(inp))
            
        else:
            print("Error: Input must be exactly 3 digits (755) or 9 characters (rwxr-xr-x).")
            sys.exit(1)
            
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
