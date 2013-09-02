prism
=====

There has been a large amount of talk about the [Prism surveillance program][prism] in the news and
among people. This was an idea I had based on the [metadata analysis that identified Paul Revere][slate].

I originally made one version in Python (which is can be viewed in `./old`), but when I wanted to
redo it better I started out with TypeScript, but quickly figured that the annoyances of TypeScript
with node.js were too much for me. After other things interrupted my progress, I decided to take
a Python + JavaScript approach.

Very much still a work-in-progress (apart from some of the python code, nothing works).

Requirements
------------

To run this program you need Python and access to Facebook.

You need to go to the [Facebook graph explorer][graph-explorer] and generate an access token with
the requirements you need. For instance to graph the likes of your friends you need the `friend_likes`
permissions. This access token should not be shared with anyone (lest they do stuff in your name),
and it expires after a few hours.

Dependencies
------------

This web application simply depends on the *flask* python module. I would suggest creating a virtual
environment for installing into. Make sure you have `virtualenv` installed, and run.

    virtualenv prism-env
    . prism-env/bin/activate

After activating the environment simply run pip like normal.

    pip install flask

Now you can run the app using

    python prism.py

Each time you want to run the app, you just activate the virtual environment, and start the
prism.py script again.


[prism]: http://en.wikipedia.org/wiki/PRISM_(surveillance_program)
[slate]: http://www.slate.com/articles/health_and_science/science/2013/06/prism_metadata_analysis_paul_revere_identified_by_his_connections_to_other.html

[graph-explorer]: https://developers.facebook.com/tools/explorer
