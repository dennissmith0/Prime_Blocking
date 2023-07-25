from gen_block_lhs import generate_lhs, generate_blocking_positions as generate_blocking_positions_lhs
from gen_block_rhs import generate_rhs, generate_blocking_positions as generate_blocking_positions_rhs
from pattern import generate_pattern
from gen_block_lhs import position_to_integer

def generate_prime_positions(n):
    k = n // 6
    # Generate LHS primes
    lhs_primes = generate_lhs(n, k)
    # Generate RHS primes
    rhs_primes = generate_rhs(n, k)
    
    # Generate LHS blocking positions
    lhs_blocking_positions_dict = generate_blocking_positions_lhs(n, lhs_primes)
    # Generate RHS blocking positions
    rhs_blocking_positions_dict = generate_blocking_positions_rhs(n, rhs_primes)
    
    # Combine LHS and RHS blocking positions
    combined_blocking_positions_dict = {}
    for p in set(lhs_blocking_positions_dict.keys()).union(rhs_blocking_positions_dict.keys()):
        combined_blocking_positions_dict[p] = sorted(lhs_blocking_positions_dict.get(p, []) + rhs_blocking_positions_dict.get(p, []))


    # Convert the combined blocking positions into integers
    blocking_integers = []
    for blocking_positions in combined_blocking_positions_dict.values():
        for sequence, index in blocking_positions:
            blocking_integers.append(position_to_integer(sequence, index))
    
    # Initialize list of potential prime positions
    potential_prime_positions = []

    # Generate the pattern
    pattern = generate_pattern(n)
    
    # Flatten the pattern and keep index 3 and 5 values only
    flattened_pattern = [item for sublist in pattern for index, item in enumerate(sublist) if index in [3, 5]]
    
    # Iterate over the flattened pattern
    for position in flattened_pattern:
        # If the position is not in the blocking positions, add it to the list of potential prime positions
        if position not in blocking_integers:
            potential_prime_positions.append(position)

    return potential_prime_positions


n = int(input("Enter a number: "))  # Get user input here
print(prime_positions := generate_prime_positions(n))  # Print the list of  prime positions
print(f"Number of primes up to {n}: {len(prime_positions)}")  # Print the number of primes