SCRIPT_DIR=$(cd $(dirname $0); pwd)
echo $SCRIPT_DIR
rm -rf $SCRIPT_DIR/docs/
reveal-md $SCRIPT_DIR/md/ --static docs
$SCRIPT_DIR/fix/addfiles.sh
python3 $SCRIPT_DIR/fix/themeURL.py $SCRIPT_DIR/docs/