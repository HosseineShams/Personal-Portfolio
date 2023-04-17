var toast = {};
toast.show = function(text, options) {
  let defaults = {
    timeout: 5000,
  };
  var settings = $.extend({}, defaults, options);

  if( Math.floor(settings.timeout) != settings.timeout && !$.isNumeric(settings.timeout) ) {
    console.warn('Timeout must be an integer.');
    settings.timeout = 5000;
  }

  var toastHTML = '<div class="toast">';
  toastHTML += '<div class="toast-body">' + text + '</div>';
  toastHTML += '</div>';

  $(toastHTML).appendTo('.toast-container').delay(settings.timeout).queue(function() {
    toast.remove($(this));
    $(this).dequeue();
  });
}

toast.remove = function(el) {
  $(el).addClass('hide');
  setTimeout(function() {
    $(el).remove();
  }, 1000);
}

toast.init = function() {
  $('body').append('<div class="toast-container"></div>');
}

$(document).ready(function() {
  toast.init();
  toast.show('Your message has been sent. Thank you!', {});
});






