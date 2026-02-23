---
layout: default
title: Help LU
seq: 10
permalink: /participate/
redirect_from:
  - /participate/participate/
  - /help/
---

# How Do I Get Involved?

## [Donate](/participate/donate)

LU uses its funds to start new chapters and provide support and mentorship to existing programs.
[Support our work by donating today.](/participate/donate)

## [Give a Testimonial](/participate/testimonials)

If you attended a program as a student or teacher, or have seen first-hand the impact LU programs can have, help us by [giving us a testimonial](/participate/testimonials).

## [Volunteer](/participate/volunteer/)

Can you help LU or one of our local programs? [Find out more.](/participate/volunteer)

## [Lead](https://docs.google.com/document/d/1-fnodjeNjqJlVq-dnUHs2wpIc-MEtwSCPYcP_gn00XM/edit)

LU has a Board of Directors to lead it into the future. If you would like set the mission for the organization, read more and apply [here](https://docs.google.com/document/d/1Mx9esPYyskLZ3j-QK7Qw2Uu2lJKECRtQYJK0ETBUxbg/edit).

---

Learning Unlimited is driven by its volunteers and supporters. Like the student groups that run Splash and other programs across the country, we are a community of individuals working together to achieve great change. There are many ways to get involved, and we hope that you'll join us as we bring more and more exciting learning and teaching opportunities to students everywhere!

Sign up to receive monthly announcements and events:

<div id="mailing_list">
  <label for="email">Email address:</label>
  <input type="email" id="email_input" placeholder="your@email.com" />
</div>

<script>
  function set_div_class(className) {
    document.getElementById("mailing_list").className = className;
  }

  function submit_email() {
    var xhr = new XMLHttpRequest();
    var email = document.getElementById("email_input").value;
    var data = "ca=41d65ce9-d319-4b8b-a283-eda01fa6d10a&list=1&source=EFD&required=list,email&email=" + encodeURIComponent(email);
    xhr.addEventListener("load", handle_load);
    xhr.addEventListener("error", function() {set_div_class("error");});
    xhr.open("POST", "https://visitor2.constantcontact.com/api/signup")
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('Content-Length', data.length);
    xhr.send(data);
    set_div_class("submitted");
  }

  function handle_load() {
    if (this.responseText && JSON.parse(this.responseText).success) {
      set_div_class("success");
    } else {
      set_div_class("error");
    }
  }
</script>
