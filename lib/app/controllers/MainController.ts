/// <reference path="../../../definitions/angularjs/angular.d.ts" />
/// <reference path="../interfaces/IMainControllerScope.ts" />


module prism {
    'use strict';

    export class MainController {
        public injection(): any {
            return [
                '$scope',
                MainController
            ];
        }

        constructor (
            private $scope: IMainControllerScope
        ) {
            $scope.fetchData = () => this.fetchData();
        }

        fetchData() {
            console.log('fetch some data');
        }
    }
}
