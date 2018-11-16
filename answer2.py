from sys import stdin

class Robot:
  headings = "NESW"
  heading_str2num = {l:i for i,l in enumerate(headings)}
  heading2movement = [(0,1), (-1,0), (0,-1), (1,0)]
  def __init__(self, board_size, loc, heading, moves):
    self.board_size = board_size
    self.x, self.y = loc
    self.heading = self.heading_str2num[heading]
    self.moves = moves
    self.move_index = 0

  def has_moves(self):
    return self.move_index < len(self.moves)
  
  def _move_forward(self):
    move_x, move_y = self.heading2movement[self.heading]
    new_x = self.x + move_x
    new_y = self.y + move_y
    if 0 <= new_x <= self.board_size[0] and 0 <= new_y <= self.board_size[1]:
      self.x, self.y = new_x, new_y
    else:
      raise Exception("Cannot move forward as robot would be out of bounds")

  def _rotate_heading(self, move):
    direction = -1 if move == 'R' else 1
    self.heading = (self.heading + direction) % 4

  def move(self):
    if not self.has_moves():
      raise Exception("Robot has no more moves")
    move = self.moves[self.move_index]
    self.move_index += 1
    if move == 'M':
      self._move_forward()
    else:
      self._rotate_heading(move)

  def __str__(self):
    headingstr = self.headings[self.heading]
    return "%d %d %s" % (self.x, self.y, headingstr)

def simulate(robot):
  while robot.has_moves():
    robot.move()

def parse_from_inp(inp):
  board_size = inp.readline().strip().split()
  board_size = (int(board_size[0]), int(board_size[1]))
  robots = []
  while 1:
    l1 = inp.readline()
    if not l1: # stdin is done
      break
    l1 = l1.strip().split()
    moves = inp.readline().strip()
    robot = Robot(board_size, (int(l1[0]), int(l1[1])), l1[2], moves)
    robots.append(robot)
  return board_size, robots


if __name__ == '__main__':
  board_size, robots = parse_from_inp(stdin)
  for robot in robots:
    simulate(robot)
    print(robot)

