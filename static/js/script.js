document.addEventListener("DOMContentLoaded", function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarToggler) {
        navbarToggler.addEventListener('click', function() {
            const navbarCollapse = document.getElementById('navbarSupportedContent');
            if (navbarCollapse) {
                navbarCollapse.classList.toggle('show');
            }
        });
    }

    function getCsrfToken() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        return csrfToken;
    }

    function handleFormSubmit(formId, resultContainerId) {
        const form = document.getElementById(formId);
        const resultContainer = document.getElementById(resultContainerId);

        if (form) {
            form.addEventListener('submit', function(event) {
                event.preventDefault();

                const formData = new FormData(form);

                fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': getCsrfToken()
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (resultContainer) {
                        resultContainer.innerHTML = `<p>${data.message}</p>`;
                        resultContainer.style.display = 'block';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });
        }
    }

    handleFormSubmit('example-form-id', 'result-container-id');
});