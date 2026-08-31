
length = int(input())
strand1 = input().split()
strand2 = input().split()

n_changes = int(input())
for _ in range(n_changes):
    parts = input().split()
    which = int(parts[0])
    pos = int(parts[1])
    gene = parts[2]
    if which == 1:
        strand1[pos] = gene
    else:
        strand2[pos] = gene

print(' '.join(strand1))
print(' '.join(strand2))

pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
mismatch = 0
for i in range(length):
    if pairs.get(strand1[i].upper()) != strand2[i].upper():
        mismatch += 1

print(mismatch)
