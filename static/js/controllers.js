var nexisApp = angular.module('nexisApp', []);

nexisApp.controller('CrewMemberCtrl', function ($scope) {
  $scope.members = [
{
      "bio": "This is my:<br><ul><li>bio</li><li>bio</li><li>bio</li><li>bio</li></ul>", 
      "filename": "2637e05.jpg", 
      "github": "rosslazer", 
      "linkedin": "", 
      "major": "Systems & Information Science", 
      "name": "Ross Lazerowitz", 
      "twitter": "@rosslazer"
    }, 
    {
      "bio": "sdfdsfdsfd<b>sfdsf</b>", 
      "filename": "IMG_20141008_202258.jpg", 
      "github": "sdfsdfds", 
      "linkedin": "sdfds", 
      "major": "Systems & Information Science", 
      "name": "f dfgdfg", 
      "twitter": "sdfsf"
    }, 
    {
      "bio": "sdfdsfdsfd<b>sfdsfsdfgfdgfdg</b>", 
      "filename": "IMG_20141008_202258.jpg", 
      "github": "sdfsdfds", 
      "linkedin": "sdfds", 
      "major": "Systems & Information Science", 
      "name": "dgdfgfdgfdgdf", 
      "twitter": "sdfsf"
    }
  ];
});