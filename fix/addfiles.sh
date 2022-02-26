SCRIPT_DIR=$(cd $(dirname $0); pwd)
echo $SCRIPT_DIR
cp ./.nojekyll $SCRIPT_DIR/../docs/

rm -rf $SCRIPT_DIR/../docs/_assets/plugin
cp -r $SCRIPT_DIR/../plugin $SCRIPT_DIR/../docs/_assets/plugin
