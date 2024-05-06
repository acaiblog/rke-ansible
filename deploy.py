#!/usr/bin/env python
# coding=utf-8
import argparse
import logging
import os

logging.basicConfig(level=logging.DEBUG)

def deploy():
    os.system('ansible-playbook  -i inventory/hosts site.yaml')

if __name__ == "__main__":
    deploy()