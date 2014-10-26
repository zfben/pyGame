# coding=UTF-8

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

class ui:

  @staticmethod
  def blue(msg):
    return bcolors.OKBLUE + msg + bcolors.ENDC

  @staticmethod
  def green(msg):
    return bcolors.OKGREEN + msg + bcolors.ENDC

  @staticmethod
  def yellow(msg):
    return bcolors.WARNING + msg + bcolors.ENDC

  @staticmethod
  def wait():
    raw_input('Press any key to continue.')

  @staticmethod
  def clear():
    print chr(27) + "[2J"

  @staticmethod
  def mes(name, msg, break_line = True):
    if break_line:
      print ''

    if type(msg) is not list:
      msg = [msg]

    for m in msg:
      print ui.blue('[' + name + '] ') + m

  @staticmethod
  def menu(name, list):
    length = len(list) - 1

    for i, item in enumerate(list):
      print ui.yellow('[' + str(i) + '] ') + item

    result = length + 1

    while result < 0 or result > length:
      _input = ''
      _input = raw_input('Please input the number of items or press enter to choose first item: ')
      if _input == '':
        result = 0
      else:
        try:
          result = int(_input)
        except Exception, e:
          e

    print 'You choose ' + ui.green(list[result])
    return result
