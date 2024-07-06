// Handle chat form submission
document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission
    const messageInput = document.getElementById('message');
    const message = messageInput.value;
    const chatReplyDiv = document.getElementById('chat-reply');

    // Send POST request to the server
    fetch(this.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: new URLSearchParams({ 'message': message })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            chatReplyDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
        } else {
            chatReplyDiv.innerHTML = `<p><strong>Reply:</strong> ${data.reply}</p>`;
        }
    })
    .catch(error => {
        chatReplyDiv.innerHTML = `<div class="alert alert-danger">An error occurred: ${error.message}</div>`;
    });
});