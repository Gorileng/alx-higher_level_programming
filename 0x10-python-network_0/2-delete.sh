#!/bin/bash
# send DELETE req to the $1 URL and displays the response body
curl -s "$1" -X DELETE
