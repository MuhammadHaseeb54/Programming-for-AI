// Toggle Dark Mode
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    const mode = document.body.classList.contains("dark-mode") ? "Dark" : "Light";
    document.getElementById("modeLabel").innerText = mode + " Mode";
}

// Form Validation for Index (Already added)
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const loader = document.getElementById("loader");

    if (form) {
        form.addEventListener("submit", function (e) {
            const headline = document.getElementById("headline").value.trim();
            const description = document.getElementById("description").value.trim();

            if (!headline || !description) {
                e.preventDefault();
                alert("Both headline and description are required.");
            } else {
                loader.style.display = "block";
            }
        });
    }
});
