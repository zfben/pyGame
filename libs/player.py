# coding=UTF-8

import os
import math
from random import randrange
import json
import base64
from ui import *
import item
import mob
import map

class Player(object):
  def __init__(self):
    self.name = ''
    self.exp = 0
    self.str = 1
    self.int = 1
    self.zeny = 0
    self.npcs = {}
    self.save = 'Prontera'
    self.map = 'Prontera'
    self.items = {
      'HP Healing': {},
      'SP Healing': {},
      'Weapon': {}
    }
    self.equipments = {
      'Weapon': ''
    }
    self.equipments_status = {
      'min_atk': 0,
      'max_atk': 0,
      'min_matk': 0,
      'max_matk': 0
    }
    self.hp = self.mhp()
    self.sp = self.msp()

  def lv(self):
    if self.exp < 10:
      return 1
    else:
      return int(math.sqrt(self.exp / 10) + 1)
  
  def mhp(self):
    return int((self.lv() + self.str) * 10)

  def msp(self):
    return int((self.lv() + self.str) * 5)

  def min_atk(self):
    return self.lv()

  def max_atk(self):
    return int(self.lv() + self.str)

  def atk(self):
    return randrange(self.min_atk(), self.max_atk())

  def min_matk(self):
    return int(self.lv() + self.int)

  def max_matk(self):
    return int(self.lv() + self.int * 2)

  def current_exp(self):
    return int(self.exp - ((self.lv() - 1) ** 2) * 10)

  def next_exp(self):
    return int(((self.lv()) ** 2) * 10)

  def status_panel(self):
    ui.mes(self.name, 'Status Panel Opened.')
    print '============================='
    print self.name + ' Lv.' + str(self.lv())
    print 'Exp ' + str(self.current_exp()) + '/' + str(self.next_exp())
    print 'HP ' + str(self.hp) + '/' + str(self.mhp()) + '  SP ' + str(self.sp) + '/' + str(self.msp())
    print 'Atk ' + str(self.min_atk()) + ' + ' + str(self.equipments_status['min_atk']) + ' ~ ' + str(self.max_atk()) + ' + ' + str(self.equipments_status['max_atk'])
    print 'Matk ' + str(self.min_matk()) + ' + ' + str(self.equipments_status['min_matk']) + ' ~ ' + str(self.max_matk()) + ' + ' + str(self.equipments_status['max_matk'])
    print 'Str ' + str(self.str) + '  Int ' + str(self.int)
    print 'Zeny ' + str(self.zeny)
    print '============================='

  def has_npc(self, names):
    result = 0

    for key in names:
      if key in self.npcs:
        result += 1

    return result == len(names)

  def add_exp(self, num):
    cur_lv = self.lv()
    self.exp = self.exp + num
    ui.mes(self.name, 'Got ' + ui.green(str(num)) + ' exp. [' + str(self.current_exp()) + '/' + str(self.next_exp()) + ']', False)
    if self.lv() > cur_lv:
      for _ in range(cur_lv):
        if randrange(2) == 0:
          self.str += 1
        else:
          self.int += 1
      self.hp = self.mhp()
      self.sp = self.msp()
      ui.mes(self.name, ui.green('Level up!'), False)

  def add_item(self, items):
    for _item in items:
      item_type = item.List[_item[0]]['type']
      if _item[0] not in self.items[item_type]:
        self.items[item_type][_item[0]] = 0
      self.items[item_type][_item[0]] += _item[1]
      ui.mes(self.name, 'Got ' + ui.green(str(_item[1]) + ' ' + _item[0]) + '. [' + str(self.items[item_type][_item[0]]) + ']', False)

  def del_item(self, items):
    for _item in items:
      item_type = item.List[_item[0]]['type']
      self.items[item_type][_item[0]] -= _item[1]
      num = self.items[item_type][_item[0]]
      if num == 0:
        self.items[item_type].pop(_item[0], None)
      ui.mes(self.name, 'Took ' + ui.green(str(_item[1]) + ' ' + _item[0]) + '. [' + str(num) + ']', False)

  def add_zeny(self, num):
    self.zeny = self.zeny + num
    ui.mes(self.name, 'Got ' + ui.green(str(num)) + ' zeny. [' + str(self.zeny) + ']', False)

  def del_zeny(self, num):
    if num > self.zeny:
      ui.mes(self.name, 'I have not enought money.')
      return False
    else:
      self.zeny -= num
      ui.mes(self.name, 'Used ' + ui.green(str(num)) + ' zeny. [' + str(self.zeny) + ']', False)
      return True

  def equip(self, name):
    item_type = item.List[name]['type']

    if self.equipments[item_type] != '':
      self.unequip(item_type)

    self.del_item([[name, 1]])
    self.equipments[item_type] = name
    for key, value in item.List[name]['status'].iteritems():
      self.equipments_status[key] += value
    ui.mes(self.name, 'Equiped ' + ui.green(name + ' | ' + item.List[name]['tip']) + '.', False)

  def unequip(self, position):
    name = self.equipments[position]
    print name
    self.add_item([[name, 1]])
    for key, value in item.List[name]['status'].iteritems():
      self.equipments_status[key] -= value
    ui.mes(self.name, 'Unequiped ' + ui.green(name + ' | ' + item.List[name]['tip']) + '.', False)

  def has_equiped(self, name):
    item_type = item.List[name]['type']
    return name in self.equipments[item_type]

  def use_item(self, name):
    self.del_item([[name, 1]])
    for key, value in item.List[name]['status'].iteritems():
      if key == 'hp':
        heal = randrange(value[0], value[1])
        if self.hp + heal > self.mhp():
          heal = self.mhp() - self.hp
        self.hp += heal
        ui.mes(self.name, 'Used 1 ' + name + ' to heal ' + ui.green(str(heal)) + ' HP. [' + str(self.hp) + '/' + str(self.mhp()) + ']', False)
      elif key == 'sp':
        heal = randrange(value[0], value[1])
        if self.sp + heal > self.msp():
          heal = self.msp() - self.sp
        self.sp += heal
        ui.mes(self.name, 'Used 1 ' + name + ' to heal ' + ui.green(str(heal)) + ' SP. [' + str(self.sp) + '/' + str(self.msp()) + ']', False)

  def bag_panel(self):
    ui.mes(self.name, 'Bag Panel Opened.')
    print '============================='
    for name, num in self.items['HP Healing'].iteritems():
      print name + ' x' + str(num) + ' | ' + item.List[name]['tip']
    for name, num in self.items['SP Healing'].iteritems():
      print name + ' x' + str(num) + ' | ' + item.List[name]['tip']
    for name, num in self.items['Weapon'].iteritems():
      print name + ' x' + str(num) + ' | ' + item.List[name]['tip']
    print '---------- Equiped ----------'
    if self.equipments['Weapon'] != '':
      print '[Weapon] ' + self.equipments['Weapon'] + ' | ' + item.List[self.equipments['Weapon']]['tip']
    print '============================='
    ans = ui.menu(self.name, ['Close bag.', 'Use healing items.', 'Use equipments.'])
    if ans == 1:
      menu = ['Return.']
      _menu = ['Return']
      if self.hp < self.mhp():
        ui.mes(self.name, 'My HP is ' + str(self.hp) + '/' + str(self.mhp()), False)
        for name, num in self.items['HP Healing'].iteritems():
          menu.append('Use 1 ' + name + ' to heal HP. [' + item.List[name]['tip'] + ']')
          _menu.append(name)
      if self.sp < self.msp():
        ui.mes(self.name, 'My SP is ' + str(self.sp) + '/' + str(self.msp()), False)
        for name, num in self.items['SP Healing'].iteritems():
          menu.append('Use 1 ' + name + ' to heal SP. [' + item.List[name]['tip'] + ']')
          _menu.append(name)
      if len(menu) > 1:
        anss = ui.menu(self.name, menu)
        if anss == 0:
          self.bag_panel()
        else:
          self.use_item(_menu[anss])
          self.bag_panel()
      else:
        ui.mes(self.name, 'I am very healthy.')
        ui.wait()
        self.bag_panel()
    elif ans == 2:
      if len(self.items['Weapon'].keys()) > 0:
        menu = ['Return.']
        equipments = []
        for weapon in self.items['Weapon'].iteritems():
          menu.append('Use ' + name + ' | ' + item.List[name]['tip'])
          equipments.append(name)
        ans = ui.menu(self.name, menu)
        if ans == 0:
          self.bag_panel()
        else:
          self.equip(equipments[ans - 1])
      else:
        ui.mes(self.name, 'I have no equipment in bag.')

  def attack_mob(self, mob_name):
    _mob = mob.Mob(mob_name)
    while self.hp > 0 and _mob.hp > 0:
      _mob.be_attacked(self)
      if _mob.hp > 0:
        _mob.attack(self)

    if self.hp < 1:
      ui.mes(self.name, ['I dead.', 'I will revive at ' + self.save + '.'])
      ui.wait()
      self.hp = self.mhp()
      self.sp = self.msp()
      self.warp(self.save)
    else:
      _mob.dead(self)

  def _dat_path(self):
    return 'archives/' + self.name + '.dat'

  def archive(self):
    f = open(self._dat_path(), 'w')
    f.write(base64.b64encode(json.dumps(self.__dict__)))
    f.close()
    print ui.yellow('Archiving completed.')

  def load(self):
    f = open(self._dat_path(), 'r')
    self.__dict__.update(json.loads(base64.b64decode(f.read())))
    f.close()
    self.status_panel()
    print ui.yellow('Loading completed.')
    ui.wait()
    self.warp(self.map)

  def is_archived(self):
    return os.path.exists(self._dat_path())

  def warp(self, map_name):
    self.map = map_name
    ui.clear()
    ui.mes(self.name, ['Now at ' + ui.green(map_name) + '.'])
    _map = map.Map(map_name, self)
