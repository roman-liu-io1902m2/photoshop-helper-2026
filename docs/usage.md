# Usage

This document describes how to use **photoshop-helper-2026**.

## Install

```bash
pip install -e .
```

## Basic example

```python
from photoshop_helper_2026.core import Config, run

cfg = Config(verbose=True, targets=["alpha", "beta"])
run(cfg)
```

## CLI

```bash
photoshop_helper_2026 alpha beta -v
```

## Theme

This project is oriented around: A Python-based utility for automating repetitive tasks in Adobe Photoshop. It allows users to batch process images and apply consistent filters. The tool includes a feature for automated layer organization and naming conventions..
