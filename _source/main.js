/* CDCE site script: mobile navigation, footer year, form handling. No tracking, no cookies. */
(function () {
  "use strict";

  // Mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
        toggle.focus();
      }
    });
  }

  // Footer year
  var y = document.querySelectorAll("[data-year]");
  for (var i = 0; i < y.length; i++) y[i].textContent = new Date().getFullYear();

  // Forms: posts to the form service set in the form's action attribute (e.g. Formspree).
  // Until a real endpoint is configured, explain that and point people to email instead.
  var forms = document.querySelectorAll("form[data-cdce-form]");
  Array.prototype.forEach.call(forms, function (form) {
    var status = form.querySelector(".form__status");
    function show(msg, kind) {
      if (!status) return;
      status.textContent = msg;
      status.className = "form__status is-visible form__status--" + kind;
      status.focus();
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var action = form.getAttribute("action") || "";
      if (action.indexOf("YOUR_FORM_ID") !== -1) {
        show("This form isn't connected yet. Please email us at hello@cdce.org.uk and we'll get back to you.", "info");
        return;
      }
      var btn = form.querySelector("[type=submit]");
      if (btn) btn.disabled = true;
      fetch(action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (r) {
          if (!r.ok) throw new Error("bad status");
          form.reset();
          show("Thank you. Your message has been sent and we'll be in touch soon.", "ok");
        })
        .catch(function () {
          show("Sorry, something went wrong sending your message. Please email hello@cdce.org.uk instead.", "info");
        })
        .then(function () { if (btn) btn.disabled = false; });
    });
  });
})();
