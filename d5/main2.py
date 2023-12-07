with open("input-test", "r") as f:
    lines = f.readlines()

output = [int(x) for x in lines[0][7:-1].split(" ")]
seed_segment = [(start, start + range_to_map -1) for start, range_to_map in zip(output[::2], output[1::2])]
print("Starts:", seed_segment)

def resegment(seeds: list[tuple], dest_start: int, source_start: int, range_to_map: int) -> list[tuple]:
    new = []
    for start, end in seeds:
        if start < source_start:
            new.append((start - (source_start - dest_start), end - (source_start - dest_start)))
        elif start < source_start and end >= source_start + range_to_map:
            new.append((start, end - range_to_map))
        elif start >= source_start and start < source_start + range_to_map and end >= source_start + range_to_map:
            new.append((start - (source_start - dest_start), end - range_to_map))
        elif start < source_start and end >= source_start and end < source_start + range_to_map:
            new.append((start, dest_start - 1))
            new.append((dest_start, end - (source_start - dest_start)))
        else:
            new.append((start, end))
    return new

def remap(seeds: list[tuple[int, int]], dest_start: int, source_start: int, range_to_map: int) -> tuple[list[tuple[int]], list[tuple[int]]]:
    remapped = []
    unchanged = []
    for start, end in seeds:
        if start < source_start:
            remapped.append((start - (source_start - dest_start), end - (source_start - dest_start)))
        elif start < source_start and end >= source_start + range_to_map:
            remapped.append((start, end - range_to_map))
        elif start >= source_start and start < source_start + range_to_map and end >= source_start + range_to_map:
            remapped.append((start - (source_start - dest_start), end - range_to_map))
        elif start < source_start and end >= source_start and end < source_start + range_to_map:
            remapped.append((start, dest_start - 1))
            remapped.append((dest_start, end - (source_start - dest_start)))
        else:
            unchanged.append((start, end))
    return unchanged, remapped

terminate_on = 3000
remapped = []
for idx, line in enumerate(lines[3:]):
    if terminate_on == 0:
        quit()
    if line[0].isdigit():
        print(idx+4, line[:-1])
        dest_start, source_start, range_to_map = [int(x) for x in line.split(" ")]
        seed_segment = resegment(seed_segment, dest_start, source_start, range_to_map)
        # remapped.extend(extended)
        print(seed_segment, remapped)
        terminate_on -= 1
    elif line[0].isalpha():
        seed_segment += remapped
        remapped = []
        print(line[:-1])

quit()
#print(output[::2])
seeds = []
for start, length in zip(output[::2], output[1::2]):
    seeds.extend(range(start, start + length))
#print(seeds)
output = seeds
def remap(seeds: list[int], dest_start: int, source_start: int, range: int) -> list[int]:
    new = []
    #print(f"Remap {dest_start=}, {source_start=}, {range=}")
    remove_x = []
    for x in seeds:
        #print(f"{x=}", end=" ")
        if x >= source_start and x < source_start + range:
            #print(f"-> {x - (source_start - dest_start)}")
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
        #print(idx+4, dest_start, source_start, range, output, new)
    else:
        output += new
        new = []
        print(line[:-1])
output += new

print(min(output))