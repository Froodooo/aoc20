from copy import deepcopy
from functools import reduce
from operator import mul


def run_a(input_file):
    tiles = _read(input_file)
    tile_neighbours = _find_edge_tiles(tiles)
    corner_tiles = [tile_id for tile_id,
                    tile_matches in tile_neighbours.items() if len(tile_matches) == 2]
    return reduce(mul, corner_tiles)


def run_b(input_file):
    tiles = _read(input_file)
    tile_neighbours = _find_edge_tiles(tiles)
    corner_tiles = [tile_id for tile_id,
                    tile_matches in tile_neighbours.items() if len(tile_matches) == 2]
    _create_image(tile_neighbours, corner_tiles)
    return 0


def _create_image(tile_neighbours, corner_tiles):
    corner_tile_lists = {}

    for corner_tile in corner_tiles:
        seen = []
        next_border_tiles = _next_border_tile(
            tile_neighbours, corner_tile, seen)
        seen += next_border_tiles
        # for next_border_tile in next_border_tiles:

        print(seen)


def _next_border_tile(tile_neighbours, tile_id, seen):
    return [neighbour_tile_id
            for neighbour_tile_id, neighbour_tiles in tile_neighbours.items()
            if tile_id in neighbour_tiles
            and len(neighbour_tiles) == 3
            and neighbour_tile_id not in seen]


def _find_edge_tiles(tiles):
    tile_neighbours = {}
    for tile_id, tile in tiles.items():
        borders = _get_tile_borders(tile)
        edges = []
        for other_tile_id, other_tile in tiles.items():
            if tile_id == other_tile_id:
                continue
            other_borders = _get_tile_borders(other_tile)
            touching_edges = 0
            for rotation in range(0, 4):
                rotated_other_borders = _rotate_borders(
                    other_borders, rotation)
                for flip in ['horizontal', 'vertical', 'none']:
                    flipped_other_borders = _flip_borders(
                        rotated_other_borders, flip)
                    intersection = [
                        (other_tile_id) for border in borders if border in flipped_other_borders]
                    touching_edges += len(intersection)
            if touching_edges > 0:
                edges.append(other_tile_id)
        tile_neighbours[tile_id] = edges

    return tile_neighbours


def _rotate_borders(borders, times):
    if times == 0:
        return borders
    return borders[-times:] + borders[:-times]


# def _rotate_tile(tile, times):
#     for _ in range(times):
#         tile = list(zip(*tile[::-1]))
#     return tile


def _flip_borders(borders, orientation):
    [top, right, bottom, left] = borders
    if orientation == 'horizontal':
        return [top[::-1], left, bottom[::-1], right]
    elif orientation == 'vertical':
        return [bottom, right[::-1], top, left[::-1]]
    else:
        return borders


# def _flip_tile(tile, orientation):
#     flipped_tile = deepcopy(tile)
#     if orientation == 'horizontal':
#         for i in range(len(tile) - 1):
#             flipped_tile[i].reverse()
#     elif orientation == 'vertical':
#         for i in range(len(tile) - 1):
#             flipped_tile[len(tile) - 1 - i] = tile[i]

#     return flipped_tile


def _get_tile_borders(tile):
    top = ''.join([pixel for pixel in tile[0]])
    bottom = ''.join([pixel for pixel in tile[len(tile) - 1]])
    left = ''.join([tile[row][0] for row in range(len(tile))])
    right = ''.join([tile[row][len(tile) - 1] for row in range(len(tile))])

    return [top, right, bottom, left]


def _read(file_name):
    with open(file_name) as f:
        input = f.read().split('\n\n')
        tiles = {}
        for tile in input:
            tiles = _read_tile(tile, tiles)

    return tiles


def _read_tile(tile, tiles):
    tile_lines = tile.rstrip().split('\n')
    tiles[int(tile_lines[0].split()[1][0:-1])] = \
        [[col for col in row] for row in tile_lines[1:]]

    return tiles


def solve():
    input_file = 'day20/20.txt'

    # result_a = run_a(input_file)
    # print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
