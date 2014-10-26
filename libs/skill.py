# coding=UTF-8

import time
from ui import *

List = {
  'Heal': {
    'tip': 'Restore yourself\'s HP.'
  },
  'Lightening Bolt': {
    'tip': 'Calls bolts of lightning from the skies to strike at a single target.'
  },
  'Cold Bolt': {
    'tip': 'Calls bolts of frigid ice from the skies to strike at a single target.'
  },
  'Envenom': {
    'tip': 'Strikes an enemy to inflict Poison status by chance.'
  }
}


def use(skill_name, skill_lv, source, target):
  time.sleep(0.8)
  if skill_name == 'Heal':
    heal = source.matk() * skill_lv
    if source.hp + heal > source.mhp():
      heal = source.mhp() - source.hp
    source.hp += heal
    ui.mes(source.name, 'Use ' + ui.green(skill_name) + ' restore ' + ui.green(heal) + ' HP. [' + str(source.hp) + '/' + str(source.mhp()) + ']', False)
  elif skill_name == 'Lightening Bolt' or skill_name == 'Cold Bolt':
    dmg = source.matk() * skill_lv
    if target.hp - dmg < 0:
      dmg = target.hp
    target.hp -= dmg
    ui.mes(source.name, 'Use ' + ui.green(skill_name) + ' attack with ' + ui.green(dmg) + ' damage. [' + str(target.hp) + '/' + str(target.mhp()) + ']', False)
  elif skill_name == 'Envenom':
    dmg = source.matk() * skill_lv
    if target.hp - dmg < 0:
      dmg = target.hp
    target.hp -= dmg
    target.status['Poison'] = int(dmg / 10)
    ui.mes(source.name, 'Use ' + ui.green(skill_name) + ' attack with ' + ui.green(dmg) + ' damage. [' + str(target.hp) + '/' + str(target.mhp()) + ']', False)
