def generate_pattern(n):
    pattern = []
    start = 2
    while start <= n:
        sequence = [start + i for i in range(6)]
        pattern.append(sequence)
        start += 6
    return pattern