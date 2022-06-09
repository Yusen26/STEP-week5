# STEP-week5

# 実行方法

## どの順番でそれぞれの場所をたどったかを調べたい場合

sample_output_generator.pyを実行すると、input_0からinput_6までの入力データに対するoutput_0からoutput_6までの出力データが一斉に得られる。

一つの入力データに対する結果（どの順番でたどったか）を調べたい場合は、solver_greedy_opt.pyのmain関数の中のinput_*.csvのところを変更して実行すればよい。

## 最終的な距離を調べたい場合

output_0.csvからoutput_6.csvを生成できている状態で、output_verifier.pyを実行すると、それぞれの手法を使ったときの最終的な距離が得られる。

# 考え方

greedy探索を用いてまず結果を出して、少しずつ最適化（より良い出力を探す）していく。詳細はGreedy探索の改善策.pptxを参照してください。
