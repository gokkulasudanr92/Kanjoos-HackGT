(function () {
    angular
        .module('sampleApp')
        .controller('mainController', mainController);

    function mainController(currentUser) {
        var model = this;
    }
})();