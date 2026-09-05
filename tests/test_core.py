"""Tests for the core module of photoshop-helper-2026."""

import pytest

from photoshop_helper_2026.core import (
    apply_filter,
    batch_process,
    organize_layers,
)


def test_apply_filter_returns_adjusted_values():
    """Verify that apply_filter modifies pixel values consistently."""
    pixels = [0, 50, 100, 200, 255]
    result = apply_filter(pixels, brightness=10, contrast=1.2)
    # Brightness adds 10, contrast multiplies around 128
    expected = [int((p - 128) * 1.2 + 128 + 10) for p in pixels]
    expected = [max(0, min(255, v)) for v in expected]
    assert result == expected


def test_batch_process_processes_all_images():
    """Ensure batch_process handles a list of image dicts and returns results."""
    images = [
        {"name": "a.jpg", "pixels": [10, 20, 30]},
        {"name": "b.jpg", "pixels": [40, 50, 60]},
    ]
    results = batch_process(images, brightness=5, contrast=1.0)
    assert len(results) == 2
    assert results[0]["name"] == "a.jpg"
    assert results[1]["name"] == "b.jpg"
    # With contrast 1.0 and brightness 5, each pixel should be +5
    assert results[0]["pixels"] == [15, 25, 35]
    assert results[1]["pixels"] == [45, 55, 65]


def test_organize_layers_applies_naming_convention():
    """Check that organize_layers renames layers using the convention."""
    layers = [
        {"name": "Layer 1", "type": "raster"},
        {"name": "Layer 2", "type": "text"},
        {"name": "Layer 3", "type": "shape"},
    ]
    organized = organize_layers(layers, prefix="FX_")
    assert organized[0]["name"] == "FX_Layer1_raster"
    assert organized[1]["name"] == "FX_Layer2_text"
    assert organized[2]["name"] == "FX_Layer3_shape"
