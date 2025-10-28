import pytest
from huskypo import Timeout, Offset

from framework import common, path
# from module.ios.cube.zh_common import CubeCommon

Timeout.DEFAULT = 30
Offset.UP = (0.5, 0.75, 0.5, 0.25)
Offset.DOWN = (0.5, 0.25, 0.5, 0.75)
Offset.LEFT = (0.75, 0.5, 0.25, 0.5)
Offset.RIGHT = (0.25, 0.5, 0.75, 0.5)


# @pytest.fixture(scope='function', autouse=True)
# def pre_login(request):
#     """
#     執行登入前的判斷，包括launching, queueing, 以及inform
#     """
#     if request.node.get_closest_marker('skip_pre_login'):
#         return
#
#     cube = request.getfixturevalue('cube')
#     aws = request.getfixturevalue('aws')