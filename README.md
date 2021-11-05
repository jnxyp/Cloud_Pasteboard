# Cloud_Pasteboard
A pasteboard API for store and retrieve texts

## APIs

|Url|Method|Parameter|Response|
|-|-|-|-|
|/status|GET|None|"Good!"|
|/p|POST|Form: {'text':text you want to save}|key to retrieve that text|
|/p|GET|?k=key to retrieve that text|text you saved|

## Note
- key is a 6 character string
- the max number of text stored in server is 1000, when overflow, the earlist text saved will be deleted
- the max length of text stored in server is 10000
