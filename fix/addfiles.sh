#!/bin/bash

SCRIPT_DIR=$1

#SCRIPT_DIR=$(cd $(dirname $0); pwd)
realpath $SCRIPT_DIR

cp $SCRIPT_DIR/fix/.nojekyll $SCRIPT_DIR/docs/
cp $SCRIPT_DIR/fix/CNAME $SCRIPT_DIR/docs/CNAME
cp -r $SCRIPT_DIR/theme $SCRIPT_DIR/docs/_assets/

rm -rf $SCRIPT_DIR/docs/_assets/plugin
cp -r $SCRIPT_DIR/plugin $SCRIPT_DIR/docs/_assets/plugin

rm -rf $SCRIPT_DIR/docs/favicon.ico
cp $SCRIPT_DIR/fix/favicon.ico $SCRIPT_DIR/docs/favicon.ico

