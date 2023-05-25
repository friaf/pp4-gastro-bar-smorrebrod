$(function() {
    $('.carousel').each(function(){
        $(this).carousel({
            interval: false
        });
    });
  });​
  
  
  
  document.querySelectorAll(".nav-link").forEach((link) => {
      if (link.href === window.location.href) {
          link.classList.add("active");
          link.setAttribute("aria-current", "page");
      }
  });
  
  $(document).ready(function() {
      $(".dropdown-toggle").dropdown();
  });
  