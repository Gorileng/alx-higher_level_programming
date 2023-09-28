#!/bin/bash
# ends the request so that the URL displays size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
