MAX_OUTPUT_IMAGES = 4
DEFAULT_OUTPUT_IMAGES = 1


def normalize_output_count(value):
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        parsed = DEFAULT_OUTPUT_IMAGES
    return max(DEFAULT_OUTPUT_IMAGES, min(MAX_OUTPUT_IMAGES, parsed))


def build_output_count_options_html(selected=DEFAULT_OUTPUT_IMAGES):
    selected = normalize_output_count(selected)
    options = []
    for value in range(DEFAULT_OUTPUT_IMAGES, MAX_OUTPUT_IMAGES + 1):
        selected_attr = " selected" if value == selected else ""
        label = f"{value} image" if value == 1 else f"{value} images"
        options.append(f'<option value="{value}"{selected_attr}>{label}</option>')
    return "".join(options)


def build_output_gallery_placeholders_html(output_count=DEFAULT_OUTPUT_IMAGES):
    output_count = normalize_output_count(output_count)
    cards = []
    for idx in range(output_count):
        cards.append(
            f"""<div class="output-card" data-output-idx="{idx}">
                <button class="output-card-download" data-output-idx="{idx}" title="Download output {idx + 1}">
                    Download
                </button>
                <div class="output-card-placeholder">Result {idx + 1}</div>
            </div>"""
        )
    return "".join(cards)
