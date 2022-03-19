#!usr/bin/env python3
from os import system
def text_replicator(): print(input('Text: ')*int(input('\nReplicate: '))), input()
while 1:
 user = input('Option 1 - Text Replicator\nOption 2 - Encryption Tool\n\n} ')
 if user == '1':
  system('clear'),text_replicator()
 if user!='1':system('clear')
