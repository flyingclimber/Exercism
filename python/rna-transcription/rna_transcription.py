def to_rna(dna_strand):
    rna_strand = ""

    for char in dna_strand:
        rna_strand += get_rna_complement(char)

    return rna_strand


def get_rna_complement(nucleotide):
    if nucleotide == "G":
        return "C"
    elif nucleotide == "C":
        return "G"
    elif nucleotide == "T":
        return "A"
    elif nucleotide == "A":
        return "U"
    else:
        return "Unknown nucleotide"
