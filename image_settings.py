import math


TARGET_OUTPUT_AREA = 1024 * 1024
ORIGINAL_ASPECT_RATIO_VALUE = "original"
ASPECT_RATIO_OPTIONS = [
    (ORIGINAL_ASPECT_RATIO_VALUE, "Original"),
    ("3:4", "3:4"),
    ("2:3", "2:3"),
    ("9:16", "9:16"),
    ("1:1", "1:1"),
    ("16:9", "16:9"),
    ("3:2", "3:2"),
    ("4:3", "4:3"),
]
ASPECT_RATIO_MAP = {
    value: float(width) / float(height)
    for value, _ in ASPECT_RATIO_OPTIONS
    if value != ORIGINAL_ASPECT_RATIO_VALUE
    for width, height in [value.split(":")]
}


def _round_down_to_multiple(value, multiple):
    return max(multiple, int(value) // multiple * multiple)


def _round_to_nearest_multiple(value, multiple):
    return max(multiple, round(float(value) / multiple) * multiple)


def resize_like_original_upload(image, max_side=1024, multiple_of=8):
    width, height = image.size
    if width > height:
        target_width = max_side
        target_height = int(target_width * height / width)
    else:
        target_height = max_side
        target_width = int(target_height * width / height)
    return (
        _round_down_to_multiple(target_width, multiple_of),
        _round_down_to_multiple(target_height, multiple_of),
    )


def calculate_dimensions_for_ratio(ratio, target_area=TARGET_OUTPUT_AREA, multiple_of=32):
    width = math.sqrt(target_area * ratio)
    height = width / ratio
    return (
        _round_to_nearest_multiple(width, multiple_of),
        _round_to_nearest_multiple(height, multiple_of),
    )


def resolve_output_dimensions(image, aspect_ratio):
    normalized_ratio = str(aspect_ratio or ORIGINAL_ASPECT_RATIO_VALUE).strip().lower()
    if normalized_ratio in ("", ORIGINAL_ASPECT_RATIO_VALUE, "raw", "原始"):
        return resize_like_original_upload(image)
    ratio = ASPECT_RATIO_MAP.get(normalized_ratio)
    if ratio is None:
        return resize_like_original_upload(image)
    return calculate_dimensions_for_ratio(ratio)
