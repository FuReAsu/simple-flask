# simple flask

Just a simple flask app with some pages to test CI/CD pipeline that's all.

## Runtime environment variables

|Name|Description|Default Value|
|---|---|---|
|APP_DATA_PATH|Data directory path|data|
|APP_LOG_PATH|Log directory path|log|
|APP_PORT|Which port the app will run on| 8765|


## Endpoints

`/cookies` sets cookies and and write them back to the page along with client IP.</br>
`/input` accepts inputs and saves them to the data.txt file in `APP_LOG_PATH` directory.

