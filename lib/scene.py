import pyxel

from typing import Callable

from enums.scene import FadeType

FADE_PALETTE_1: list[int] = [0, 0, 0, 1, 2, 1, 5, 13, 2, 4, 9, 3, 5, 1, 9, 10]
FADE_PALETTE_2: list[int] = [0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 4, 1, 1, 0, 2, 4]
FADE_PALETTE_3: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class Scene:
  def __init__(self, fps: int) -> None:
    self.__fps: int = fps
    self.__time: int = self.__set_time()
    self.__fade_start_time: int = 0
    self.__fade_time: int = 0
    self.__fade_type: FadeType | None = None
    self.__fade_callback: Callable | None = None


  def update(self) -> None:
    self.__time = self.__set_time()


    if (self.__fade_type != None):
      self.__do_fade()


  def __set_time(self) -> int:
    return round(pyxel.frame_count / self.__fps * 1000)


  def __do_fade(self) -> None:
    time: float = (self.__time - self.__fade_start_time) / self.__fade_time
    palette: list[int] | None = None


    if time <= 0.33:
      palette = FADE_PALETTE_1 \
        if self.__fade_type == FadeType.fade_out else FADE_PALETTE_3
    elif time <= 0.67:
      palette = FADE_PALETTE_2
    elif time <= 1:
      palette = FADE_PALETTE_3 \
        if self.__fade_type == FadeType.fade_out else FADE_PALETTE_1
    else:
      if self.__fade_type == FadeType.fade_in:
        pyxel.pal()


      if self.__fade_callback != None:
        self.__fade_callback()


      self.__fade_type = None
      self.__fade_callback = None

      return


    for col1, col2 in enumerate(palette):
      pyxel.pal(col1, col2)


  def fade_out(self, time: int, callback: Callable | None = None) -> None:
    if self.__fade_type == None:
      self.__fade_type = FadeType.fade_out
      self.__fade_start_time = self.__time
      self.__fade_time = time
      self.__fade_callback = callback


  def fade_in(self, time: int, callback: Callable | None = None) -> None:
    if self.__fade_type == None:
      self.__fade_type = FadeType.fade_in
      self.__fade_start_time = self.__time
      self.__fade_time = time
      self.__fade_callback = callback
