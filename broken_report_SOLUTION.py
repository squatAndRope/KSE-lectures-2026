"""
broken_report_SOLUTION.py — FASTA report script (fixed version, for the teacher)

Bugs that were in broken_report.py:
  1. SyntaxError      — missing ":" after "for line in f"
  2. FileNotFoundError— filename typo: "sequenses.fasta"
  3. NameError        — "lenghts.append(...)" instead of "lengths"
  4. KeyError         — counts[base] used before it exists (needs .get or an if)
  5. SILENT BUG       — no .strip(): every line keeps its "\n", so sequences are
                        too long, GC% is too low and counts contains "\n"
"""

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

filename = "data/sequences.fasta"

sequences = {}
name = None

with open(filename) as f:
    for line in f:
        line = line.strip()          # FIX 5: remove the newline
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
    lengths.append(len(seq))
    print(f"{name}\tlength: {len(seq)}\tGC: {gc:.1f}%")

print()
print("Average length:", sum(lengths) / len(lengths))
print()

# ---- total base counts ----

counts = {}

for seq in sequences.values():
    for base in seq:
        counts[base] = counts.get(base, 0) + 1

print("Base counts:", counts)
