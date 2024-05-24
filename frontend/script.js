function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');

    if (userInput.trim() === '') return;

    // Display user message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = 'Você: ' + userInput;
    chatBox.appendChild(userMessageDiv);

    // Clear input
    document.getElementById('user-input').value = '';

    // Send message to backend
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display chatbot response
        const botMessageDiv = document.createElement('div');
        botMessageDiv.textContent = 'Bot: ' + data.response;
        chatBox.appendChild(botMessageDiv);

        // Scroll to the bottom
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error('Error:', error));
}
