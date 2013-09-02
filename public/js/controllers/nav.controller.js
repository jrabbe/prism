var prism;
(function (prism) {
    'use strict';

    prism.NavController = [
        '$location',
        '$scope',
        function ($location, $scope) {

            var onPath = function (path) {
                switch (path) {
                    case '/':
                        $scope.currentPage = 'home';
                        break;
                    case '/about':
                        $scope.currentPage = 'about';
                        break;
                }
            };

            $scope.location = $location;
            $scope.$watch('location.path()', function (path) {
                return onPath(path);
            });
        }];

})(prism || (prism = {}));
