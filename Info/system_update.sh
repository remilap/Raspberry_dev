#!/bin/sh
################################################################################
# 
#-------------------------------------------------------------------------------
# HISTORY:
# 2017-09-04 - R. Lapointe    - Inverse upgrade and dist-upgrade
################################################################################

sudo apt-get update

sudo apt-get dist-upgrade

sudo apt-get upgrade

sudo apt-get autoremove

sudo apt-get clean

