var myApp = angular.module('myApp',[]);

myApp.controller('MainCtrl',['$scope', function($scope) {

	$scope.text = "Hello, Im Chris. How You Doooing!";

}]);

myApp.controller('UserCtrl',['$scope',function($scope){
	$scope.user = {};
	$scope.user.details = {
		'username' : 'Chris Niu',
		'id' : '1'
	};


}]);

myApp.directive('customButton', function(){
	return {
		restrict: 'A',
		replace: true,
		transclude: true,
		template: '<a href="" class="myawesomebutton" ng-transclude>' +
                '<i class="icon-ok-sign"></i>' +
              '</a>',
		link: function (scope, element, attrs){

		}
	};
});