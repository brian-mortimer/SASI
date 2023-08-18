/**
 * Sends a question to a chatbot API using the HTTP POST method.
 * @param {string} text - The question to send.
 * @returns {Promise} - A promise that resolves with the response data or rejects with an error.
 */
export function sendQuestion(text){
    // Define URL.
    const url = "http://10.237.222.204:5005/webhooks/rest/webhook";

    // create payload to be sent.
    const payload = {
        "sender": "test_user",
        "message": text
    };

    return fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        console.error('Error:', error);
        return error;
    });
}