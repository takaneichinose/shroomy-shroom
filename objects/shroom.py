import pyxel

from typing import Final
from constants.settings import Settings

from enums.object import Margin
from lib.platformer import Platformer
from lib.platformer import Direction


WIDTH: Final[int] = 16
HEIGHT: Final[int] = 16
MOVE_SPEED: Final[float] = 0.05
JUMP_SPEED: Final[float] = 3
MAX_DX: Final[int] = 1
MAX_DY: Final[int] = 4
BOUNCE: Final[float] = 0.5
MARGIN: Margin = Margin(4, 0, 2, 2)


class Shroom(Platformer):
  __is_eating: bool = False

  def __init__(self, x, y) -> None:
    super(Shroom, self).__init__()

    self.width = WIDTH
    self.height = HEIGHT
    self.x = x
    self.y = y
    self.animation_name = "idle_left"
    self.animations = {
      "idle_left": [[16, 16], [16, 32], [16, 48], [16, 32]],
      "idle_right": [[0, 16], [0, 32], [0, 48], [0, 32]],
      "walk_left": [[16, 64], [16, 32], [16, 80], [16, 32]],
      "walk_right": [[0, 64], [0, 32], [0, 80], [0, 32]],
      "jump_left": [[16, 80]],
      "jump_right": [[0, 80]],
      "eat_left": [[48, 16], [48, 32], [48, 48]],
      "eat_right": [[32, 16], [32, 32], [32, 48]],
    }
    self.tilemap = 0
    self.tile_width = WIDTH
    self.tile_height = HEIGHT
    self.acceleration = MOVE_SPEED
    self.jump_speed = JUMP_SPEED
    self.max_dx = MAX_DX
    self.max_dy = MAX_DY
    self.bounce = BOUNCE
    self.x_direction = Direction.left
    self.margin = MARGIN
    self.solid_tilemap = 0
    self.solid_list = list(((x, y) for x in range(6) for y in [14, 15]))
    self.is_flip = False


  def update(self) -> None:
    if self.is_ground and (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A)):
      pyxel.play(3, 12)


    super(Shroom, self).update()


    if self.x + self.margin.left < 0:
      self.x = -self.margin.left
    elif self.x + self.width - self.margin.right > Settings.width:
      self.x = Settings.width - (self.width - self.margin.right)


    self.is_flip = self.x_direction == Direction.left


    self.__create_animation()


  def __after_eat_animation(self):
    face: str = "left" if self.is_flip else "right"

    self.animation_name = "idle_" + face
    self.set_eating(False)


  def __create_animation(self) -> None:
    face: str = "left" if self.is_flip else "right"

    if self.__is_eating:
      self.animate("eat_" + face, 7.5, self.__after_eat_animation)
    elif self.is_jumping or self.is_falling:
      self.animate("jump_" + face, 0)
    elif self.is_ground:
      if self.is_walking:
        self.animate("walk_" + face , 6)
      else:
        self.animate("idle_" + face, 8)

  
  def set_eating(self, is_eating: bool) -> None:
    self.__is_eating = is_eating
    self.disabled_controls = is_eating


  def get_eating(self) -> bool:
    return self.__is_eating
