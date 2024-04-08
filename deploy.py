# coding=utf-8
import argparse
import logging
import os

logging.basicConfig(level=logging.DEBUG)

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, required=True, help='')
    args = parser.parse_args().__dict__
    return args

def deploy():
    os.system('ansible-playbook  -i inventory/hosts -e "k8s_action=%s" site.yaml' %action)

if __name__ == "__main__":
    action = args()['action']
    locals()[action]()