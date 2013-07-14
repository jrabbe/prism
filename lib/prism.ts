/// <reference path="../../typescript/DefinitelyTyped/node/node.d.ts" />
/// <reference path="../../typescript/DefinitelyTyped/express/express.d.ts" />

import express = module("express");

//
// PRISM web application in typescript
//

var app = express();

app.use(express.static('./public'));

module.exports = app;
