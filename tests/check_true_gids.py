from .common import *
from src.tmxpy import TMXpy, convertMapNameToFile
from pathlib import Path
import json

tmx = TMXpy(
    [Path(MAP_PATH)],
    path=Path.joinpath(Path(MAP_PATH), "Farm.tmx")
)

tmx.generateGIDDict()

print(json.dumps(tmx.trueGIDDict, indent=4))