n = int(input())

unique_chemicals = set()

for _ in range(n):
    chemicals = input().split()
    for chemical in chemicals:
        unique_chemicals.add(chemical)

# unique_chemicals = {chemical for _ in range(n) for chemical in input().split()}

for chemical in unique_chemicals:
    print(chemical)
