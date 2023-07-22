from pathlib import Path
from .common import MAP_PATH
from .warps import recursive_get_warps

from src.tmxpy import TMXpy
from PIL import Image



warps = recursive_get_warps('Farm')
print(warps)

output_img = 