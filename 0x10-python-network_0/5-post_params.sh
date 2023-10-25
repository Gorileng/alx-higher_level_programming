#!/bin/bash
#curl send a POST req to the URL, then display the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
