import pyxel

import random
import time

from constants.settings import Settings
from enums.controls import Direction
from enums.gameover import Reason
from lib.scene import Scene
from objects.textbox import TextBox
from objects.crow import Crow
from objects.shroom import Shroom
from objects.spore import Spore


shroom: Shroom | None = None
spores: list[Spore] = []
crows: list[Crow] = []
instructions: TextBox | None = None
game_over: TextBox | None = None


class GameScene(Scene):
  __started: bool = False
  __game_over: bool = False
  __fps: int
  __time: int
  __elapsed: int
  __addition: int
  __total_time: int
  __frame_count: float
  __last_spore: int
  __last_crow: int
  __reason: Reason | None


  def __init__(self, width: int, height: int, fps: int) -> None:
    super().__init__(fps)

    self.screen_width = width
    self.screen_height = height
    self.__fps = fps

    self.init()


  def init(self) -> None:
    global shroom
    shroom = Shroom(Settings.start_x, Settings.start_y)

    global spores
    spores = []

    global crows
    crows = []

    # TODO: Fix the textbox rendering if I would come back to this project
    global instructions
    instructions = TextBox(
      ["Use arrow keys to jump!", "Press 'Space' to jump!", "Get spores to add time!", "Avoid the crows!"])

    global game_over
    game_over = None

    self.__game_over = False
    self.__time = Settings.start_time
    self.__elapsed = 0
    self.__addition = 0
    self.__total_time = 0
    self.__frame_count = pyxel.frame_count
    self.__last_spore = 0
    self.__last_crow = 0
    self.__reason = None

    pyxel.stop()


  def update(self) -> None:
    if not self.__started or self.__game_over:
      self.__start_game()

      return


    if shroom is not None:
      shroom.update()


    for crow in crows:
      crow.update()


      if crow.is_delete():
        crows.remove(crow)


    self.__elapsed = round((pyxel.frame_count - self.__frame_count) / self.__fps)
    self.__total_time = self.__time + self.__addition - self.__elapsed

    self.__add_spore()
    self.__add_crow()
    self.__define_collision()


    if self.__total_time <= 0:
      self.__reason = Reason.time_out
      self.__set_game_over()


  def __start_game(self) -> None:
    if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
      self.__started = True

      self.init()

      pyxel.playm(0, loop = True)


  def __add_spore(self) -> None:
    if self.__elapsed - self.__last_spore < Settings.spore_time:
      return


    index: int = random.randint(0, len(Settings.spore_spawn_list)) - 1
    spore_spawn: tuple[int, int] = Settings.spore_spawn_list[index]
    x: int = spore_spawn[0]
    y: int = spore_spawn[1]
    spore: Spore = Spore(x, y)

    spores.append(spore)

    self.__last_spore = self.__elapsed


  def __add_crow(self) -> None:
    if self.__elapsed - self.__last_crow < Settings.crow_time:
      return
    

    index: int = random.randint(0, len(Settings.crow_spawn_list)) - 1
    crow_spawn: tuple[int, int] = Settings.crow_spawn_list[index]
    x: int = crow_spawn[0]
    y: int = crow_spawn[1]
    crow: Crow = Crow(x, y)

    crow.x_direction = Direction.left


    if x < 0:
      crow.x_direction = Direction.right


    crows.append(crow)

    self.__last_crow = self.__elapsed


  def __define_collision(self) -> None:
    if shroom is None:
      return


    for spore in spores:
      if shroom.collided(spore) and not shroom.get_eating():
        spore.set_catch(True)
        shroom.set_eating(True)

        spores.remove(spore)

        self.__addition += Settings.add_score

        pyxel.play(3, 13)

        break


    for crow in crows:
      if shroom.collided(crow):
        self.__reason = Reason.crow
        self.__set_game_over()


  def __set_game_over(self) -> None:
    if self.__game_over or shroom is None:
      return


    self.__game_over = True

    shroom.disabled_controls = True

    pyxel.stop()
    pyxel.play(0, 11)

    time.sleep(2)

    global game_over


    if self.__reason == Reason.time_out:
      game_over = TextBox(["\nOpps Time's out!", "\nTry again?"])
    elif self.__reason == Reason.crow:
      game_over = TextBox(["\nYou were eaten by a crow", "\nTry again?"])


  def draw(self) -> None:
    pyxel.cls(0)

    self.__draw_background()

    pyxel.camera()
    pyxel.bltm(0, 0, 0, 0, 0, self.screen_width, self.screen_height, 0)


    if shroom is not None:
      shroom.draw()


    for crow in crows:
      crow.draw()


    for spore in spores:
      spore.draw()


    if not self.__started and instructions is not None:
      instructions.draw()


    if self.__game_over and game_over is not None:
      game_over.draw()


    pyxel.text(5, 5, "TIME:" + str(self.__total_time), 7)


  def __draw_background(self) -> None:
    y: int = Settings.bg_y


    for index in range(Settings.bg_range):
      color: int = Settings.bg_color[index]
      height: int = Settings.bg_height[index]

      pyxel.rect(0, y, Settings.width, height, color)


      for line in range(1, Settings.bg_range - index + 2, 2):
        line_color: int = Settings.bg_line[index]

        pyxel.line(0, y + line, Settings.width, y + line, line_color)


      y += height
