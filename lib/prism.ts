/// <reference path="../definitions/node/node.d.ts" />
/// <reference path="../definitions/express/express.d.ts" />

import express = module("express");

//
// PRISM web application in typescript
//

var app = express();

app.use('/css', express.static('./public/css'));
app.use('/img', express.static('./public/img'));
app.use('/templates', express.static('./public/templates'));
app.use('/js', express.static('./js/lib/app'));
app.use('/js/vendor', express.static('./bower_components'));

app.get('*', function (request, response) {
    response.sendfile('./public/index.html');
    });

module.exports = app;
