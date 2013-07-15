/// <reference path="../../../definitions/angularjs/angular.d.ts" />
/// <reference path="../models/FetchObject.ts" />

module prism {
    'use strict';

    export interface IMainControllerScope extends ng.IScope {
        fetch: FetchObject;
        fetchData: () => void;
    }
}
