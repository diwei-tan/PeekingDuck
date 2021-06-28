from typing import List, Tuple, Any, Iterable, Union
import numpy as np
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX, LINE_AA
import peekingduck.pipeline.nodes.draw.utils.constants as constants
from peekingduck.pipeline.nodes.draw.utils.general import \
    get_image_size, project_points_onto_original_image


def draw_count(frame: np.array, count: int) -> None:
    """draw count of selected object onto frame

    Args:
        frame (np.array): image of current frame
        count (int): total count of selected object
            in current frame
    """
    text = 'COUNT: {0}'.format(count)
    cv2.putText(frame, text, (10, 50), FONT_HERSHEY_SIMPLEX,
                0.75, COUNTING_TEXT_COLOR, 2, LINE_AA)


def draw_fps(frame: np.array, current_fps: float) -> None:
    """ Draw FPS onto frame image

    Args:
        frame (np.array): image of current frame
        current_fps (float): value of the calculated FPS
    """
    text = "FPS: {:.05}".format(current_fps)
    text_location = (25, 25)

    cv2.putText(frame, text, text_location, FONT_HERSHEY_SIMPLEX, FONT_SCALE,
                PINK_COLOR, FONT_THICKNESS, LINE_AA)