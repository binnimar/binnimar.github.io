document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".nav-toggle");
    const navLinks = document.querySelector(".nav-links");

    toggleButton.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });
});

document.querySelector(".nav-toggle").addEventListener("click", function () {
    document.querySelector(".nav-links").classList.toggle("active");
});
