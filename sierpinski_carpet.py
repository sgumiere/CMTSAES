"""Sierpinski Carpet fractal generator using matplotlib."""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def sierpinski_carpet(ax, x, y, size, depth):
    """Recursively draw a Sierpinski carpet.

    Args:
        ax: Matplotlib axes to draw on.
        x, y: Bottom-left corner coordinates.
        size: Side length of the current square.
        depth: Remaining recursion depth.
    """
    if depth == 0:
        return

    sub = size / 3
    # Remove the center square
    ax.add_patch(patches.Rectangle((x + sub, y + sub), sub, sub, color="white"))

    # Recurse into the 8 surrounding sub-squares
    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:
                continue  # skip center
            sierpinski_carpet(ax, x + col * sub, y + row * sub, sub, depth - 1)


def main():
    depth = 5
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # Start with a filled black square
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, color="black"))

    # Carve out the carpet pattern
    sierpinski_carpet(ax, 0, 0, 1, depth)

    plt.title(f"Sierpinski Carpet (depth {depth})", fontsize=16, pad=12)
    plt.tight_layout()
    plt.savefig("sierpinski_carpet.png", dpi=200, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
