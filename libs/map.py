# coding=UTF-8

import sys
from random import randrange
from ui import *
import npc
import item

List = {
  'Prontera': {
    'type': 'town',
    'npcs': {
      'Healing Dealer': True,
      'Weapon Dealer': True,
      'Recycler': True
    },
    'warps': ['Prontera South Field']
  },
  'Prontera South Field':{
    'type': 'field',
    'mobs': [
      ['Poring', 60],
      ['Lunatic', 40]
    ],
    'warps': ['Prontera']
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

    if 'mobs' in List[name]:
      self.menu.append('Find monsters.')
      self._menu.append(['Find monsters.', 'Find Mobs'])

    if 'warps' in List[name]:
      for name in List[name]['warps']:
        self.menu.append('Warp to ' + name)
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

    elif self._menu[ans][1] == 'Find Mobs':
      rand = randrange(100)
      _mob = ''
      cur_num = 0
      for data in List[self.name]['mobs']:
        cur_num += data[1]
        if rand < cur_num:
          _mob = data[0]
          break

      ui.mes(self.player.name, 'Find a ' + ui.green(_mob) + '!')
      anss = ui.menu(self.player.name, ['Attack!', 'Run away!'])
      if anss == 0:
        self.player.attack_mob(_mob)

    elif self._menu[ans][1] == 'Warp':
      self.player.warp(self._menu[ans][0])

    self.open_menu()
