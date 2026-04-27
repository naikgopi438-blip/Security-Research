# NASA Recon Findings
- Target: svs.gsfc.nasa.gov
- Findings: CRLF Injection, Staging leak (staging.earth.gov)
- Tools: Termux, Curl, Webhook.site
## Subdomains Found
ingest.eic.earth.gov
sm2a.eic-staging.staging.earth.gov
sealevel.staging.earth.gov
sm2a.eic.earth.gov
sm2a.ghgcenter.earth.gov
sm2a.earth.gov
staging.earth.gov
sm2a.eic.staging.earth.gov
sm2a.staging.earth.gov
tutorials.earth.gov
www.earth.gov
dev.earth.gov
### Critical Discovery: Apache Airflow - Mon Apr 27 18:54:01 IST 2026
- Found Apache Airflow instance on sm2a.staging.earth.gov
- Server detected: gunicorn
- Potential for Unauthenticated Access / Info Leak.
