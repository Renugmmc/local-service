const serviceLink = document.getElementById("serviceId");
const homeLink = document.getElementById("homeId");
const aboutLink = document.getElementById("aboutId");
const contactLink = document.getElementById("contactId");
const bookLink = document.getElementById("bookId");
const registerLink = document.getElementById("registerId");

if (window.location.pathname === "/") {
  homeLink.style.color = "red";
}
if (window.location.pathname === "/service/") {
  serviceLink.style.color = "red";
}
if (window.location.pathname === "/aboutus/") {
  aboutLink.style.color = "red";
}
if (window.location.pathname === "/contact/") {
  contactLink.style.color = "red";
}
if (window.location.pathname === "/table/") {
  bookLink.style.color = "red";
}
if (window.location.pathname === "/register/") {
  registerLink.style.color = "red";
}
