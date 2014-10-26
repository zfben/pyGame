# coding=UTF-8

from ui import *

List = {
  'Healing Dealer': {
    'type': 'Shop',
    'items': ['Red Potion', 'Blue Potion']
  },
  'Weapon Dealer': {
    'type': 'Shop',
    'items': ['Knife', 'Cutter', 'Main Gauche']
  },
  'Recycler': {
    'type': 'Recycler'
  },
  'Cecily': {
    'type': 'Quest'
  },
  'Joffrey': {
    'type': 'Quest'
  }
}

def quest(npc_name, player):
  if npc_name == 'Cecily':
    if player.has_npc(['Cecily']):
      next_lv = player.skills['Heal'] + 1
      money = next_lv ** 2 * 100
      ui.mes('Cecily', ['If you want to upgrade Heal, you should give me more money!', 'Lv.' + str(next_lv) + ' Heal need ' + str(money) + 'z.'])
      if player.zeny >= money:
        if ui.menu(player.name, ['Upgrade now.', 'I don\'t need it.']) == 0:
          player.del_zeny(money)
          player.add_skill('Heal')
          ui.mes('Cecily', 'I am sure you will like it!')
        else:
          ui.mes('Cecily', 'Umm..')
    else:
      ui.mes('Cecily', 'If you give me 100, I will tell you a secret.')
      if ui.menu(player.name, ['Tell me.', 'It\'s boring.']) == 0:
        if player.zeny >= 100:
          player.del_zeny(100)
          player.add_skill('Heal')
          ui.mes('Cecily', ['The secret is ' + ui.green('Heal') + ' !', 'Now you can use it in battle.'])
          player.npcs['Cecily'] = True
        else:
          ui.mes('Cecily', 'You have not enough money.')
      else:
        ui.mes('Cecily', 'Umm..')
  elif npc_name == 'Joffrey':
    if player.has_npc(['Joffrey']):
      next_lv = player.skills['Cold Bolt'] + 1
      money = next_lv ** 2 * 200
      ui.mes('Joffrey', ['If you want to upgrade Cold Bolt, you should give me more money!', 'Lv.' + str(next_lv) + ' Cold Bolt need ' + str(money) + 'z.'])
      if player.zeny >= money:
        if ui.menu(player.name, ['Upgrade now.', 'It\'s too experensive.']) == 0:
          player.del_zeny(money)
          player.add_skill('Heal')
          ui.mes('Joffrey', 'I am sure you will like it!')
        else:
          ui.mes('Joffrey', 'Umm..')
    else:
      ui.mes('Joffrey', ['Cold Bolt is a powerful skill.', 'I learned it from Undersea Tunnel.', 'If you give me 200, I will tech you.'])
      if ui.menu(player.name, ['Teach me, please.', 'I can learn it by myself.']) == 0:
        if player.zeny >= 200:
          player.del_zeny(200)
          player.add_skill('Cold Bolt')
          ui.mes('Joffrey', ['Be careful, don\'t cold bolt youself!'])
          player.npcs['Joffrey'] = True
        else:
          ui.mes('Joffrey', 'I am not free.')
      else:
        ui.mes('Joffrey', 'Umm..')

