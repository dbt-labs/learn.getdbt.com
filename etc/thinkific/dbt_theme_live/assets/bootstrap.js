//
// Tab Hash
// --------------------------------------------------

$('.nav-tabs a[data-toggle="tab"]').click(function(e) {
	var scroll = $(document).scrollTop();
	var tabs = $(this).closest('.nav-tabs');
	window.location.hash = this.hash;
	$("html, body").scrollTop( tabs.offset().top );
});

//
// Tab Scroll & Focus
// --------------------------------------------------

$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
	var target = this.href.split('#');
	var tab = $('.nav a').filter('[href="#'+target[1]+'"]');
	var tabs = tab.closest('.nav-tabs');
	$("html, body").scrollTop( tabs.offset().top );
	tab.tab('show');
});

//
// Collapse
// --------------------------------------------------

$(document).on('click','[data-toggle="collapse"]',function(e) {
	e.preventDefault();
});

//
// Tooltips
// --------------------------------------------------

$(document).tooltip({
	selector: '[data-toggle="tooltip"]',
	placement: function(tip,element){
		return ( $(element).attr('data-placement') ) ? $(element).attr('data-placement') : 'right';
	},
	container: 'body'
});

//
// Popover
// --------------------------------------------------

$('[data-toggle=popover]').popover({container: 'body', html: true});

//
// Carousels
// --------------------------------------------------

$(document).ready(function() {
    $('[data-carousel]').carousel();
});
