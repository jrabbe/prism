#!/usr/bin/python

ACCESS_TOKEN = ''
HOST = 'https://graph.facebook.com'

def facebookRequest(url):
    '''Makes a Facebook Graph API request based on the specified url.'''

    query = {'access_token': ACCESS_TOKEN}
    r = requests.get(HOST + url, params=query);

    try:
        return json.loads(r.text)['data']
    except:
        print 'ERROR! Could not read data from ', r.url
        print ''
        print r.text
        return []

def getFriends(person = None):
    '''Get list of Facebook friends for the specified person, or for 'me' if no argument is given.'''

    fetching_for = 'me' if person == None else person['id']
    fetching_descr = 'me' if person == None else person['name']
    url = '/' + fetching_for + ' /friends'

    print '-> Fetching friends for ', fetching_descr, '...'
    return facebookRequest(url)

def getGroups(person):
    '''Get Facebok groups the specified person is a member of'''

    url = '/' + person['id'] + '/groups'

    print '=> Fetching groups for ', person['name'], '...'
    return facebookRequest(url)

def getLikes(person):
    '''Get Facebook likes for the specified person.'''

    url = '/' + person['id'] + '/likes'

    print '+> Fetching likes for ', person['name'], '...'
    return facebookRequest(url)

def buildGroupDB(personList):
    '''Fetches groups for each person in the list, and builds the '''

    all_groups = {}


    for person in personList:
        groups = getGroups(person)
        for group in groups:
            if group['id'] not in all_groups.keys():
                all_groups[group['id']] = group


def main():
    '''The main function of the application'''

    parser = argparse.ArgumentParser(prog='fetching', description='''Fetches data from facebook
        and builds corrolation databases (json files).''')
    parser.add_argument('-f', '--friends', action='store_true', help='''Fetch friends.
        The likes or groups options means that this defaults to true unless the input file is provided.''')
    parser.add_argument('-g', '--groups', action='store_true', help='''Fetch groups for friends.''')
    parser.add_argument('-l', '--likes', action='store_true', help='''Fetch likes for friends.''')
    parser.add_argument('-i', '--input', type=file, default=None, help='''A json file containing a friend list.''')
    parser.add_argument('-p', '--prefix', default=None, help='''The prefix to use for output files,
        will be prepended to the output json files, e.g. <prefix>_groups.js. If not provided,
        the output files are simply groups.json, etc.''')

    args = parser.parse_args()

    return 0

if __name__ == '__main__':
    sys.exit(main())
