"use strict";

jQuery(document).ready(function($)
                       {


	 $(".main_menu a.menu-4").addClass('active');
     $("#menu-container .about").addClass("animated fadeInDown").show();
     $(this).addClass('active');
	
});


function loadScript() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' +
      'callback=initialize';
  document.body.appendChild(script);
}

function initialize() {
    var mapOptions = {
      zoom: 12,
      center: new google.maps.LatLng(16.8251789,96.1439764)
    };
    var map = new google.maps.Map(document.getElementById('templatemo_map'),  mapOptions);
}