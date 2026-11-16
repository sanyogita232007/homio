async function sendMessage() {
    let input = document.getElementById('user-input');
    let msg = input.value.trim();
    if (!msg) return;

    let chatBox = document.getElementById('chat-box');

    // Tera message dikhao
    chatBox.innerHTML += `<div style="text-align:right; background:#007bff; color:white; padding:8px; border-radius:10px; margin:5px;">${msg}</div>`;
    input.value = '';

    // Ab asli Homio se jawab mango
    let res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
    });
    let data = await res.json();

    chatBox.innerHTML += `<div style="text-align:left; background:#f1f1f1; padding:8px; border-radius:10px; margin:5px;">${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}