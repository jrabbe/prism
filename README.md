# prism

There has been a large amount of talk about the [Prism surveillance program][prism] in the news and
among people. This was an idea I had based on the [metadata analysis that identified Paul Revere][slate].

I made one version in Python (can be seen in `./old`), but when I wanted to redo it better, I wanted
to try out something new. Since I've been meaning to try out Typescript for a while, that was the
choice.

Very much still a work-in-progress (apart from some of the python code, nothing works).

## Requirements

To run this program you need node.js and access to Facebook.

You need to go to the [Facebook graph explorer][graph-explorer] and generate an access token with
the requirements you need. For instance to graph the likes of your friends you need the `friend_likes`
permissions. This access token should not be shared with anyone (lest they do stuff in your name),
and it expires after a few hours.

## Usage

Have to figure this out... May want to just have a thin JS 'app' shell that includes the typescript
modules.




[prism]: http://en.wikipedia.org/wiki/PRISM_(surveillance_program)
[slate]: http://www.slate.com/articles/health_and_science/science/2013/06/prism_metadata_analysis_paul_revere_identified_by_his_connections_to_other.html

[graph-explorer]: https://developers.facebook.com/tools/explorer

[process]: http://nodejs.org/api/process.html#process_process_argv
[commander]: https://github.com/visionmedia/commander.js
[typescript-require]: https://github.com/eknkc/typescript-require
[typescript-node-definitions]: https://github.com/soywiz/typescript-node-definitions
