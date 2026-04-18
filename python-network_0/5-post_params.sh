#!/bin/bash
# Sends a POST request with email and subject variables to a URL
curl -s "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
