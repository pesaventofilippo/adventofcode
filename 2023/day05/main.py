import multiprocessing as mp
MAPS: dict[int, list[tuple[int, int, int]]] = {}
SEED_RANGES: list[tuple[int, int]] = []

def _convert(_value: int, _map: int) -> int:
    _map = MAPS[_map]
    for mapping in _map:
        if (_value >= mapping[1]) and (_value < mapping[1]+mapping[2]):
            return mapping[0] - mapping[1] + _value
    return _value

seed_to_soil = lambda seed: _convert(seed, 0)
soil_to_fertilizer = lambda soil: _convert(soil, 1)
fertilizer_to_water = lambda fertilizer: _convert(fertilizer, 2)
water_to_light = lambda water: _convert(water, 3)
light_to_temperature = lambda light: _convert(light, 4)
temperature_to_humidity = lambda temperature: _convert(temperature, 5)
humidity_to_location = lambda humidity: _convert(humidity, 6)


with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()

        if line == "":
            continue

        elif line.startswith("seeds: "):
            seeds = [int(x) for x in line.split(": ", 1)[1].split()]
            SEED_RANGES = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

        elif line == "seed-to-soil map:":
            LOADED_MAP = 0
        elif line == "soil-to-fertilizer map:":
            LOADED_MAP = 1
        elif line == "fertilizer-to-water map:":
            LOADED_MAP = 2
        elif line == "water-to-light map:":
            LOADED_MAP = 3
        elif line == "light-to-temperature map:":
            LOADED_MAP = 4
        elif line == "temperature-to-humidity map:":
            LOADED_MAP = 5
        elif line == "humidity-to-location map:":
            LOADED_MAP = 6

        else:
            if LOADED_MAP not in MAPS:
                MAPS[LOADED_MAP] = []
            MAPS[LOADED_MAP].append(tuple(int(x) for x in line.split()))


def eval_seeds(_range: tuple[int, int]) -> int:
    minim = -1
    print(f"Eval {_range[0]}-{_range[1]}...")
    for seed in range(_range[0], _range[1]):
        val = humidity_to_location(
            temperature_to_humidity(
                light_to_temperature(
                    water_to_light(
                        fertilizer_to_water(
                            soil_to_fertilizer(
                                seed_to_soil(seed)
                            )
                        )
                    )
                )
            )
        )
        minim = val if minim == -1 else min(minim, val)
    print(f"---> {_range[0]}-{_range[1]} done: {minim}.")
    return minim


if __name__ == "__main__":
    SEED_RANGES = [(SEED_RANGES[i][0] + (SEED_RANGES[i][1] - SEED_RANGES[i][0])//8 * j,
                    SEED_RANGES[i][0] + (SEED_RANGES[i][1] - SEED_RANGES[i][0])//8 * (j+1))
                   for i in range(len(SEED_RANGES)) for j in range(8)]

    with mp.Pool(4) as pool:
        results = pool.imap_unordered(eval_seeds, SEED_RANGES, chunksize=1)
        print(min(results))
