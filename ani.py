import streamlit as st
st.title("アニバーサリー総選挙2021 予想")
st.button('予想をし直す')
import numpy as np
random=["柳田","千賀","藤原","マーティン","森","外崎","則本","松井","上沢","伊藤","吉田","山本","岡本","菅野","佐藤","藤浪","ビシエド","大野","オースティン","ソト","鈴木","栗林","村上","奥川"]
one=[]
two=[]
i=np.random.randint(0,2)
one.append(random[i])
if i%2==0:
    two.append(random[i+1])
else:
    two.append(random[i-1])

i=np.random.randint(2,4)
one.append(random[i])
if i%2==0:
    two.append(random[i+1])
else:
    two.append(random[i-1])

i=np.random.randint(4,6)
one.append(random[i])
if i%2==0:
    two.append(random[i+1])
else:
    two.append(random[i-1])

i=np.random.randint(6,8)
one.append(random[i])
if i%2==0:
    two.append(random[i+1])
else:
    two.append(random[i-1])

i=np.random.randint(8,10)
one.append(random[i])
if i%2==0:
    two.append(random[i+1])
else:
    two.append(random[i-1])

if one[0]=="柳田":
    one.append("山本")
    two.append("吉田")
else:
    one.append("吉田")
    two.append("山本")

i=np.random.randint(12,14)
one.append(random[i])
if i%2==0:
    two.append(random[i+1])
else:
    two.append(random[i-1])

if one[6]=="岡本":
    one.append("佐藤")
    two.append("藤浪")
else:
    one.append("藤波")
    two.append("佐藤")

if one[1]=="マーティン":
    one.append("大野")
    two.append("ビシエド")
else:
    one.append("ビシエド")
    two.append("大野")
    
if one[8]=="ビシエド":
    one.append("オースティン")
    two.append("ソト")   
else:
    one.append("ソト")
    two.append("オースティン")
    
if one[3]=="松井":
    one.append("鈴木")
    two.append("栗林")
else:
    one.append("栗林")
    two.append("鈴木")
    
if one[6]=="岡本":
    one.append("奥川")
    two.append("村上")
else:
    one.append("村上")
    two.append("奥川")

st.header("第一弾")
st.write(one)
st.header("第二弾")
st.write(two)

# チェックボックス
#st.checkbox('ラベル', value=False) # valueは初期状態

# ラジオボタン
#st.radio("ラベル",('選択肢1', '選択肢2', '選択肢3'))

# 選択肢
#st.selectbox('ラベル',('選択肢1', '選択肢2', '選択肢3'))

# 複数選択
#st.multiselect('ラベル', ['選択肢1', '選択肢2', '選択肢3'],初期選択値のリスト)
#st.multiselect('ラベル', ['選択肢1', '選択肢2', '選択肢3'],['選択肢2']) #例

# スライダー
#st.slider('ラベル', 最小値, 最大値, 初期値, 刻み値, フォーマット %d,%fなど)

# テキスト入力
#st.text_input('ラベル', '初期表示文字列')

# 数値入力
#st.number_input('ラベル', 最小値, 最大値, 初期値)

# ファイルアップロード
#st.file_uploader("ラベル", type=ファイルタイプ,encoding) 
# 上限ファイルサイズ200MB, ファイルタイプはcsvやpngなどをstrかlistで与える
