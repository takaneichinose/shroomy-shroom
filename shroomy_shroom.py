import pyxel


from constants.settings import Settings
from scenes.game_scene import GameScene


width: int = Settings.width
height: int = Settings.height
fps: int = Settings.fps


pyxel.init(width, height, title = Settings.title, fps = fps)

game_scene: GameScene = GameScene(width, height, fps)


def update() -> None:
  game_scene.update()


def draw() -> None:
  game_scene.draw()


pyxel.load(filename = Settings.pyxres_filename)
pyxel.run(update, draw)
