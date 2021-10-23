import time
import streamlit as st
def main(i):
    status_area = st.empty()
    count_down_sec = i
    for i in range(count_down_sec):
        time.sleep(1)
st.title("アニバーサリー総選挙2021 予想")
simulation=st.sidebar.radio("何をシミュレーションしますか？",("60連目をシミュレーション","累計報酬をシミュレーション"))
toba=st.sidebar.text_input('名前を入力してください', '調子くん')
team=st.sidebar.radio("自チーム",("福岡ソフトバンクホークス","千葉ロッテマリーンズ","埼玉西武ライオンズ","東北楽天ゴールデンイーグルス","北海道日本ハムファイターズ","オリックス・バファローズ","読売ジャイアンツ","阪神タイガース","中日ドラゴンズ","横浜DeNAベイスターズ","広島東洋カープ","東京ヤクルトスワローズ"))
if team=="福岡ソフトバンクホークス":
        te=0
elif team=="千葉ロッテマリーンズ":
        te=1
elif team=="埼玉西武ライオンズ":
        te=2
elif team=="東北楽天ゴールデンイーグルス":
        te=3
elif team=="北海道日本ハムファイターズ":
        te=4
elif team=="オリックス・バファローズ":
        te=5
elif team=="読売ジャイアンツ":
        te=6
elif team=="阪神タイガース":
        te=7
elif team=="中日ドラゴンズ":
        te=8
elif team=="横浜DeNAベイスターズ":
        te=9
elif team=="広島東洋カープ":
        te=10
elif team=="東京ヤクルトスワローズ":
        te=11

if st.button('予想'):
        import numpy as np
        random=["柳田","千賀","藤原","マーティン","森","外崎","則本","松井","上沢","伊藤","吉田","山本","岡本","菅野","佐藤","藤浪","ビシエド","大野","オースティン","ソト","鈴木","栗林","村上","奥川"]
        one=["千賀","マーティン","森","則本","上沢","吉田","菅野","佐藤","ビシエド","ソト","鈴木","村上"]
        two=["柳田","藤原","外崎","松井","伊藤","山本","岡本","藤浪","大野","オースティン","栗林","奥川"]
        
        if toba=="野﨑康誠":
                one=["戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱"]
                two=["戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱","戸柱"]
        if toba=="佐藤廉":
                one=["源田","源田","源田","源田","源田","源田","衛藤","源田","源田","源田","源田","源田"]
                two=["源田","源田","源田","源田","源田","源田","衛藤","源田","源田","源田","源田","源田"]
        if toba=="大槻亮介":
                one=["三浦","遠藤","斎藤隆","山﨑康晃","ローズ","ブランコ","村田","石井琢朗","筒香","鈴木尚典","高木豊","谷繫"]
                two=["愛萌","愛萌","愛萌","愛萌","愛萌","愛萌","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里"]

        if simulation=="60連目をシミュレーション":
                s=0
                a=0
                b=0
                k=10
                while k>1:
                        main(1)
                        y=np.random.randint(1,1001)
                        se=np.random.randint(1,31)
                        if se<=21:
                            series="Series1"
                        elif 21<=se:
                            series="Series2"
                            se=se-21
                        if y<=25:
                                z=np.random.randint(1,11)
                                if z<=5:
                                        s+=1
                                        st.write("S "+one[np.random.randint(0,12)]+" アニバ")
                                        k-=1
                                else:
                                    if se<=21:
                                        s+=1
                                        st.write("S "+series)
                                        k-=1
                        elif 25<y<=110:
                                z=np.random.randint(1,11)
                                if z<=3:
                                        a+=1
                                        st.write("A "+one[np.random.randint(0,12)]+" アニバ")
                                        k-=1
                                else:
                                        a+=1
                                        st.write("A "+series)
                                        k-=1
                        else:
                                b+=1
                                st.write("B")
                                k-=1
                if k==1:
                        main(1)
                        st.write("S "+one[int(te)])
        main(1)
    
        if simulation=="累計報酬をシミュレーション":
                st.write(one[np.random.randint(0,12)])

   
        if toba=="野崎康誠":
                st.write("文字、間違えてませんか？？")

        if toba=="調子くん":
                st.write("アタリが引けるといいね！！")

        if toba=="調子カス":
                st.write("ハズレが引けるといいね！！")
