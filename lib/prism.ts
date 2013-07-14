/// <reference path="../../typescript/DefinitelyTyped/node/node.d.ts" />
/// <reference path="../../typescript/DefinitelyTyped/express/express.d.ts" />

import express = module("express");

//
// PRISM web application in typescript
//

var app = express();

app.get("/", function(request, response) {
    response.send("Welcome to PRISM");
});

module.exports = app;

