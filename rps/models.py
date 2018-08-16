from csv import DictReader
import json
import os
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont


module_path = __file__
pwd = '/'.join(module_path.split('/')[:-1])
ASSET_DIR = os.path.join(pwd, 'data')
DATA = os.path.join(ASSET_DIR, 'battle-table.csv')
SPRITE_MAP = os.path.join(ASSET_DIR, 'plays.json')
SPRITE_SHEET = os.path.join(ASSET_DIR, 'plays.png')
MARKER = os.path.join(ASSET_DIR, 'lose.png')


class Player:
    def __init__(self, name):
        self.name = name.title()
        self.score = 0

    def __str__(self):
        return self.name

    def won(self):
        self.score += 1


class Roll:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def _rolls(self):
        with open(DATA) as fin:
            reader = DictReader(fin)
            for row in reader:
                if row['Attacker'] == self.name:
                    yield row
                else:
                    continue

    def can_defeat(self, other_roll):
        return other_roll.name in self.win

    @property
    def lose(self):
        pwned = []
        for row in self._rolls():
            for key in row.keys():
                if row[key] == 'lose':
                    pwned.append(key)
        return pwned

    @property
    def win(self):
        wins = []
        for row in self._rolls():
            for key in row.keys():
                if row[key] == 'win':
                    wins.append(key)
        return wins


class Sprite:
    DEFAULT_WIDTH = 250
    DEFAULT_HEIGHT = 100
    DEFAULT_CANVAS_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)
    BG_COLOR = (108, 122, 128)
    FONT_COLOR = (59, 201, 193)
    FONT_TYPE = os.path.join(ASSET_DIR, 'Ubuntu-R.ttf')
    FONT_SIZE = 42
    FONT_PADDING_HOR = 0
    FONT_PADDING_VERT = 20

    def __init__(self, player_roll, pc_roll, loser=None, text='vs'):
        self.player_roll = player_roll
        self.pc_roll = pc_roll
        self.text = text
        self.plays = plays()
        self.loser = loser

        self.gen_image()

    def get_sprite(self, roll):
        region = self.plays[roll.name]
        ss = Image.open(SPRITE_SHEET)
        sprite = ss.crop(region)
        return sprite

    def gen_image(self):
        image = Image.new('RGB', self.DEFAULT_CANVAS_SIZE, self.BG_COLOR)
        player_sprite = self.get_sprite(self.player_roll)
        pc_sprite = self.get_sprite(self.pc_roll)
        player_offset = (10, 10)
        pc_offset = (self.DEFAULT_WIDTH - 92, 10)

        if self.loser == 'player':
            player_sprite = self.mark(player_sprite)
        elif self.loser == 'pc':
            pc_sprite = self.mark(pc_sprite)

        image.paste(player_sprite, player_offset, player_sprite)
        image.paste(pc_sprite, pc_offset, pc_sprite)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(self.FONT_TYPE, self.FONT_SIZE)
        text_offset = (107, self.FONT_PADDING_VERT, self.FONT_PADDING_HOR)
        draw.text(text_offset, self.text, self.FONT_COLOR, font=font)
        image.show()

    @staticmethod
    def mark(sprite):
        marker = Image.open(MARKER)
        marker_offset = (0, 0)
        sprite.paste(marker, marker_offset, marker)
        return sprite


def load_map(file: str) -> dict:
    with open(file) as s_map:
        data = json.loads(s_map.read())
    return data['frames']


def plays() -> defaultdict:
    frames = load_map(SPRITE_MAP)
    sprites = defaultdict(dict)

    for frame in frames:
        filename = frame['filename'].split('.')[0]
        x = frame['frame']['x']
        y = frame['frame']['y']
        w = x + frame['sourceSize']['w']
        h = y + frame['sourceSize']['h']
        sprites[filename.title()] = (x, y, w, h)

    return sprites
