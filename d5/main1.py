with open("input", "r") as f:
    lines = f.readlines()

output = [int(x) for x in lines[0][7:-1].split(" ")]
print("Seeds:", output)

def remap(seeds: list[int], dest_start: int, source_start: int, range: int) -> list[int]:
    new = []
    print(f"Remap {dest_start=}, {source_start=}, {range=}")
    remove_x = []
    for x in seeds:
        print(f"{x=}", end=" ")
        if x >= source_start and x < source_start + range:
            print(f"-> {x - (source_start - dest_start)}")
            new.append(x - (source_start - dest_start))
            remove_x.append(x)
    for s in remove_x:
        seeds.remove(s)
    return seeds, new

new = []
for idx, line in enumerate(lines[3:]):
    if line[0].isdigit():
        dest_start, source_start, range = [int(x) for x in line.split(" ")]
        output, tmp = remap(output, dest_start, source_start, range)
        new.extend(tmp)
        print(idx+4, dest_start, source_start, range, output, new)
    else:
        output += new
        new = []
        print(line[:-1])
output += new

print(min(output))