#!/usr/bin/env python
import time, httplib, logging, socket

remote = {
  'domain': 'localhost',
  'port': '8888',
  'path': '/',
}

state = {
  'kegs': {
    1: 0,
    2: 0,
  },
  'environment': {
    'temp': 0,
  },
}

def get_arduino_state():
  return {
    'kegs': {
      1: 12,
      2: 15,
    },
    'environment': {
      'temp': 38,
    },
  }

def push_state(remote, state):
  post = httplib.HTTPConnection(remote['domain'], remote['port'])
  headers = {"Content-type": "application/json"}
  try:
    post.request('POST', remote['path'], state, headers)
  except socket.error:
    # do nothing
    None

while True:
  current_state = get_arduino_state()
  if current_state == state:
    time.sleep(60)
  else:
    state = current_state
    push_state(remote, state)
    time.sleep(4)
