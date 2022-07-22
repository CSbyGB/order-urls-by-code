# Order url by code

This script has been made to get all 400 response code from a list of url.  
I am planning on upgrading it so that it can sort url by response code.

## TODO

- [ ] Make it sort url by code an outputing a different file for each family of code (file for all 400, file for all 500, etc)
- [ ] Handle errors
  - List of errors to handle: 
    - [x] certificate `requests.exceptions.SSLError` `Caused by SSLError(SSLCertVerificationError` - done by using `verify=False`
    - [ ] Failed to connect
- [ ] Make a fancy menu with options and all
