#!/usr/bin/env python
#implemented on ubuntu 14.04
import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--warning", type=int, help="Set the level for warning messages", default = 5)
parser.add_argument("-c", "--critical", type=int, help="Set the level for critical messages", default = 10)
parser.add_argument("-u", "--user", type=str, help="Monitor for a specific user")
args = parser.parse_args()

critical = args.critical
warning = args.warning
user = args.user

if args.critical < args.warning:
	print('ERROR: Critical threshold must be above warning threshold.')
	sys.exit()

whoout = subprocess.check_output(['who','-q'])

# look for a specific user if user is not None 
if user is None:
	numusers = int(whoout[whoout.index('users')+6:-1])
else:
	numusers = len(whoout.split(user)[:-1])

# trap most severe conditions first
if numusers >= critical:
        print('NUM USERS CRITICAL, numusers: ' + str(numusers))
        sys.exit(2)
elif numusers >= warning:
	print('NUM USERS WARNING, numusers: ' + str(numusers))
	sys.exit(1)	
elif numusers < warning and numusers < critical:
	print('NUM USERS OK')
	sys.exit(0)
