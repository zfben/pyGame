# coding=UTF-8

import sys
import signal

def signal_handler(signal, frame):
  print('\n\033[92mSee you :)')
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if sys.platform.startswith('win'):
  print 'Sorry, the game can\'t run in Windows. Please run in OS X or Linux.'
else:
  import os
  from libs.ui import *
  from libs.player import Player

  ui.clear()

  print '''
   _____                                   _    
  |  __ \                                 | |   
  | |__) |__ _  __ _ _ __   __ _ _ __ ___ | | __
  |  _  // _` |/ _` | '_ \ / _` | '__/ _ \| |/ /
  | | \ \ (_| | (_| | | | | (_| | | | (_) |   < 
  |_|  \_\__,_|\__, |_| |_|\__,_|_|  \___/|_|\_\\
                __/ |                           
               |___/                      By Ben
  '''

  ui.mes('Training Grounds Receptionist', ['Hello, you look to be new here.', 'What is your name?'])

  current = Player()

  while current.name == '' or ('/' in current.name) or ('\\' in current.name):
    current.name = raw_input(ui.blue('[You]') + ' My name is ')

  if current.is_archived():
    current.load()
  else:
    from libs.training_ground import TrainingGround
    TrainingGround.run(current)
