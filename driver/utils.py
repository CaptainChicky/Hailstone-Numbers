"""Shared utilities for Collatz/hailstone visualization drivers."""

import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt

import os


def is_prime(n):
    """Check if n is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_cmap(n, name="hsv"):
    """Get a colormap with n discrete colors."""
    return mpl.colormaps[name].resampled(n)


def setup_output():
    """Create and return the output directory path."""
    output_directory = "generated"
    os.makedirs(output_directory, exist_ok=True)
    return output_directory


def save_figure(
    filepath,
    dpi=500,
    watermark_x=0.075,
    watermark_y=0.065,
    halign="center",
    left=0.15,
    bottom=0.1,
    fmt=None,
):
    """Add watermark and save the figure."""
    txt = "Made by Chicky"
    plt.figtext(
        watermark_x,
        watermark_y,
        txt,
        wrap=True,
        horizontalalignment=halign,
        fontsize=8,
        color="grey",
    )
    plt.tight_layout()
    plt.subplots_adjust(left=left, bottom=bottom)
    save_kwargs = {"dpi": dpi}
    if fmt:
        save_kwargs["format"] = fmt
    plt.savefig(filepath, **save_kwargs)
