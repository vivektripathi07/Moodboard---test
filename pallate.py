import random
import colorsys

def generate_random_palette(n_colors=5, brightness_min=0.4, brightness_max=0.9, saturation_min=0.5, saturation_max=0.9):
    """
    Generate a random but visually balanced color palette.

    Args:
        n_colors (int): Number of colors in the palette (default: 5)
        brightness_min (float): Min brightness (value in HSV) - 0 to 1
        brightness_max (float): Max brightness - 0 to 1
        saturation_min (float): Min saturation - 0 to 1
        saturation_max (float): Max saturation - 0 to 1

    Returns:
        list: List of hex color strings (e.g., ['#FF5733', '#33A8FF', ...])
    """
    palette = []

    for _ in range(n_colors):
        # Random hue (0 to 1) - full color spectrum
        h = random.random()

        # Controlled saturation and brightness for better aesthetics
        s = random.uniform(saturation_min, saturation_max)
        v = random.uniform(brightness_min, brightness_max)

        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # Convert to 0-255 range and to hex
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        # Format as hex
        hex_color = f"#{r:02X}{g:02X}{b:02X}"
        palette.append(hex_color)

    return palette