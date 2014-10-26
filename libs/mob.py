# coding=UTF-8

from random import randrange
import time
from ui import *
import player

List = {
  'Poring': {
    'hp': [8, 10],
    'atk': [1, 2],
    'exp': [2, 4],
    'items': {
      'Red Potion': 40,
      'Blue Potion': 10,
      'Knife': 1
    }
  },
  'Lunatic': {
    'hp': [16, 20],
    'atk': [3, 6],
    'exp': [4, 8],
    'items': {
      'Red Potion': 60,
      'Blue Potion': 20,
      'Knife': 5
    }
  }
}

class Mob(object):
  def __init__(self, name):
    super(Mob, self).__init__()
    self.name = name
    self.db = List[name]
    self.hp = randrange(self.db['hp'][0], self.db['hp'][1])
    self.max_hp = self.hp
    self.exp = randrange(self.db['exp'][0], self.db['exp'][1])
    self.items = []

    for name, per in self.db['items'].iteritems():
      if randrange(100) < per:
        self.items.append([name, 1])

  def mhp(self):
    return self.max_hp

  def atk(self):
    return randrange(self.db['atk'][0], self.db['atk'][1])

  def _attack(self, source, target):
    time.sleep(1)
    dmg = source.atk()
    if dmg > target.hp:
      dmg = target.hp
    target.hp -= dmg
    ui.mes(source.name, 'Attack ' + target.name + ' with ' + ui.green(str(dmg)) + ' damage. [' + str(target.hp) + '/' + str(target.mhp()) + ']', False)
    
  def be_attacked(self, source):
    self._attack(source, self)

  def attack(self, target):
    self._attack(self, target)

  def dead(self, source):
    ui.mes(self.name, 'Noooo!', False)
    source.add_exp(self.exp)
    source.add_item(self.items)
