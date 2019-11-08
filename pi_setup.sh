#!/bin/bash
mssh=$(mktemp)
ping raspberrypi -c 1 | grep -o -E "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" > "$mssh"
cat ~/.ssh/id_rsa.pub | ssh pi@"$mssh" 'cat >> ~/.ssh/authorized_keys'
ssh pi@"$mssh"