import pyxel

from constants.settings import Settings


class TextBox():
  __text_list: list[str] = []


  def __init__(self, text_list: list[str]):
    self.__text_list = text_list


  def draw(self) -> None:
    size: list[int] = Settings.text_box_size
    padding: int = Settings.text_box_padding

    pyxel.rect(size[0], size[1], size[2], size[3], Settings.text_box_bg)


    index: int = 0


    for text in self.__text_list:
      x: int = size[0] + padding
      y: int = size[1] + padding + (index * Settings.text_box_line_height)

      pyxel.text(x, y, text, Settings.text_box_color)

      index += 1


    start_text: str = "PRESS 'SPACE' TO START"
    
    pyxel.text(Settings.width / 2 - len(start_text) / 2 * 8 / 2, 108, start_text, Settings.text_box_color)

