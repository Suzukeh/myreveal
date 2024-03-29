#!/bin/bash
SCRIPT_DIR=$1
# SCRIPT_DIR=$(cd $(dirname $0); pwd)
realpath $SCRIPT_DIR

cp $SCRIPT_DIR/docs/CNAME $SCRIPT_DIR/fix/CNAME
reveal-md $SCRIPT_DIR/md/ --static docs --glob '**/*_slides.md'

$SCRIPT_DIR/fix/addfiles.sh $SCRIPT_DIR
python3 $SCRIPT_DIR/fix/themeURL.py $SCRIPT_DIR/docs/