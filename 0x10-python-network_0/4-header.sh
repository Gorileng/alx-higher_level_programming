#!/bin/bash
# Sends the GET request to the given URL with a header variable.
curl -sH "X-School-User-Id: 98" "$1"
