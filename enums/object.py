from dataclasses import dataclass

@dataclass
class Margin:
  top: int = 0
  bottom: int = 0
  left: int = 0
  right: int = 0

  def __init__(self, top = 0, bottom = 0, left = 0, right = 0) -> None:
    self.top = top
    self.bottom = bottom
    self.left = left
    self.right = right
