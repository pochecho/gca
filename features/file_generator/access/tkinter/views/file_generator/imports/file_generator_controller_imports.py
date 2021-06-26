import json
import os
from tkinter import Button
from tkinter import Checkbutton
from tkinter import E
from tkinter import Entry
from tkinter import filedialog
from tkinter import Frame
from tkinter import IntVar
from tkinter import N
from tkinter import S
from tkinter import StringVar
from tkinter import W

from core.helpers.token_extractor.tokens_extractor import TokensExtractor
from features.file_generator.domain.models.models import Class
from features.file_generator.domain.use_cases.code_generator_use_case import CodeGeneratorUseCase