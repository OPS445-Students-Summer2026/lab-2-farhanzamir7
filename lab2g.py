#!/usr/bin/env python3

# Author: Farhan Zamir
# Author ID: 119679181
# Date Created: 2026/05/13

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
