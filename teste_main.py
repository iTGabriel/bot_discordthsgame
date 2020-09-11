import pytest, requests, settings, discord, time, subprocess, signal

import os

def run_sendmessage_client():
    p = subprocess.Popen('python main.py', stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)
    time.sleep(5.0)
    log = open("text_main.txt", "r")
    p.kill()
    return log.read()
    
def test_run_sendmessage_client():
    assert bool(run_sendmessage_client()) == False