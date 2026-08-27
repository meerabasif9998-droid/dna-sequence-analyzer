def dna_analyzer(sequence):
    print("DNA sequence analyzer is running...")

    sequence = sequence.strip().upper()
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    base_count = len(sequence)

    print(f"The number of G nucleotides in the sequence is: {g_count}")
    print(f"The number of C nucleotides in the sequence is: {c_count}")
    print(f"The total number of bases in the sequence is: {base_count}")

    print(f"The percentage of G nucleotides in the sequence is: {(g_count / base_count) * 100:.2f}%")
    print(f"The percentage of C nucleotides in the sequence is: {(c_count / base_count) * 100:.2f}%")

    gc_percentage = ((g_count + c_count) / base_count) * 100
    print(f"The percentage of G and C nucleotides in the sequence is: {gc_percentage:.2f}%")

    if gc_percentage >= 60:
        print("The sequence is categorized as 'High GC Content'.")
    elif gc_percentage >= 40:
        print("The sequence is categorized as 'Moderate GC Content'.")
    else:
        print("The sequence is categorized as 'Low GC Content'.")


sequence = input("Please enter a DNA sequence: ")
dna_analyzer(sequence)