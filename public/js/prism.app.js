

var prism;
(function (angular, prism) {
    'use strict';

    angular.module('prism', ['ngRoute'])

        .controller('MainController', prism.MainController)
        .controller('NavController', prism.NavController)

        .config(['$locationProvider', '$routeProvider', function ($locationProvider, $routeProvider) {
                $routeProvider.when('/', {
                    controller: 'MainController',
                    templateUrl: '/assets/templates/main.tmpl'
                }).when('/about', {
                    controller: 'NavController',
                    templateUrl: '/assets/templates/about.tmpl'
                }).otherwise({ redirectTo: '/' });

                $locationProvider.html5Mode(true);
            }
        ])
    ;

})(angular, prism || (prism = {}));
