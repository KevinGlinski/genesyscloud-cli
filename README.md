# Genesys Cloud CLI

The Genesys Cloud cli is a tool to interact with [Genesys Cloud](https://developer.mypurecloud.com/)

## Install
//TODO: pip install ... ?

## Local setup

The cli authenticates using client credentials which you will have to [create yourself](https://help.mypurecloud.com/articles/create-an-oauth-client/)

```gc profile new``` is the easiest way to setup your credentials.  This will create a credentials file at ~/.genesyscloud/credentials and can support multiple profiles for different organizations.

```
$ gc profile new
Profile Name [DEFAULT]: mycompanyname
Genesys Cloud Environment (mypurecloud.com, usw2.pure.cloud): mypurecloud.com
OAuth Client ID: dfbdc514-e830-4745-bffa-1cb7ee7f2736
OAuth Client Secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

### Profiles
With multiple profiles configured, you can either specify one when connnecting:

```$ gc --profile <profilename> <command> ```

Or switch a named profile to the default

```$ gc profile setdefault <profilename> ```

## Command Structure

The Genesys Cloud cli uses a multipart structure 

```
$ gc <command> <subcommand> [options and params]
```

### Pagination

For resources that have multiple pages such as listing users, there are options available on how to process the pages.  By default the cli uses a page size of 250 and retrieves all items.

 ```
 --page-size    # set a page size other than 250
 --page-number   # return a specific page
 ```

### Data Inputs

Some commands require bodies to be sent with the request, such as creating a new user.  The body can be supplied a number of ways.

1) Passing json with the command
    ```
    $ gc user new "{\"name":\"Joe Smith\"}"
    ```

2) Referencing a file
    ```
    $ gc user new file://user.json
    ```

3) Stream input
    ```
    $ gc user new < user.json
    ```

    ```
    $ echo "{\"name":\"Joe Smith\"}" | gc user new
    ```

## Testing locally
```
$ cd genesyscloudcli
$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
```
