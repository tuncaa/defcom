# defcom
共通処理用

ComDBM(dbname,SQL,dataset):
dbnameに接続して、SQLを実行、結果を返します。
datasetの要素数に応じて、
0:sqlを引数なしで実行:簡易なselect等を想定
1:sqlにdatasetを代入し、実行、comitする
1<:sqlにdatasetを代入し、実行、comitする
