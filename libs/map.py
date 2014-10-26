# coding=UTF-8

import sys
from random import randrange
from ui import *
import core
import npc
import mob
import item

List = {
  'Prontera': {
    'npcs': {
      'Healing Dealer': True,
      'Weapon Dealer': True,
      'Recycler': True,
      'Cecily': True
    },
    'warps': ['Prontera West Field', 'Prontera South Field']
  },
  'Prontera West Field': {
    'mobs': [
      ['Poring', 30],
      ['Lunatic', 30],
      ['Fabre', 20],
      ['Hornet', 10],
      ['Pupa', 10]
    ],
    'warps': ['Prontera', 'Prontera Southwest Field', 'Prontera Culvert 1']
  },
  'Prontera South Field': {
    'mobs': [
      ['Poring', 20],
      ['Lunatic', 30],
      ['Fabre', 40],
      ['Pupa', 10]
    ],
    'warps': ['Prontera', 'Prontera Southwest Field', 'Izlude West Field']
  },
  'Prontera Southwest Field': {
    'mobs': [
      ['Poring', 10],
      ['Savage Babe', 30],
      ['Rocker', 60]
    ],
    'warps': ['Prontera South Field', 'Prontera West Field']
  },
  'Prontera Culvert 1': {
    'mobs': [
      ['Thief Bug', 30],
      ['Tarou', 30],
      ['Familiar', 30],
      ['Thief Bug Egg', 10]
    ],
    'warps': ['Prontera West Field', 'Prontera Culvert 2']
  },
  'Prontera Culvert 2': {
    'mobs': [
      ['Thief Bug', 20],
      ['Tarou', 20],
      ['Spore', 20],
      ['Plankton', 20],
      ['Familiar', 10],
      ['Thief Bug Egg', 10]
    ],
    'warps': ['Prontera Culvert 1', 'Prontera Culvert 3']
  },
  'Prontera Culvert 3': {
    'mobs': [
      ['Tarou', 20],
      ['Poison Spore', 30],
      ['Plankton', 30],
      ['Thief Bug', 10],
      ['Familiar', 10]
    ],
    'warps': ['Prontera Culvert 2', 'Prontera Culvert 4']
  },
  'Prontera Culvert 4': {
    'mobs': [
      ['Female Thief Bug', 30],
      ['Male Thief Bug', 30],
      ['Drainliar', 20],
      ['Cramp', 20]
    ],
    'warps': ['Prontera Culvert 3']
  },
  'Izlude': {
    'npcs': {
      'Healing Dealer': True,
      'Weapon Dealer': True,
      'Recycler': True,
      'Joffrey': True
    },
    'warps': ['Izlude West Field']
  },
  'Izlude West Field': {
    'mobs': [
      ['Lunatic', 30],
      ['Fabre', 60],
      ['Poring', 10]
    ],
    'warps': ['Izlude', 'Prontera South Field']
  },
  'Byalan Island': {
    'warps': ['Izlude', 'Undersea Tunnel 1']
  },
  'Undersea Tunnel 1': {
    'mobs': [
      ['Hydra', 20],
      ['Kukre', 20],
      ['Marina', 20],
      ['Vadon', 20],
      ['Plankton', 20]
    ],
    'warps': ['Byalan Island', 'Undersea Tunnel 2']
  },
  'Undersea Tunnel 2': {
    'mobs': [
      ['Hydra', 10],
      ['Kukre', 10],
      ['Marina', 20],
      ['Vadon', 20],
      ['Plankton', 20],
      ['Cornutus', 20]
    ],
    'warps': ['Undersea Tunnel 1', 'Undersea Tunnel 3']
  },
  'Undersea Tunnel 3': {
    'mobs': [
      ['Marse', 20],
      ['Obeaune', 20],
      ['Marina', 20],
      ['Merman', 20],
      ['Cornutus', 20]
    ],
    'warps': ['Undersea Tunnel 2', 'Undersea Tunnel 4']
  },
  'Undersea Tunnel 4': {
    'mobs': [
      ['Marse', 20],
      ['Swordfish', 20],
      ['Marine Sphere', 20],
      ['Merman', 20],
      ['Phen', 20]
    ],
    'warps': ['Undersea Tunnel 3', 'Undersea Tunnel 5']
  },
  'Undersea Tunnel 5': {
    'mobs': [
      ['Strouf', 20],
      ['Swordfish', 20],
      ['Deviace', 20],
      ['Merman', 20],
      ['Phen', 20]
    ],
    'warps': ['Undersea Tunnel 4']
  }
}

class Map(object):
  def __init__(self, name, player):
    self.name = name
    self.player = player
    self.menu = ['Open my panels.']
    self._menu = [['Open panels', 'Panels']]

    if 'npcs' in List[name]:
      for key, value in List[name]['npcs'].iteritems():
        npc_type = npc.List[key]['type']
        self._menu.append([key, npc_type])

        if npc_type == 'Shop':
          self.menu.append('Trade with ' + key + '.')
          
        elif npc_type == 'Recycler':
          self.menu.append('Sell items to ' + key + '.')

        elif npc_type == 'Quest':
          self.menu.append('Talk with ' + key + '.')

    if 'mobs' in List[name]:
      self.menu.append('Find monsters.')
      self._menu.append(['Find monsters.', 'Find Mobs'])

    if 'warps' in List[name]:
      for name in List[name]['warps']:
        self.menu.append('Go to ' + name)
        self._menu.append([name, 'Warp'])

    ui.mes(player.name, 'I want to ..')

    self.open_menu()

  def open_menu(self):
    ans = ui.menu(self.player.name, self.menu)
    if self._menu[ans][1] == 'Panels':
      anss = ui.menu(self.player.name, ['Return.', 'Open status panel.', 'Open bag panel.', 'Archive Game.', 'Archive and exit Game.'])
      if anss == 1:
        self.player.status_panel()
        ui.wait()
      elif anss == 2:
        self.player.bag_panel()
      elif anss == 3:
        self.player.archive()
      elif anss == 4:
        self.player.archive()
        print('\n\033[92mSee you :)')
        sys.exit(0)

    elif self._menu[ans][1] == 'Shop':
      ui.mes(self._menu[ans][0], 'Welcome, what can I help you?')
      ui.mes(self.player.name, 'I have ' + str(self.player.zeny) + 'z now.')
      menu = ['Return.']
      _menu = []
      for name in npc.List[self._menu[ans][0]]['items']:
        menu.append(name + ' ' + str(item.List[name]['price']) + 'z | ' + item.List[name]['tip'])
        _menu.append(name)
      anss = ui.menu(self._menu[ans][0], menu)
      if anss != 0 and self.player.del_zeny(item.List[_menu[anss - 1]]['price']):
        self.player.add_item([[_menu[anss - 1], 1]])

    elif self._menu[ans][1] == 'Recycler':
      ui.mes(self._menu[ans][0], 'Welcome, what do you want to sell?')
      menu = ['Return.']
      _menu = []
      for _type, _list in self.player.items.iteritems():
        for name, num in self.player.items[_type].iteritems():
          menu.append(name + ' ' + str(item.List[name]['price']/2) + 'z/per, total ' + str(num) + '.')
          _menu.append([name, num])
      anss = ui.menu(self.player.name, menu)
      if anss != 0:
        _item = _menu[anss - 1]
        if _item[1] > 1:
          num = _item[1] + 1
          while num > _item[1]:
            num = raw_input(ui.blue('[' + self._menu[ans][0] + ']') + ' How much ' + _item[0] + ' do you want to sell? (Max ' + str(_item[1]) + ', press 0 to cancel.) ')
            try:
              num = int(num)
            except Exception, e:
              num = _item[1] + 1
          if num == 0:
            self.open_menu()
            return
        else:
          num = 1

        self.player.del_item([[_item[0], num]])
        self.player.add_zeny(item.List[_item[0]]['price'] / 2 * num)

    elif self._menu[ans][1] == 'Quest':
      npc.quest(self._menu[ans][0], self.player)

    elif self._menu[ans][1] == 'Find Mobs':
      _mob = core.rand(List[self.name]['mobs'])[0]

      ui.mes(self.player.name, 'Find a ' + ui.green(_mob + ' Lv.' + str(mob.List[_mob]['lv'])) + ' !')
      anss = ui.menu(self.player.name, ['Attack!', 'Run away!'])
      if anss == 0:
        self.player.attack_mob(_mob)

    elif self._menu[ans][1] == 'Warp':
      self.player.warp(self._menu[ans][0])

    self.open_menu()
