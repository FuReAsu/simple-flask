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
Set this to 1 if there's one reverse proxy for example: nginx -> flask.
Set this to 2 if there's two reverse proxies for example: cloudflare -> nginx -> flask.

## Endpoints

`/cookies` sets cookies and and write them back to the page along with client IP.</br>
`/input` accepts inputs and saves them to the data.txt file in `APP_LOG_PATH` directory.
