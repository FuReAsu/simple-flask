# simple flask

Just a simple flask app with some pages to test CI/CD pipeline that's all.

## Runtime environment variables

|Name|Description|Default Value|
|---|---|---|
|APP_DATA_PATH|Data directory path|data|
|APP_LOG_PATH|Log directory path|log|
|APP_PORT|Which port the app will run on| 8765|
|REVERSE_PROXIES|How many reverse proxies used| 1|

`REVERSE_PROXIES` is used for flask's proxyFix config that trusts a certain number of proxy header layers.</br>
Set this to 1 if there's one reverse proxy for example: nginx -> flask.</br>
Set this to 2 if there's two reverse proxies for example: cloudflare -> nginx -> flask.

## Endpoints

`/cookies` print out session cookies back to the page has a button to release cookies.</br>
`/input` accepts inputs and saves them to the data.txt file in `APP_LOG_PATH` directory.</br>
`/status` shows client IP, Server Hostname, Host Header value, shows if the server is behing https (kinda unnecessary) , uptime.</br>
`/health` returns json. Intended to be used as healh-check endpoint. Needs improvements.</br>
`/picture` shows an href'ed picture. Just to test referenced media loading.
