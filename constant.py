# SETTING
STOPWATCH_TIME = 5
HINT_TIME = 5
ICON_NAME = "brain.png"

# PATH
IMAGE_PATH = "./venv/Component/Images/"
ICON_PATH = "./venv/Component/Icons/"

# LABEL
LEVEL_LABEL_HEIGHT = 30
TIME_LABEL_HEIGHT = 80

# WINDOW
WINDOW_WIDTH = int(1200)
WINDOW_HEIGHT = int(800)
WINDOW_X = int(300)
WINDOW_Y = int(300)

# BUTTON
BUTTON_WIDTH = int(130)
BUTTON_HEIGHT = int(50)
BUTTON_MARGIN = int(10)
START_BUTTON_X = (WINDOW_WIDTH-BUTTON_WIDTH)/2
START_BUTTON_Y = WINDOW_HEIGHT - (BUTTON_HEIGHT + BUTTON_MARGIN)

# GRID
GRID_MARGIN = 10
GRID_WIDTH = WINDOW_WIDTH - GRID_MARGIN * 2
GRID_HEIGHT = WINDOW_HEIGHT - BUTTON_HEIGHT - TIME_LABEL_HEIGHT - LEVEL_LABEL_HEIGHT

# IMAGE_TILE
IMAGE_TILE_COUNT = 16
IMAGE_TILE_HEIGHT = GRID_HEIGHT / 4