# coding=UTF-8

from random import randrange

def rand(data):
  result = []
  num = randrange(100)
  cur = 0
  for item in data:
    cur += item[1]
    if num < cur:
      result = item
      break
  return result
