# myreveal

スライドをreveal.jsで作ってるからGithub Pagesに置いときたい

## メモ

[reveal-md](https://github.com/webpro/reveal-md)を使う

1. スライドを `md/foo/foo_slides.md` に作る
1. ` reveal-md md/ -w` でライブリロードのプレビュー
1. `reveal-md md/ --static bar` でbarディレクトリ下に`foo.html` とその他を生成
1. barディレクトリを公開

ここらへんをまとめて`static.sh`にしている。themeURL.pyはreveal-mdの[バグによる壊れたパス](https://github.com/webpro/reveal-md/issues/403#issue-1100518130)を修復するやつ。
