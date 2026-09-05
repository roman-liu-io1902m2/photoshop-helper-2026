"""Photoshop Helper 2026: command-line interface.

Parses command-line arguments, constructs a :class:`~core.Config`
instance, and delegates execution to :func:`core.run`.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser for the CLI.

    Returns:
        A fully configured :class:`argparse.ArgumentParser`.
    """
    parser = argparse.ArgumentParser(
        prog="photoshop-helper",
        description="Batch-process images in Adobe Photoshop with consistent filters "
                    "and automated layer organization.",
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="Directory containing source images to process.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=None,
        help="Directory for processed images (default: <input_dir>/processed).",
    )
    parser.add_argument(
        "-f",
        "--filter",
        choices=["brightness", "contrast", "saturation", "grayscale"],
        required=True,
        help="Filter to apply to every image.",
    )
    parser.add_argument(
        "--strength",
        type=float,
        default=1.0,
        help="Filter strength multiplier (default: 1.0).",
    )
    parser.add_argument(
        "--layer-prefix",
        type=str,
        default="PROC",
        help="Prefix for auto-generated layer names (default: 'PROC').",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recurse into subdirectories when collecting input files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report actions without invoking Photoshop.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point for the command-line interface.

    Args:
        argv: Optional list of command-line arguments. When ``None``,
              ``sys.argv[1:]`` is used.

    Returns:
        Process exit code (0 for success, non-zero for failure).
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    from core import Config, run

    config = Config(
        input_dir=args.input_dir,
        output_dir=args.output_dir or args.input_dir / "processed",
        filter_name=args.filter,
        strength=args.strength,
        layer_prefix=args.layer_prefix,
        recursive=args.recursive,
        dry_run=args.dry_run,
    )

    try:
        return run(config)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
