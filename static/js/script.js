document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.querySelector("#taskForm");

    if (taskForm) {
        taskForm.addEventListener("submit", (event) => {
            // FIX: Ensure form is valid BEFORE disabling button
            if (!taskForm.checkValidity()) {
                return; // Let browser display HTML5 validation errors
            }

            const button = taskForm.querySelector("button[type='submit']");
            button.textContent = "Submitting...";
            button.disabled = true;
        });
    }

    // UX Enhancement: Auto-dismiss alert messages after 4 seconds
    const alerts = document.querySelectorAll(".alert");
    if (alerts.length > 0) {
        setTimeout(() => {
            alerts.forEach((alert) => {
                alert.style.transition = "opacity 0.5s ease, transform 0.5s ease";
                alert.style.opacity = "0";
                alert.style.transform = "translateY(-10px)";
                setTimeout(() => alert.remove(), 500);
            });
        }, 4000);
    }
});