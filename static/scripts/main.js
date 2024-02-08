document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("recommendation-form");

    form.addEventListener("submit", function (event) {
        const skillsInput = document.getElementById("skills-input");

        if (skillsInput.value.trim() === "") {
            // Prevent form submission if the input is empty
            event.preventDefault();
            alert("Please enter your interests before getting recommendations!");
        } else {
            // Proceed with form submission when there is content
            // You can add any additional logic here before redirection
            console.log('Form submitted with content:', skillsInput.value);

            // Redirect to r.html with the entered skills as a query parameter
            window.location.href = "r.html";
        }
    });

    document.getElementById('recb').addEventListener('click', function() {
        console.log('Button clicked!');
        window.location.href = 'r.html';
    });

    document.getElementById('recb1').addEventListener('click', function() {
        console.log('Button clicked!');
        sendChatBtn.addEventListener("click", handleChat);
    });
});
