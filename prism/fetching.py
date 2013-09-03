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
import uuid

from . import errors

class Fetching(object):
    """Class for fetching data from Facebook.

    This class contains a number of methods that fetch data, specifically the friends of the
    user with the specified access token, and for each friend their events, groups, likes, and/or
    likes as specified on the input.

    Attributes:
        accessToken: The access token for the user.
        fetchAttributes: A list of the attributes to fetch.
        valid: True if the fetchObject is valid and can be used to fetch data from Facebook.
        objectMap: A map of UUIDs to Fetching instances for the clients using this app.

        HOST: The Facebook graph host to make API requests towards.
        VALID_ATTRIBUTES: A list containing the valid attributes that can be fetched.
    """

    HOST = 'https://graph.facebook.com'
    VALID_ATTRIBUTES = ['events', 'groups', 'interests', 'likes']

    accessToken = ''
    fetchAttributes = []
    valid = True
    objectMap = {}

    @classmethod
    def generateId(cls):
        return uuid.uuid4()

    @classmethod
    def createFetchObject(cls, fetchAttributes):
        if cls.objectMap == None:
            cls.objectMap = {}

        obj = Fetching(fetchAttributes)

        cls.objectMap[Fetching.generateId()] = obj

        return obj

    def __init__(self, fetchAttributes):
        # check variables for existence, and validity.

        if 'accessToken' in fetchAttributes and isinstance(fetchAttributes['accessToken'], (str, unicode)):
            self.accessToken = fetchAttributes['accessToken']
            del fetchAttributes['accessToken']
        else:
            self.valid = False
            return

        self.fetchAttributes = []
        for key, value in fetchAttributes.iteritems():
            if key in self.VALID_ATTRIBUTES and value == True:
                self.fetchAttributes.append(key)

    def facebookRequest(self, url, field=None):
        """Makes a Facebook Graph API request based on the specified url.
        """

        query = {'access_token': self.accessToken}
        r = requests.get(self.HOST + url, params=query);

        responseData = json.loads(r.text)
        if u'error' in responseData:
            raise errors.ResponseError(responseData[u'error'][u'message'])

        if field != None:
            if field in responseData:
                return responseData[field]
            else:
                raise errors.ResponseDataError(field, r.text)

        return responseData

    def checkAccessToken(self):
        try:
            self.facebookRequest('/me')
        except errors.ResponseError as e:
            return {u'error': unicode(e), u'valid': False}
        except:
            return {u'error': u'Unknown error occurred, cannot fetch data.', u'valid': False}

        return {u'valid': True}


    def getFriends(self, person=None):
        """Get list of Facebook friends for the specified person

        Fetches all the Facebook friends of the given person, or for 'me' (i.e. the person owning
            the access token) if person is None.
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

