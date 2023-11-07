import pyxel

from typing import Final
from constants.settings import Settings

from enums.object import Margin
from lib.platformer import Platformer
from lib.platformer import Direction


WIDTH: Final[int] = 16
HEIGHT: Final[int] = 16
MARGIN: Margin = Margin(6, 4, 4, 4)


class Crow(Platformer):
  __is_hurt: bool = False
  __move_speed = Settings.crow_speed


  def __init__(self, x, y) -> None:
    super(Crow, self).__init__()

    self.width = WIDTH
    self.height = HEIGHT
    self.x = x
    self.y = y
    self.animation_name = "move_left"
    self.animations = {
      "move_left": [[64, 16], [64, 32], [64, 48], [64, 64]],
      "move_right": [[80, 16], [80, 32], [80, 48], [80, 64]],
      "hurt_left": [[64, 80], [64, 96]],
    }
    self.tilemap = 0
    self.gravity = 0
    self.disabled_controls = True
    self.tile_width = WIDTH
    self.tile_height = HEIGHT
    self.x_direction = Direction.left
    self.margin = MARGIN


  def update(self) -> None:
    super(Crow, self).update()

    if self.x_direction == Direction.left:
      self.x -= self.__move_speed
      self.animate("move_left", 7.5)
    elif self.x_direction == Direction.right:
      self.x += self.__move_speed
      self.animate("move_right", 7.5)


  def set_move_speed(self, move_speed: int) -> None:
    self.__move_speed = move_speed


  def is_delete(self) -> bool:
    return self.x_direction == Direction.left and self.x < -self.width or \
      self.x_direction == Direction.right and self.x > Settings.width
