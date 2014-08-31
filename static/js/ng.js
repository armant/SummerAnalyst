var app = angular.module('app', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('//');
  $interpolateProvider.endSymbol('//');
});

app.controller('FirmFormCtrl', function($scope, $http) {
  $scope.submit = function () {
  	var in_data = { name: $scope.name, app_status: $scope.app_status, 
  	  	deadline: $scope.deadline, reminder_date: $scope.reminder_date, 
  	  	reminder_recurrence_number: $scope.reminder_recurrence_number,
  	  	reminder_recurrence_type: $scope.reminder_recurrence_type }
  	$http.post('NewFirmView', in_data)
  	  .success(function(out_data) {
  	  	alert('Successfully added a firm.');
  	  })
  }
});

