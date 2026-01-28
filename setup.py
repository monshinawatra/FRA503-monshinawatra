import os
import toml

from setuptools import setup
from pathlib import Path

# Obtain the extension data from the extension.toml file
EXTENSION_PATH = Path(__file__).parent.resolve()
# Read the extension.toml file
EXTENSION_TOML_DATA = toml.load(EXTENSION_PATH / "config" / "extension.toml")

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    # generic
    "numpy",
    "torch==2.5.1",
    "torchvision>=0.14.1",  # ensure compatibility with torch 1.13.1
    # 5.26.0 introduced a breaking change, so we restricted it for now.
    # See issue https://github.com/tensorflow/tensorboard/issues/6808 for details.
    "protobuf>=3.20.2, < 5.0.0",
    # basic logger
    "tensorboard",
]

PYTORCH_INDEX_URL = ["https://download.pytorch.org/whl/cu118"]

# Installation operation
setup(
    name="rlenv",
    packages=["rlenv"],
    version="0.0.1",
    zip_safe=False,
)
