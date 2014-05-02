#!/usr/bin/env python
import httplib, logging, json, socket, serial, urllib
from pprint import pprint

with open('config.json') as json_data:
  config = json.load(json_data)

ser = serial.Serial(config['serial'], 9600)

state = {
  'kegs': [ 0, 0 ],
  'temperature': 0,
  'access_token': config['access_token']
}

def get_arduino_state():
  value = ser.readline().strip()
  if value:
    values = value.split(',')
    values[0] = (9 / 5) * ( float(values[0]) - 273) + 32
    return {
      'kegs': [ float(values[1]), float(values[2]) ],
      'temperature': values[0],
      'access_token': config['access_token']
    }

def push_state(remote, state):
  post = httplib.HTTPConnection(remote['domain'], str(remote['port']))
  headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
  state = urllib.urlencode(state)
  try:
    post.request('POST', remote['path'], state, headers)
    print "Posted "
    pprint(state)
    print " to "
    pprint(remote)
    print " with response "
    pprint(post.getresponse().read())
  except socket.error, e:
    print "Error posting "
    pprint(state)
    print " to "
    pprint(remote)
    print "Error: " + str(e)

while True:
  current_state = get_arduino_state()
  if current_state:
    state = current_state
    push_state(config['remote'], state)
