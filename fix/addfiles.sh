SCRIPT_DIR=$(cd $(dirname $0); pwd)
echo $SCRIPT_DIR
cp $SCRIPT_DIR/.nojekyll $SCRIPT_DIR/../docs/

rm -rf $SCRIPT_DIR/../docs/_assets/plugin
rm -rf $SCRIPT_DIR/../docs/favicon.ico

cp $SCRIPT_DIR/favicon.ico $SCRIPT_DIR/../docs/favicon.ico
cp -r $SCRIPT_DIR/../plugin $SCRIPT_DIR/../docs/_assets/plugin
