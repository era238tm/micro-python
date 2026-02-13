import numpy as np
from PIL import Image


def mandelbrot_set(image_size=2**12, max_iteration=2**6):
    real_axis = np.linspace(-2, 2, num=image_size)
    imag_axis = real_axis[real_axis < 0]

    c_grid = np.zeros((image_size // 2, image_size), dtype=complex)
    c_grid.real, c_grid.imag = np.meshgrid(real_axis, imag_axis)
    z_grid = np.zeros_like(c_grid)

    pixel_grid = np.zeros((image_size // 2, image_size, 3), dtype=np.uint8)
    todo = np.ones_like(c_grid, dtype=bool)

    for iteration in range(max_iteration):
        z_grid[todo] = z_grid[todo] ** 2 + c_grid[todo]
        mask = np.logical_and(np.absolute(z_grid) > 2, todo)

        hue = 255 * (iteration + 1) / max_iteration
        saturation = 255
        value = 255 if iteration < max_iteration else 0

        pixel_grid[mask] = (hue, saturation, value)
        todo = np.logical_and(todo, np.logical_not(mask))

    return np.concatenate((pixel_grid, np.flip(pixel_grid, axis=0)))


if __name__ == '__main__':
    image = Image.fromarray(mandelbrot_set(), mode='HSV').convert('RGB')
    image.save('output.png', optimize=True)
