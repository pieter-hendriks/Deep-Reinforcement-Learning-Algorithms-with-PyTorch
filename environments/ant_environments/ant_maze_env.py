

# NOTE THIS CODE IS TAKEN FROM https://github.com/tensorflow/models/tree/master/research/efficient-hrl/environments
# and is not my code.



from .maze_env import MazeEnv
from .ant import AntEnv


class AntMazeEnv(MazeEnv):
    MODEL_CLASS = AntEnv
