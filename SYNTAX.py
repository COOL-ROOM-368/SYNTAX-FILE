import os, sys
os.system('git pull')
try:
    __import__("ANT").main_a()
except Exception as e:
    exit(str(e))
