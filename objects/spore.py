from typing import Final

from enums.object import Margin
from lib.platformer import Platformer
from lib.platformer import Direction


WIDTH: Final[int] = 16
HEIGHT: Final[int] = 16
MARGIN: Margin = Margin(6, 6, 6, 6)


class Spore(Platformer):
  __is_catch: bool = False


  def __init__(self, x, y) -> None:
    super(Spore, self).__init__()

    self.width = WIDTH
    self.height = HEIGHT
    self.x = x
    self.y = y
    self.animation_name = "default"
    self.animations = {
      "default": [[0, 96]],
      "animate": [[0, 96], [16, 96], [32, 96], [48, 96]],
    }
    self.tilemap = 0
    self.tile_width = WIDTH
    self.tile_height = HEIGHT
    self.margin = MARGIN


  def update(self) -> None:
    super(Spore, self).update()


    if self.__is_catch:
      self.animate("default", 0)
    else:
      self.animate("animate", 6)


  def set_catch(self, is_catch: bool) -> None:
    self.__is_catch = is_catch
