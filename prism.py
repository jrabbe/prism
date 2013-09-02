# -------------------------------------------------------------------------------------------------
# Copyright (C) 2013 Jonas Rabbe
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# -------------------------------------------------------------------------------------------------

from flask import Flask, request

#
# Static assets
#

app = Flask(__name__, static_url_path='/assets', static_folder='public')

#
# API endpoints
#

@app.route('/api/fetch-data', methods=['GET'])
def fetchData():
    """ Endpoint action for fetching data from Facebook.

    Parses the provided query string to find which types of data to fetch.

    Query string arguments:
        access-token: The access token for the user providing at least access to any of the other
        options selected.
        events: If present all events will be fetched for each friend.
        groups: If present all groups will be fetched for each friend.
        interests: If present all interests will be fetched for each friend.
        likes: If present all likes will be fetched for each friend.
    """

    accessToken = request.args.get('access-token', '')

    events = request.args.get('events', None)
    groups = request.args.get('groups', None)
    interests = request.args.get('interests', None)
    likes = request.args.get('likes', None)



    return "test"

#
# Catch all endpoint serving the index page
#

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return app.send_static_file('index.html')

#
# Run the app
#

if __name__ == "__main__":
    app.run(debug=True)

