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

import requests
import json

class fetching:
    """Class for fetching data from Facebook.

    This class contains a number of methods that fetch data, specifically the friends of the
    user with the specified access token, and for each friend their events, groups, likes, and/or
    likes as specified on the input.
    """

    def __init__(self):
        self.ACCESS_TOKEN = ''
        self.HOST = 'https://graph.facebook.com'

    def facebookRequest(self, url):
        """Makes a Facebook Graph API request based on the specified url.
        """

        query = {'access_token': self.ACCESS_TOKEN}
        r = requests.get(self.HOST + url, params=query);

        try:
            return json.loads(r.text)['data']
        except:
            print 'ERROR! Could not read data from ', r.url
            print ''
            print r.text
            return []

    def checkAccessToken(self, accessToken):
        pass

    def getFriends(self, person=None):
        """Get list of Facebook friends for the specified person, or for 'me' if no argument
        is given.
        """

        fetching_for = 'me' if person == None else person['id']
        fetching_descr = 'me' if person == None else person['name']
        url = '/' + fetching_for + ' /friends'

        print '-> Fetching friends for ', fetching_descr, '...'
        return self.facebookRequest(url)

    def getGroups(self, person):
        """Get Facebok all groups for the specified person.
        """

        url = '/' + person['id'] + '/groups'

        print '=> Fetching groups for ', person['name'], '...'
        return self.facebookRequest(url)

    def getLikes(self, person):
        """Get Facebook likes for the specified person.
        """

        url = '/' + person['id'] + '/likes'

        print '+> Fetching likes for ', person['name'], '...'
        return self.facebookRequest(url)

    def buildGroupDB(self, personList):
        """Fetches groups for each person in the list, and builds a table with it.
        """

        all_groups = {}

        for person in personList:
            groups = self.getGroups(person)
            for group in groups:
                if group['id'] not in all_groups.keys():
                    all_groups[group['id']] = group

