# coding=UTF-8

from random import randrange
import time
from ui import *
import core
import player
import skill

List = {
  'Poring': {
    'lv': 1,
    'hp': 60,
    'atk': 8,
    'exp': 20
  },
  'Lunatic': {
    'lv': 3,
    'hp': 55,
    'atk': 11,
    'exp': 27,
    'skills': [
      ['Heal', 20, 1]
    ]
  },
  'Pupa': {
    'lv': 4,
    'hp': 66,
    'atk': 0,
    'matk': 30,
    'exp': 27,
    'skills': [
      ['Heal', 30, 2]
    ]
  },
  'Fabre': {
    'lv': 6,
    'hp': 72,
    'atk': 12,
    'exp': 54
  },
  'Hornet': {
    'lv': 11,
    'hp': 90,
    'atk': 13,
    'exp': 60,
    'skills': [
      ['Lightening Bolt', 20, 1]
    ]
  },
  'Savage Babe': {
    'lv': 14,
    'hp': 180,
    'atk': 19,
    'exp': 90,
    'skills': [
      ['Heal', 30, 1]
    ]
  },
  'Rocker': {
    'lv': 15,
    'hp': 185,
    'atk': 19,
    'exp': 99
  },
  'Thief Bug': {
    'lv': 21,
    'hp': 354,
    'atk': 56,
    'exp': 126,
    'skills': [
      ['Envenom', 20, 1]
    ]
  },
  'Tarou': {
    'lv': 22,
    'hp': 420,
    'atk': 72,
    'exp': 135
  },
  'Familiar': {
    'lv': 24,
    'hp': 427,
    'atk': 68,
    'exp': 144
  },
  'Thief Bug Egg': {
    'lv': 20,
    'hp': 344,
    'atk': 0,
    'matk': 100,
    'exp': 126,
    'skills': [
      ['Heal', 30, 2]
    ]
  },
  'Spore': {
    'lv': 18,
    'hp': 280,
    'atk': 25,
    'exp': 87,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Plankton': {
    'lv': 40,
    'hp': 1232,
    'atk': 75,
    'exp': 334,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Poison Spore': {
    'lv': 26,
    'hp': 456,
    'atk': 68,
    'exp': 163,
    'skills': [
      ['Envenom', 20, 1]
    ]
  },
  'Female Thief Bug': {
    'lv': 28,
    'hp': 531,
    'atk': 42,
    'exp': 180,
    'skills': [
      ['Heal', 20, 2]
    ]
  },
  'Male Thief Bug': {
    'lv': 30,
    'hp': 595,
    'atk': 46,
    'exp': 198,
    'skills': [
      ['Envenom', 20, 1]
    ]
  },
  'Drainliar': {
    'lv': 47,
    'hp': 1162,
    'atk': 100,
    'exp': 389,
    'skills': [
      ['Envenom', 20, 2]
    ]
  },
  'Cramp': {
    'lv': 82,
    'hp': 3898,
    'atk': 435,
    'exp': 972,
    'skills': [
      ['Envenom', 20, 3]
    ]
  },
  'Hydra': {
    'lv': 34,
    'hp': 854,
    'atk': 35,
    'exp': 233,
    'skills': [
      ['Heal', 20, 1]
    ]
  },
  'Kukre': {
    'lv': 42,
    'hp': 1111,
    'atk': 65,
    'exp': 315,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Marina': {
    'lv': 42,
    'hp': 1209,
    'atk': 73,
    'exp': 340,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Vadon': {
    'lv': 45,
    'hp': 1252,
    'atk': 78,
    'exp': 342,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Marse': {
    'lv': 47,
    'hp': 1456,
    'atk': 85,
    'exp': 389,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Obeaune': {
    'lv': 53,
    'hp': 2158,
    'atk': 107,
    'exp': 476,
    'skills': [
      ['Cold Bolt', 20, 2]
    ]
  },
  'Merman': {
    'lv': 60,
    'hp': 2940,
    'atk': 131,
    'exp': 616,
    'skills': [
      ['Cold Bolt', 20, 2]
    ]
  },
  'Marine Sphere': {
    'lv': 51,
    'hp': 1924,
    'atk': 99,
    'exp': 446,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Phen': {
    'lv': 52,
    'hp': 1963,
    'atk': 102,
    'exp': 446,
    'skills': [
      ['Cold Bolt', 20, 1]
    ]
  },
  'Swordfish': {
    'lv': 57,
    'hp': 2600,
    'atk': 156,
    'exp': 525,
    'skills': [
      ['Cold Bolt', 20, 2]
    ]
  },
  'Deviace': {
    'lv': 60,
    'hp': 3135,
    'atk': 168,
    'exp': 658,
    'skills': [
      ['Cold Bolt', 20, 3]
    ]
  },
  'Strouf': {
    'lv': 61,
    'hp': 3052,
    'atk': 170,
    'exp': 626,
    'skills': [
      ['Cold Bolt', 30, 3]
    ]
  }
}

class Mob:
  def __init__(self, name):
    self.name = name
    self.db = List[name]
    self.lv = self.db['lv']
    self.hp = randrange(self.db['hp'], self.db['hp'] + self.lv)
    self.max_hp = self.hp
    self.exp = randrange(self.db['exp'], self.db['exp'] + self.lv)
    self.zeny = randrange(self.exp, self.exp + self.lv)
    self.status = {}

  def mhp(self):
    return self.max_hp

  def atk(self):
    if self.db['atk'] == 0:
      return 0
    else:
      return randrange(self.db['atk'], self.db['atk'] + self.lv)

  def matk(self):
    if 'matk' not in self.db:
      return int(self.atk() * 1.5)
    else:
      return randrange(self.db['matk'], self.db['matk'] + self.lv)

  def _attack(self, source, target):
    if len(target.status.keys()) > 0:
      for name, dmg in target.status.iteritems():
        if dmg > target.hp:
          dmg = target.hp
        if dmg > 0:
          target.hp -= dmg
          ui.mes(source.name, 'Attack ' + target.name + ' with ' + ui.green(name + ' ' + str(dmg)) + ' damage. [' + str(target.hp) + '/' + str(target.mhp()) + ']', False)
          if target.hp == 0:
            break

    skill_data = []
    if isinstance(source, Mob) and 'skills' in List[source.name]:
      skill_data = core.rand(List[source.name]['skills'])
    elif isinstance(source, player.Player) and len(source.skills.keys()) > 0 and randrange(100) < (source.int / float(source.int + source.str) * 100):
      name = source.skills.keys()[randrange(len(source.skills.keys()))]
      skill_data = [name, 0, source.skills[name]]
    if len(skill_data) > 0:
      if skill_data[0] != 'Heal' or source.hp != source.mhp():
        skill.use(skill_data[0], skill_data[2], source, target)
        return

    dmg = source.atk()
    if dmg == 0:
      return
    elif dmg > target.hp:
      dmg = target.hp
    time.sleep(0.8)
    target.hp -= dmg
    ui.mes(source.name, 'Attack ' + target.name + ' with ' + ui.green(str(dmg)) + ' damage. [' + str(target.hp) + '/' + str(target.mhp()) + ']', False)
    
  def be_attacked(self, source):
    self._attack(source, self)

  def attack(self, target):
    self._attack(self, target)

  def dead(self, source):
    ui.mes(self.name, 'Noooo!', False)
    source.status = {}
    source.hp = source.mhp()
    source.add_exp(self.exp)
    source.add_zeny(self.zeny)
