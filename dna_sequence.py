def dna_sequence_fragments(dna_sequence):
    seen = {}
    for k in [2, 3, 4]:
        for i in range(len(dna_sequence) - k + 1):
            fragment = dna_sequence[i:i+k]
            if fragment not in seen:
                seen[fragment] = None
    # Printing like a set, but ordered
    print("{", end="")
    print(", ".join(f"'{kmer}'" for kmer in seen.keys()), end="")
    print("}")

# Example usage
dna_sequence = "ATCGATCG"
dna_sequence_fragments(dna_sequence)