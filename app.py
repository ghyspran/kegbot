#!/usr/bin/env python
from flask import Flask, jsonify
from kegbot import keg

app = Flask(__name__)

@app.route('/keg/', methods = ['GET'])

def get_keg():
  return jsonify({
    'kegs': [ 1, 2 ]
  })

@app.route('/keg/<int:keg_id>', methods = ['GET', 'POST', 'DELETE'])
def get_keg_n(keg_id):
  keg_state_get(keg_id)
  keg_state = {
    'id': keg_id,
    'state': 0.9
  }
  return jsonify(keg_state)

def post_keg(keg_id):
  if not request.get_json():
    abort(400)
  print request.get_json()
  return 'Keg ' + str(keg_id) + ' added'

def delete_keg(keg_id):
  return 'Keg ' + str(keg_id) + ' deleted'

if __name__ == '__main__':
  app.run(debug = True)
