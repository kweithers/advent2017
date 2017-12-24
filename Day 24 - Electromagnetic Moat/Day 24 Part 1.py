import copy
data = []
with open('day24.txt', 'r') as f:
    for line in f.readlines():
        a, b = line.split('/')
        data.append((int(a), int(b)))

bridge = ([], 0)

def run(b, d):
    available = [a for a in d if b[1] in a]
    if len(available) == 0:
        yield b
    else:
        for a in available:
            d_ = copy.copy(d)
            d_.remove(a)
            for q in run((b[0] + [a], a[0] if b[1] == a[1] else a[1]), d_):
                yield q

print max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), run(bridge, data)))