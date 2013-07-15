/// <reference path="../../../definitions/angularjs/angular.d.ts" />

module prism {
    'use strict';

    export interface INavControllerScope extends ng.IScope {
        currentPage: string;
        location: ng.ILocationService;
    }
}
