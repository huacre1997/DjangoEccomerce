"use strict";

$(function () {
  $(".js-header-responsive").select2({
    width: 'resolve' // need to override the changed default

  });
  document.querySelectorAll(".tabs").forEach(function (tab) {
    // Selecting headings and blocks with content
    var tabHeading = tab.querySelectorAll(".tabs__heading");
    var tabContent = tab.querySelectorAll(".tabs__content"); // A variable for the data attribute

    var tabName; // For each tab heading...

    tabHeading.forEach(function (element) {
      // ...add event listener
      element.addEventListener("click", function () {
        // Disabling each tab
        tabHeading.forEach(function (item) {
          item.classList.remove("is-active");
        }); // Enabling a tab

        element.classList.add("is-active"); // Getting value from the data attribute

        tabName = element.getAttribute("data-tab-index"); // Checking all the blocks with content

        tabContent.forEach(function (item) {
          // If the item has the same class as the value of the data attribute...
          item.classList.contains(tabName) ? item.classList.add("is-active") : item.classList.remove("is-active"); // Add class 'is-active' to this item
          // Otherwise, remove the class
        });
      });
    });
  });
  var swiper = new Swiper('.swiper-container', {
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      renderBullet: function renderBullet(index, className) {
        console.log(index);
        return '<span class="' + className + '">' + (index + 1) + '</span>';
      }
    }
  });
  $(document).on("click", "#closeModal", function () {
    $(".modal-backdrop").removeClass("modal-backdrop fade show ");
    $("#exampleModal").css("opacity", "0");
  });
  $(document).on("click", "#openModal", function () {
    $("#exampleModal").removeClass("none");
    $("<div class='modal-backdrop  show animated fadeIn'></div>").insertAfter("body");
    $("#exampleModal").css("opacity", "1");
  });

  if (!window.location.href.includes("page") || window.location.href.includes("order") || window.location.href.includes("sc") || window.location.href.includes("price") || !window.location.href.includes() == "") {
    console.log(window.location.href);
    $(".pagination .page-item_list:nth-child(3)").addClass("active");
  }

  $(".children").find("i").remove();
  $('#navbar.navbar-right ul li a').click(function () {
    //clear active status of any parent LI's
    $('#navbar.navbar-right ul li').removeClass('active'); // store id of new active sub-nav

    var currSub = $(this).parent();
    currSub.addClass('active');
    var id = currSub.attr('id'); // clear active status of any sub-nav list

    $('#subnavbar ul.navbar-nav').removeClass('active'); // set selected sub-nav to active

    $('.' + id).addClass('active');
    console.log($('.' + id).attr('class'));
  });
  $(document).on('click', '.tree i', function (e) {
    $(this).parent().siblings('ul').fadeToggle();
    $(this).toggleClass(function () {
      return $(this).is('.fa-angle-right') ? $(this).removeClass("fa-angle-right").addClass("fa-angle-down") : $(this).removeClass("fa-angle-down").addClass("fa-angle-right");
    });
  });
  $(document).on('change', '.tree input[type=checkbox]', function (e) {
    $(this).parent().siblings('ul').find("input[type='checkbox']").prop('checked', this.checked);
    $(this).parentsUntil('.tree').children("input[type='checkbox']").prop('checked', this.checked);
    e.stopPropagation();
  });
  $(".children>ul").hover(function () {
    $(this).css("background-color", "lightgrey").css("border-radius", "0.25em").css("padding", "0 0.5em").css("transition", "0.5s");
  }, function () {
    $(this).css("background-color", "").css("border-radius", "").css("padding", "");
  });
});