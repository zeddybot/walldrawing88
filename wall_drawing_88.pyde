from itertools import product

ROWS, COLS = 10, 10
AMPLITUDE_RANGE, WAVELENGTH_RANGE = (15, 50), (15, 50)

size(800, 800)
background(255, 255, 255)
stroke(0)
strokeWeight(1)


def wave(theta, b, rect_coords):
    amplitude, wavelength = random(*AMPLITUDE_RANGE), random(*WAVELENGTH_RANGE)
    noiseSeed(int(random(-1000, 1000)))
    box_x0, box_y0, box_x1, box_y1 = box
    m = -tan(theta)
    if m > 0:
        end_y = 0
    else:
        end_y = height
    x0 = 0
    y0 = b
    x1 = (b - end_y) / m
    y1 = end_y
    length = 10 * sqrt(sq(x1 - x0) + sq(y1 - y0))
    for i in range(int(length)):
        x = map(i, 0, length, x0, x1)
        y = map(i, 0, length, y0, y1)
        waviness = map(noise(x / wavelength, y / wavelength), 0, 1, -amplitude, amplitude)
        x += waviness * sin(theta)
        y += waviness * cos(theta)
        if x >= box_x0 and x <= box_x1 and y >= box_y0 and y <= box_y1:
            point(x, y)


def get_offset_range(theta):
    if theta > 0:
        max_offset = (height / COLS) + (width * tan(theta) / ROWS)
        min_offset = 0
    else:
        max_offset = height / COLS
        min_offset = width * tan(theta) / ROWS
    return min_offset, max_offset

for row in range(10):
    line(row * width / ROWS, 0, row * width / ROWS, height)

for col in range(10):
    line(0, col * height / COLS, width, col * height / COLS)

for row, col in product(range(ROWS), range(COLS)):
    theta = random(-HALF_PI, HALF_PI)
    min_offset, max_offset = get_offset_range(theta)
    slope = tan(theta)
    num_lines = random(1, 15)
    offsets = [random(min_offset, max_offset) for _ in range(int(num_lines))]
    
    for offset in offsets:
        b  = (col * height / COLS) + offset - (slope * (row+1) * width / ROWS)
        box = (row * width / ROsWS, col * height / COLS, (row + 1) * width / ROWS, (col + 1) * height / COLS)
        wave(theta, b, box)

save("examples/image.png")
