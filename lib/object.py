import pyxel

from typing import Callable

from enums.object import Margin

class Object:
  width: int = 0
  height: int = 0
  x: float = 0
  y: float = 0
  dx: float = 0
  dy: float = 0
  margin: Margin = Margin()
  animation_id: int = 0
  animation_name: str | None = None
  animation_time: int = 0
  animations: dict[str, list[list[int]]] = {}
  is_hidden: bool = False


  def __init__(self) -> None:
    super(Object, self).__init__()

    self.animation_time = pyxel.frame_count


  def draw(self) -> None:
    if self.is_hidden or self.animation_name == None:
      return


    image: list[int] = self.animations[self.animation_name][self.animation_id]
    u: int = image[0]
    v: int = image[1]


    pyxel.blt(self.x, self.y, 0, u, v, self.width, self.height, 0)


  def animate(self, name: str, frames: float, callback: Callable | None = None) -> None:
    if self.animation_name == None:
      return


    if self.animation_name != name:
      self.animation_id = 0
      self.animation_name = name
      self.animation_time = pyxel.frame_count


    elapsed_frame: int = pyxel.frame_count - self.animation_time


    if elapsed_frame < frames:
      return


    self.animation_time = pyxel.frame_count
    self.animation_id += 1

    end_animation_id = len(self.animations[name]) - 1


    if self.animation_id >= end_animation_id:
      if callback != None:
        self.animation_id = end_animation_id
        callback()
      else:
        self.animation_id = 0


  def collided(self, object: "Object") -> bool:
    a_x1: float = self.x + self.margin.left
    a_x2: float = self.x + self.width - self.margin.right
    a_y1: float = self.y + self.margin.top
    a_y2: float = self.y + self.height - self.margin.bottom
    b_x1: float = object.x + object.margin.left
    b_x2: float = object.x + object.width - object.margin.right
    b_y1: float = object.y + object.margin.top
    b_y2: float = object.y + object.height - object.margin.bottom

    condition_x: list[int] = []
    condition_y: list[int] = []

    condition_x.append(a_x1 <= b_x1 and a_x2 >= b_x1 and a_x2 <= b_x2)
    condition_x.append(a_x1 >= b_x1 and a_x1 <= b_x2 and a_x2 >= b_x2)
    condition_x.append(a_x1 >= b_x1 and a_x1 <= b_x1 and a_x2 <= b_x2)
    condition_x.append(a_x1 <= b_x2 and a_x2 >= b_x1 and a_x2 >= b_x2)
    condition_x.append(a_x1 >= b_x2 and a_x1 <= b_x2 and a_x2 <= b_x2)
    condition_y.append(a_y1 <= b_y1 and a_y2 >= b_y1 and a_y2 <= b_y2)
    condition_y.append(a_y1 >= b_y1 and a_y1 <= b_y2 and a_y2 >= b_y2)
    condition_y.append(a_y1 >= b_y1 and a_y1 <= b_y1 and a_y2 <= b_y2)
    condition_y.append(a_y1 <= b_y2 and a_y2 >= b_y1 and a_y2 >= b_y2)
    condition_y.append(a_y1 >= b_y2 and a_y1 <= b_y2 and a_y2 <= b_y2)


    for x in list(condition_x):
      for y in list(condition_y):
        if x and y:
          return True


    return False
