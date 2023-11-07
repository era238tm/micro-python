import numpy as np
from PIL import Image


def julia_set(complex_parameter, image_size=2**12, max_iteration=2**8):
    real_axis = np.linspace(-2, 2, num=image_size)
    imag_axis = real_axis[real_axis <= 0]

    z_grid = np.zeros((image_size // 2, image_size), dtype=complex)
    z_grid.real, z_grid.imag = np.fliplr(np.meshgrid(real_axis, imag_axis))
    c_grid = np.full_like(z_grid, complex_parameter)

    pixel_grid = np.zeros((image_size // 2, image_size, 3), dtype=np.uint8)
    todo = np.ones_like(z_grid, dtype=bool)

    for iteration in range(max_iteration):
        z_grid[todo] = z_grid[todo] ** 2 + c_grid[todo]
        mask = np.logical_and(np.absolute(z_grid) > 2, todo)

        hue = 255 * (iteration + 1) / max_iteration
        saturation = 255
        value = 255 if iteration < max_iteration else 0

        pixel_grid[mask] = (hue, saturation, value)
        todo = np.logical_and(todo, np.logical_not(mask))

    return np.concatenate((np.rot90(pixel_grid, 2), pixel_grid))


if __name__ == '__main__':
    image = Image.fromarray(julia_set(-0.61+0j), mode='HSV').convert('RGB')
    image.save(f'output/{0.61+0j}.png', optimize=True)
