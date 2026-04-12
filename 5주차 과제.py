for dan in range(2, 10):
    print(f"# {dan}단 #", end="\t")
print()

for i in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan}X{i}= {dan*i}", end="\t")
    print()