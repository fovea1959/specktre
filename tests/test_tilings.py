# -*- encoding: utf-8 -*-

from specktre.tilings import generate_squares, generate_triangles


def test_generate_squares():
    result = generate_squares(
        image_width=100,
        image_height=100,
        side_length=50
    )
    squares = list(result)
    assert squares == [
        [(0, 0), (50, 0), (50, 50), (0, 50)],
        [(0, 50), (50, 50), (50, 100), (0, 100)],
        [(0, 100), (50, 100), (50, 150), (0, 150)],
        [(50, 0), (100, 0), (100, 50), (50, 50)],
        [(50, 50), (100, 50), (100, 100), (50, 100)],
        [(50, 100), (100, 100), (100, 150), (50, 150)],
        [(100, 0), (150, 0), (150, 50), (100, 50)],
        [(100, 50), (150, 50), (150, 100), (100, 100)],
        [(100, 100), (150, 100), (150, 150), (100, 150)]
    ]
