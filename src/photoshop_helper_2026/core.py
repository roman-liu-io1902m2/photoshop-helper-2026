"""Core implementation for photoshop-helper-2026 automated batch processing."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class Config:
    """Configuration for batch processing operations."""

    input_dir: Path
    output_dir: Path
    filters: List[str] = field(default_factory=list)
    naming_convention: str = "{stem}_processed"
    organize_layers: bool = True
    layer_prefix: str = "LAYER_"
    recursive: bool = False


def _build_naming_convention(stem: str, config: Config) -> str:
    """Generate a consistent filename based on the naming convention."""
    return config.naming_convention.format(stem=stem)


def _organize_layers(layer_names: List[str], config: Config) -> List[str]:
    """Apply layer organization and naming conventions to layer names."""
    if not config.organize_layers:
        return layer_names

    organized = []
    for index, name in enumerate(layer_names, start=1):
        organized.append(f"{config.layer_prefix}{index:03d}_{name}")
    return organized


def run(config: Config) -> int:
    """Execute the batch processing workflow.

    Args:
        config: Configuration object specifying directories, filters, and options.

    Returns:
        Exit code: 0 on success, 1 on failure.
    """
    if not config.input_dir.exists():
        print(f"Error: Input directory '{config.input_dir}' does not exist.")
        return 1

    config.output_dir.mkdir(parents=True, exist_ok=True)

    if config.recursive:
        image_files = sorted(config.input_dir.rglob("*.png")) + \
                      sorted(config.input_dir.rglob("*.jpg")) + \
                      sorted(config.input_dir.rglob("*.psd"))
    else:
        image_files = sorted(config.input_dir.glob("*.png")) + \
                      sorted(config.input_dir.glob("*.jpg")) + \
                      sorted(config.input_dir.glob("*.psd"))

    processed_count = 0
    for image_path in image_files:
        output_name = _build_naming_convention(image_path.stem, config)
        output_path = config.output_dir / f"{output_name}{image_path.suffix}"

        # Simulate applying filters and organizing layers
        layer_names = [f"background_{processed_count}"]
        organized_layers = _organize_layers(layer_names, config)

        if config.filters:
            for f in config.filters:
                print(f"  Applying filter '{f}' to {image_path.name}")

        print(f"Processing: {image_path.name} -> {output_path.name}")
        print(f"  Organized layers: {organized_layers}")
        processed_count += 1

    print(f"\nBatch complete: {processed_count} image(s) processed.")
    return 0
