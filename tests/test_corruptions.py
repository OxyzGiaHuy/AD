import numpy as np

from src.robustness.corruptions import blur, brightness_contrast, gaussian_noise, jpeg


def test_corruptions_preserve_shape_and_range():
    image = np.full((8, 8, 3), 0.5, dtype="float32")
    for fn in (gaussian_noise, blur, brightness_contrast, jpeg):
        out = fn(image)
        assert out.shape == image.shape
        assert out.min() >= 0.0
        assert out.max() <= 1.0
