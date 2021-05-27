from distutils.core import setup
from PIL import Image, ImageTk
import py2exe

import pytest

setup(windows=['app.py'])