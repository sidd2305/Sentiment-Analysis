document.addEventListener("DOMContentLoaded", function () {
    // Add your code to fetch recommendations and dynamically create course cards here
    // Example:
    const recommendations = [
        { name: "Introduction to Python Programming", instructor: "Dr. John Smith", link: "https://example.com/course1" },
        { name: "Web Development with JavaScript", instructor: "Prof. Emily Davis", link: "https://example.com/course2" },
        { name: "Data Science Essentials", instructor: "Dr. Alice Johnson", link: "https://example.com/course3"},
        { name: "Machine Learning Fundamentals", instructor: "Prof. Michael Brown", link: "https://example.com/course4" },
        { name: "Graphic Design Mastery", instructor: "Dr. Sarah Lee", link: "https://example.com/course5" },
        // Add more recommendations as needed
    ];

    const recommendationsContainer = document.getElementById('recommendations-container');

    recommendations.forEach((course, index) => {
        const card = document.createElement('div');
        card.classList.add('course-card');
        card.style.backgroundImage = `url(${course.background})`;

        card.innerHTML = `
            <h2>${course.name}</h2>
            <p>Instructor: ${course.instructor}</p>
            <a href="${course.link}" target="_blank">Course Link</a>
        `;
        recommendationsContainer.appendChild(card);
    });
});
