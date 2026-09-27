"""
broken_report.py — FASTA report script

This script SHOULD:
  1. read data/sequences.fasta
  2. store the sequences in a dictionary {name: sequence}
  3. print the length and GC content of each sequence
  4. print how many times each base appears in total

It contains 5 bugs. 🐛
Fix them ONE AT A TIME: run, read the FIRST error, fix, run again.

Four bugs give you an error message.
One bug gives you NO error at all — but the numbers are wrong. 🤫
Hint for that one: what does a line read from a file end with?
"""

filename = "data/sequenses.fasta"

sequences = {}
name = None

with open(filename) as f:
    for line in f
        if line.startswith(">"):
            name = line[1:]
            sequences[name] = ""
        else:
            sequences[name] = sequences[name] + line

print("Sequences loaded:", len(sequences))
print()

# ---- report per sequence ----

lengths = []

for name, seq in sequences.items():
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    lenghts.append(len(seq))
    print(f"{name}\tlength: {len(seq)}\tGC: {gc:.1f}%")

print()
print("Average length:", sum(lengths) / len(lengths))
print()

# ---- total base counts ----

counts = {}

for seq in sequences.values():
    for base in seq:
        counts[base] = counts[base] + 1

print("Base counts:", counts)
