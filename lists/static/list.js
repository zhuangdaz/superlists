window.Superlists = {};

window.Superlists.initialize = function () {
  $('input[name="text"]').on('keypress click', function() {
    console.log('in keypress handler');
    $('.has-error').hide();
  });
};
