/// <reference path="../../../definitions/angularjs/angular.d.ts" />
/// <reference path="../interfaces/INavControllerScope.ts" />

module prism {
    'use strict';

    export class NavController {
        public injection(): any {
            return [
                '$scope',
                '$location',
                NavController
            ];
        }

        constructor (
            private $scope: INavControllerScope,
            private $location: ng.ILocationService
        ) {
            $scope.location = $location;
            $scope.$watch('location.path()', (path) => this.onPath(path));
        }

        onPath(path: string) {
            switch(path) {
                case '/':
                    this.$scope.currentPage = 'home';
                    break;
                case '/about':
                    this.$scope.currentPage = 'about';
                    break;
            }
        }
    }
}
