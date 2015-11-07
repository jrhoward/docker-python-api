# docker-python-api
Example API implementation using Python Flask for the APIs and Ngnix as a reverse proxy and HTTP server.

The API returns UNIX fortune cookies.

A static website served by Ngnix that calls the API and rotates Fortune cookies every 20 seconds.

There is also a slack integration using the slash command.

The run.sh files are self explanatory.

Run for API containers. From the fortune directory with four containers to work with the current Ngnix configuration

```./run.sh 5000 && ./run.sh 5001 && ./run.sh 5002 && ./run.sh 5003```

Run nginx from the nginx directory

``` ./run.sh ```
