var prism;
(function (prism) {
    'use strict';

    prism.MainController = [
        '$scope',
        function MainController($scope) {
            var fetchData = function () {
                console.log('fetch some data');
            };

            $scope.fetchData = function () {
                return fetchData();
            };
        }];

})(prism || (prism = {}));
