$(document).ready(function(){

    $('pre code').each(function(i, block) {
    	hljs.highlightBlock(block);
    }); 

    $(".button-collapse").sideNav();
    $(".parallax").parallax();
});
