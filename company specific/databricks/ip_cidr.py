def ip_str_to_int(ip_str):
    """
    Converts an IPv4 string (e.g., "192.168.1.10") to its 32-bit integer representation.
    Raises ValueError for invalid formats.
    """
    octets = ip_str.split('.')
    if len(octets) != 4:
        raise ValueError(f"Invalid IP address format: '{ip_str}'. Must have 4 octets.")

    ip_int_val = 0
    for i, octet_str in enumerate(octets):
        try:
            octet_val = int(octet_str)
        except ValueError:
            raise ValueError(f"Invalid IP address format: '{ip_str}'. Octet '{octet_str}' is not an integer.")

        if not (0 <= octet_val <= 255):
            raise ValueError(f"Invalid IP address format: '{ip_str}'. Octet '{octet_val}' out of range (0-255).")
        
        # Shift the current integer value left by 8 bits (to make space for the new octet)
        # and then OR it with the new octet value.
        # (octet1 << 24) + (octet2 << 16) + (octet3 << 8) + octet4
        ip_int_val = (ip_int_val << 8) | octet_val
        
    return ip_int_val

def cidr_str_to_ip_range(cidr_str):
    """
    Converts a CIDR string (e.g., "192.168.1.0/24") into a tuple
    representing the start and end IP addresses in their integer forms.
    Raises ValueError for invalid formats.
    """
    parts = cidr_str.split('/')
    if len(parts) != 2:
        raise ValueError(f"Invalid CIDR format: '{cidr_str}'. Must be in 'IP/prefix' format.")

    ip_part_str, prefix_part_str = parts

    try:
        base_ip_int = ip_str_to_int(ip_part_str)
    except ValueError as e:
        # Re-raise with more context about CIDR
        raise ValueError(f"Invalid IP part in CIDR '{cidr_str}': {e}")

    try:
        prefix_len = int(prefix_part_str)
    except ValueError:
        raise ValueError(f"Invalid prefix in CIDR '{cidr_str}': '{prefix_part_str}' is not an integer.")

    if not (0 <= prefix_len <= 32):
        raise ValueError(f"Invalid prefix in CIDR '{cidr_str}': {prefix_len} out of range (0-32).")

    # Calculate the network mask
    # For a prefix_len of P, the mask has P leading 1s, followed by (32-P) 0s.
    # 0xFFFFFFFF is a 32-bit integer with all bits set to 1.
    # Shifting it left by (32 - prefix_len) creates the mask.
    # The & 0xFFFFFFFF ensures the mask remains a positive 32-bit integer,
    # important because Python integers can be arbitrarily large.
    if prefix_len == 0: # Special case for /0, matches all IPs
        mask = 0
    else:
        mask = (0xFFFFFFFF << (32 - prefix_len)) & 0xFFFFFFFF
    
    # The start of the CIDR block is the network address.
    # This is found by ANDing the base IP with the mask.
    # This correctly handles cases where the IP part of CIDR is not the network address itself
    # e.g., "192.168.1.10/24" will correctly use 192.168.1.0 as the start.
    start_ip_int = base_ip_int & mask
    
    # The number of addresses in the block is 2^(32 - prefix_len)
    num_addresses = 1 << (32 - prefix_len) # Same as 2**(32 - prefix_len)
    
    # The end of the CIDR block
    # For /32, num_addresses will be 1, so end_ip_int = start_ip_int + 1 - 1 = start_ip_int.
    end_ip_int = start_ip_int + num_addresses - 1
    
    return start_ip_int, end_ip_int

def validate_ip_address_no_library(ip_to_check_str, rules):
    """
    Validates a given IP address based on a list of network rules,
    without using the 'ipaddress' library.

    Args:
        ip_to_check_str (str): The IP address to validate (e.g., "10.0.0.5").
        rules (list): A list of tuples, where each tuple is
                      (cidr_block_str, action_str).
                      Example: [("10.0.0.0/28", "Allow"), ("10.0.0.0/24", "Deny")]

    Returns:
        str: "Allow" or "Deny" based on the first matching rule,
             or "Deny" if no rules match or if the input IP is invalid.
    """
    try:
        target_ip_int = ip_str_to_int(ip_to_check_str)
    except ValueError as e:
        print(f"Error: Invalid IP address format for '{ip_to_check_str}': {e}. Defaulting to Deny.")
        return "Deny"

    for cidr_block_str, action in rules:
        try:
            start_ip_range, end_ip_range = cidr_str_to_ip_range(cidr_block_str)
        except ValueError as e:
            print(f"Warning: Invalid CIDR format '{cidr_block_str}' in rules: {e}. Skipping this rule.")
            continue # Skip this malformed rule

        if start_ip_range <= target_ip_int <= end_ip_range:
            # The IP falls into this CIDR block. Apply the action.
            return action

    # If no rules matched, the default action is Deny.
    return "Deny"

# --- Explanation for Manual Implementation ---

# 1. `ip_str_to_int(ip_str)`:
#    - Splits the input string "A.B.C.D" by the dot `.` into four parts (octets).
#    - Validates that there are exactly four octets.
#    - For each octet string:
#      - Converts it to an integer.
#      - Validates that the integer value is between 0 and 255 (inclusive).
#    - Combines these four 8-bit octet values into a single 32-bit integer. This is typically
#      done by left-shifting the accumulated integer value by 8 bits (to make space for the
#      next octet) and then using a bitwise OR with the new octet value.
#      Example: For "192.168.1.10"
#      - Start with `ip_int = 0`
#      - Octet 1 (192): `ip_int = (0 << 8) | 192 = 192`
#      - Octet 2 (168): `ip_int = (192 << 8) | 168 = (49152) | 168 = 49320`
#      - Octet 3 (1):   `ip_int = (49320 << 8) | 1 = (12625920) | 1 = 12625921`
#      - Octet 4 (10):  `ip_int = (12625921 << 8) | 10 = (3232235776) | 10 = 3232235786`
#    - If any validation fails (wrong number of octets, non-integer octet, octet out of range),
#      it raises a `ValueError`.

# 2. `cidr_str_to_ip_range(cidr_str)`:
#    - Splits the CIDR string "X.Y.Z.W/P" by the slash `/` into the IP part and the prefix length part.
#    - Validates that there are exactly two parts.
#    - Parses the IP part using the `ip_str_to_int` function created above.
#    - Parses the prefix length string into an integer. Validates that this prefix is between 0 and 32.
#    - Calculates the Network Mask:
#      - The mask determines which part of an IP address is the network portion and which is the host portion.
#      - For a prefix length `P`, the mask has `P` leading 1s followed by `(32-P)` 0s in its binary representation.
#      - It's calculated as `(0xFFFFFFFF << (32 - P)) & 0xFFFFFFFF`.
#        - `0xFFFFFFFF` is `2**32 - 1`, representing 32 set bits.
#        - `(32 - P)` gives the number of host bits.
#        - Shifting `0xFFFFFFFF` left by this many bits effectively zeros out the host bits positions, leaving 1s for the network bits.
#        - The final `& 0xFFFFFFFF` ensures the result is treated as an unsigned 32-bit integer, which is good practice in Python when dealing with bitwise operations that should mimic fixed-size integers.
#      - A special case for `P=0` results in a mask of `0`.
#    - Calculates the Start IP of the Range (Network Address):
#      - This is `base_ip_int & mask`. The bitwise AND operation with the mask zeros out the host portion of the `base_ip_int`, effectively giving the first IP address in the CIDR block. This is crucial because an input like "10.0.0.5/28" should refer to the block starting at "10.0.0.0".
#    - Calculates the Number of Addresses in the block: `2^(32 - P)`.
#    - Calculates the End IP of the Range: `start_ip_int + num_addresses - 1`.
#    - Returns a tuple `(start_ip_int, end_ip_int)`.
#    - Raises `ValueError` if any format or value is invalid.

# 3. `validate_ip_address_no_library(ip_to_check_str, rules)`:
#    - The overall logic is the same as the version using the `ipaddress` library.
#    - It calls the manually implemented `ip_str_to_int` and `cidr_str_to_ip_range`.
#    - Includes `try-except ValueError` blocks to catch errors from these helper functions.
#      - If the main `ip_to_check_str` is invalid, it prints an error and returns "Deny".
#      - If a CIDR string within the `rules` is invalid, it prints a warning and skips that rule,
#        continuing to process the rest of the rules.

# --- Example Usage (from your problem description) ---
if __name__ == "__main__":
    print("--- Testing Manual Implementation ---")

    print("\n--- Example 1 ---")
    ip1 = "10.0.0.5"
    rules1 = [
        ("10.0.0.0/28", "Allow"),   # Range: 10.0.0.0 to 10.0.0.15
        ("10.0.0.0/24", "Deny"),
        ("0.0.0.0/0", "Allow")
    ]
    result1 = validate_ip_address_no_library(ip1, rules1)
    print(f"IP: {ip1}, Rules: {rules1}, Result: {result1}") # Expected: Allow

    print("\n--- Example 2 ---")
    ip2 = "10.0.0.20"
    result2 = validate_ip_address_no_library(ip2, rules1)
    print(f"IP: {ip2}, Rules: {rules1}, Result: {result2}") # Expected: Deny (matches 10.0.0.0/24)

    print("\n--- Example 3 ---")
    ip3 = "192.168.1.1"
    rules3 = [
        ("10.0.0.0/8", "Allow")
    ]
    result3 = validate_ip_address_no_library(ip3, rules3)
    print(f"IP: {ip3}, Rules: {rules3}, Result: {result3}") # Expected: Deny (default)

    print("\n--- Example 4: Rule order matters ---")
    ip4 = "10.0.0.5"
    rules4 = [
        ("10.0.0.0/24", "Deny"),
        ("10.0.0.0/28", "Allow")
    ]
    result4 = validate_ip_address_no_library(ip4, rules4)
    print(f"IP: {ip4}, Rules: {rules4}, Result: {result4}") # Expected: Deny

    print("\n--- Example 5: /32 CIDR ---")
    ip5 = "192.168.1.100"
    rules5 = [
        ("192.168.1.100/32", "Allow"),
        ("192.168.1.0/24", "Deny")
    ]
    result5 = validate_ip_address_no_library(ip5, rules5)
    print(f"IP: {ip5}, Rules: {rules5}, Result: {result5}") # Expected: Allow

    print("\n--- Example 6: Non-matching /32 ---")
    ip6 = "192.168.1.101"
    result6 = validate_ip_address_no_library(ip6, rules5)
    print(f"IP: {ip6}, Rules: {rules5}, Result: {result6}") # Expected: Deny (matches 192.168.1.0/24)

    print("\n--- Example 7: /0 CIDR (Allow all) ---")
    ip7 = "8.8.8.8"
    rules7 = [
        ("0.0.0.0/0", "Allow")
    ]
    result7 = validate_ip_address_no_library(ip7, rules7)
    print(f"IP: {ip7}, Rules: {rules7}, Result: {result7}") # Expected: Allow
    
    print("\n--- Example 8: CIDR with host bits set (e.g. 10.0.0.5/28) ---")
    # The base IP 10.0.0.5 for CIDR 10.0.0.5/28 should resolve to network 10.0.0.0/28
    # Range for 10.0.0.0/28 is 10.0.0.0 to 10.0.0.15
    ip8 = "10.0.0.10" # This IP is within 10.0.0.0/28
    rules8 = [
        ("10.0.0.5/28", "Allow") 
    ]
    result8 = validate_ip_address_no_library(ip8, rules8)
    print(f"IP: {ip8}, Rules: {rules8}, Result: {result8}") # Expected: Allow

    ip8_outside = "10.0.0.16" # This IP is outside 10.0.0.0/28
    result8_outside = validate_ip_address_no_library(ip8_outside, rules8)
    print(f"IP: {ip8_outside}, Rules: {rules8}, Result: {result8_outside}") # Expected: Deny


    print("\n--- Example 9: Invalid input IP ---")
    ip9 = "10.0.0.256"
    result9 = validate_ip_address_no_library(ip9, rules1)
    print(f"IP: {ip9}, Rules: {rules1}, Result: {result9}") # Expected: Deny (with error)

    print("\n--- Example 10: Invalid CIDR (prefix out of range) ---")
    ip10 = "10.0.0.1"
    rules10 = [
        ("10.0.0.0/33", "Allow"), # Invalid prefix
        ("10.0.0.0/28", "Deny")
    ]
    result10 = validate_ip_address_no_library(ip10, rules10)
    print(f"IP: {ip10}, Rules: {rules10}, Result: {result10}") # Expected: Deny (first rule skipped, matches second)

    print("\n--- Example 11: Invalid CIDR (IP part malformed) ---")
    rules11 = [
        ("10.0.0/24", "Allow"), # Invalid IP
        ("10.0.0.0/28", "Deny")
    ]
    result11 = validate_ip_address_no_library(ip10, rules11)
    print(f"IP: {ip10}, Rules: {rules11}, Result: {result11}") # Expected: Deny (first rule skipped, matches second)

    print("\n--- Example 12: Invalid CIDR (prefix not integer) ---")
    rules12 = [
        ("10.0.0.0/abc", "Allow"), # Invalid prefix
        ("10.0.0.0/28", "Deny")
    ]
    result12 = validate_ip_address_no_library(ip10, rules12)
    print(f"IP: {ip10}, Rules: {rules12}, Result: {result12}") # Expected: Deny (first rule skipped, matches second)