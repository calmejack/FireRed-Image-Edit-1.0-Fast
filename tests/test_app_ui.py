from app_ui import (
    MAX_OUTPUT_IMAGES,
    build_output_count_options_html,
    build_output_gallery_placeholders_html,
    normalize_output_count,
)


def test_output_count_options_default_to_one_and_allow_up_to_four():
    html = build_output_count_options_html()

    assert MAX_OUTPUT_IMAGES == 4
    assert html.count("<option") == 4
    assert 'value="1" selected' in html
    assert 'value="4"' in html


def test_output_gallery_renders_a_download_button_for_each_output_card():
    html = build_output_gallery_placeholders_html(3)

    assert html.count('class="output-card"') == 3
    assert html.count('class="output-card-download"') == 3
    assert 'data-output-idx="0"' in html
    assert 'data-output-idx="1"' in html
    assert 'data-output-idx="2"' in html


def test_normalize_output_count_clamps_to_supported_range():
    assert normalize_output_count(None) == 1
    assert normalize_output_count(0) == 1
    assert normalize_output_count(2) == 2
    assert normalize_output_count(8) == 4
