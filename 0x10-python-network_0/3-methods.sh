#!/bin/bash
# curl so to display all the HTTP methods for the server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
