#import tmxpy does not work
import sys, random, time, argparse
from pathlib import Path

#sys.path.append('..')

#from src.tmxpy import TMXpy#, hello#
from tmxpy import TMXpy

#parser = argparse.ArgumentParser(description='Render a TMX file.')
#parser.add_argument('map', metavar='map', type=str, nargs=1, help='The path to the TMX file to render.')

MAP_PATH = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Stardew Valley\\Content (unpacked)\\Maps'

def farm():
    tmx = TMXpy(
        [Path(MAP_PATH)],
        path="tests\\Farm.tmx")
                
    #print(tmx.__dict__)

    tmx.generateGIDDict()

    # random.seed = time.time()
    # randomlySelectedTile = random.choice(list(tmx.tiles.keys()))
    # print(randomlySelectedTile)

    #tmx.renderLayer(1).save("tests\\render.png")
    tmx.renderAllLayers().save("tests\\render-farm.png")


def render(name: str):
    tmx = TMXpy(
        [Path(MAP_PATH)],
        path=Path.joinpath(Path(MAP_PATH), name + ".tmx"))
                
    #print(tmx.__dict__)

    tmx.generateGIDDict()

    # random.seed = time.time()
    # randomlySelectedTile = random.choice(list(tmx.tiles.keys()))
    # print(randomlySelectedTile)

    #tmx.renderLayer(1).save("tests\\render.png")
    tmx.renderAllLayers(blocked=['3']).save(f"tests\\render-{name}.png")

for x in ['SeedShop']:
    render(x)