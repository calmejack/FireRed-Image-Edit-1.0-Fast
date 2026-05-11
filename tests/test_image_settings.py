from image_settings import resolve_output_dimensions


class DummyImage:
    def __init__(self, width, height):
        self.size = (width, height)


def test_preserves_original_aspect_ratio_for_original_mode():
    image = DummyImage(1200, 800)

    width, height = resolve_output_dimensions(image, "original")

    assert (width, height) == (1024, 680)


def test_uses_fixed_square_ratio_when_requested():
    image = DummyImage(1200, 800)

    width, height = resolve_output_dimensions(image, "1:1")

    assert (width, height) == (1024, 1024)


def test_uses_fixed_portrait_ratio_when_requested():
    image = DummyImage(800, 1200)

    width, height = resolve_output_dimensions(image, "9:16")

    assert (width, height) == (768, 1376)
