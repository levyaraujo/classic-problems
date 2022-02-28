from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "tccgcggcgatacgcagcgggccaaccgatcacaaaggggctctcgccgg".upper()


def string_to_gene(string: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(string), 3):
        if (i+2) >= len(string):
            return gene
        codon: Codon = (Nucleotide[string[i]], Nucleotide[string[i+1]], Nucleotide[string[i+2]])
        gene.append(codon)
    
    return gene

my_gene: Gene = string_to_gene(gene_str)
print(my_gene)