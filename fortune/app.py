from flask import Flask, jsonify, abort, request, make_response, url_for, redirect
from flask.ext.httpauth import HTTPBasicAuth
import os

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()
token = os.environ['TOKEN']

# get the list of possible dbs. Cant get `fortune -f` to work from python. This file path is distro dependent
files = os.popen('ls /usr/share/games/fortunes').read().split('\n')
dblist = filter(None,[element for element in files  if not '.' in element ])
dblistAsString = ', '.join(dblist)

#not being used but an example using authentication
@auth.get_password
def get_password(username):
    if username == 'fortune':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify( { 'error': 'An error occured' } ), 500)

# A slack specific impementation
@app.route('/fortune', methods = ['POST'])
def getFortune():
    if (  request.values.get('token') != token ):
        abort(403)

    db = request.values.get('text')
    result = 'unknown option'
    if db and not db.isspace():
        if db == 'list':
            # dont call fortune, return db list
            result = dblistAsString
        elif db in dblist:
            # the string refers to an existing fortune db
            result = os.popen('fortune '+db).read()
    else:
        result = os.popen('fortune fortunes').read()

    if (  request.values.get('format' ) == 'json' ):
        return jsonify( { 'text': unicode( result , errors='ignore') } )

    return unicode( result  , errors='ignore')

# A more generic api implementation follows
@app.route('/api/fortune', methods = ['GET'])
def listApiPaths():
    q = request.values.get('q')
    if q == 'list':
        return getFortuneApi('list')
    else:
        return getFortuneApi('random')

@app.route('/api/fortune/<string:db>', methods = ['GET'])
#@auth.login_required
def getFortuneApi(db):
    result = 'unknown option'
    if db and not db.isspace():
        if db == 'list':
            # dont call fortune, return db list
            result = dblistAsString
        elif db == 'random':
            result = os.popen('fortune').read()
        elif db in dblist:
            # the string refers to an existing fortune db
            result = os.popen('fortune '+db).read()

    if (  request.values.get('format' ) == 'text' ):
        return unicode( result  , errors='ignore')

    return jsonify( { 'text': unicode( result , errors='ignore') } )

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
