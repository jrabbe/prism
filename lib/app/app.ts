/// <reference path="../../definitions/angularjs/angular.d.ts" />
/// <reference path="controllers/MainController.ts" />

module prism {
    'use strict';

    var prism = angular.module('prism', [])
    .config(['$locationProvider', '$routeProvider', function ($locationProvider, $routeProvider) {
        $routeProvider
        .when('/', {
            controller: 'MainController',
            templateUrl: '/templates/main.tmpl'
            })
        .when('/about', {
            controller: 'NavController',
            templateUrl: '/templates/about.tmpl'
            })
        .otherwise({redirectTo: '/'})
        ;

        // configure html5 to get links working on jsfiddle
        $locationProvider.html5Mode(true);
    }])
    .controller('MainController', MainController.prototype.injection())
    .controller('NavController', NavController.prototype.injection())
    ;
}
