from typing import Final


class Settings:
  pyxres_filename: Final[str] = "shroomy_shroom.pyxres"
  title: Final[str] = "Shroomy Shroom"
  width: Final[int] = 128
  height: Final[int] = 128
  fps: Final[int] = 60
  bg_y: Final[int] = 16
  bg_color: Final[list[int]] = [1, 5, 12, 6]
  bg_height: Final[list[int]] = [32, 24, 16, 8]
  bg_range: Final[int] = 4
  bg_line: Final[list[int]] = [0, 1, 5, 12]
  start_x: Final[int] = 56
  start_y: Final[int] = 80
  start_time: Final[int] = 30
  spore_time: Final[int] = 5
  spore_spawn_list: Final[list[tuple[int, int]]] = [
    (0, 48), (16, 64), (32, 80), (48, 80),
    (64, 80), (80, 80), (72, 80), (96, 80),
  ]
  add_score: Final[int] = 5
  crow_time: Final[int] = 2
  crow_spawn_list: Final[list[tuple[int, int]]] = [
    (-16, 48), (-16, 64), (-16, 80),
    (128, 48), (128, 64), (128, 80),
  ]
  crow_speed: Final[float] = 0.5
  text_box_size: Final[list[int]] = [8, 56, 112, 64]
  text_box_bg: int = 0
  text_box_color: int = 7
  text_box_padding: int = 8
  text_box_line_height: int = 10
