from .common import *
from src.tmxpy import *
from pathlib import Path
import json, os

INPUT_TMX = str(Path.joinpath(
    Path(os.getcwd()), 
    Path('tests'), 
    Path('Farm-XML.tmx')
))

XMLtoCSV(INPUT_TMX, INPUT_TMX.replace('-XML', '-CSV'))