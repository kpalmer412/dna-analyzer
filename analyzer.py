def calculate_gc_content(sequence):
    bases = sequence.upper()
    gc_count = bases.count('G') + bases.count('C')
    return (gc_count / len(bases)) * 100 if bases else 0

def transcribe_to_rna(sequence):
    return sequence.upper().replace('T', 'U')
