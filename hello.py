from flask import Flask
import os
import unirest
from flask import request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/url')
def requestw():
  url = 'http://imgur.com/' + request.args.get('imgur')
  response = unirest.post("https://camfind.p.mashape.com/image_requests",
  headers={
    "X-Mashape-Key": "ysmAp4zJQcmshhUqiSlmhotB226Bp1fclLOjsnidCdRFmzIRI9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "image_request[locale]": "en_US",
    "image_request[remote_image_url]": url
  } )
  token = response.body['token']
  response2 = unirest.get("https://camfind.p.mashape.com/image_responses/{token}",
  headers={
    "X-Mashape-Key": "ysmAp4zJQcmshhUqiSlmhotB226Bp1fclLOjsnidCdRFmzIRI9",
    "Accept": "application/json"
  })

  if response2.body['status'] is "completed":
      return jsonify(response = response2['name'])
  return jsonify(response = 'none')

if __name__ == '__main__':
  app.debug = True
  app.run()
