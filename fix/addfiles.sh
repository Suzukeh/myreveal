SCRIPT_DIR=$(cd $(dirname $0); pwd)
cp ./.nojekyll $SCRIPT_DIR/../docs/
echo $SCRIPT_DIR
rm -rf $SCRIPT_DIR/../docs/_assets/plugin
cp -r $SCRIPT_DIR/../plugin $SCRIPT_DIR/../docs/_assets/plugin
