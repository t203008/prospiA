import time
import streamlit as st
st.title("アニバーサリー総選挙2021 予想")
toba=st.sidebar.text_input('', 'アニバーサリー総選挙2021')
k=int(st.sidebar.number_input("表示間隔",value=0.5))
def main(i):
    status_area = st.empty()
    count_down_sec = i
    for i in range(count_down_sec):
        time.sleep(k)
simulation=st.sidebar.radio("何をシミュレーションしますか？",("60連目をシミュレーション","累計報酬をシミュレーション"))
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
        
s1_players=["サンチェス","今村信貴","菅野智之","髙橋優貴","戸郷翔征","高梨雄平","中川皓太","大竹寛","鍵谷陽平","デラロサ","大城卓三","中島宏之","吉川尚輝","若林晃弘","岡本和真","坂本勇人","ウィーラー","亀井善行","丸佳浩","松原聖弥","梶谷隆幸",
            "青柳晃洋","福谷浩司","平良拳太郎","森下暢仁","石川雅規","秋山拓巳","柳裕也","濵口遥大","大瀬良大地","スアレス","西勇輝","大野雄大","大貫晋一","九里亜蓮","小川泰弘","ガンケル","小笠原慎之介","ピープルズ","床田寛樹","田口麗斗",
            "伊藤将司","勝野昌慶","今永昇太","野村祐輔","高梨裕稔","馬場皐輔","谷元圭介","山﨑康晃","菊池保則","梅野雄吾","岩崎優","福敬登","エスコバー","塹江敦哉","清水昇","岩貞祐太","祖父江大輔","石田健大","ケムナ誠","マクガフ","小林慶祐",
            "又吉克樹","砂田毅樹","中田廉","今野龍太","スアレス","R.マルティネス","三嶋一輝","栗林良吏","石山泰稚","梅野隆太郎","木下拓哉","戸柱恭孝","會澤翼","西田明央",
            "マルテ","A.マルティネス","ソト","クロン","中村悠平","糸原健斗","ビシエド","牧秀悟","菊池涼介","内川聖一","大山悠輔","阿部寿樹","柴田竜拓","堂林翔太","松本友",
            "木浪聖也","高橋周平","宮﨑敏郎","田中広輔","山田哲人","中野拓夢","京田陽太","大和","小園海斗","村上宗隆","サンズ","福田永将","倉本寿彦","長野久義","西浦直亨",
            "近本光司","根尾昂","佐野恵太","松山竜平","青木宣親","糸井嘉男","大島洋平","神里和毅","西川龍馬","塩見泰隆","佐藤輝明","平田良介","桑原将志","羽月隆太郎","山崎晃大朗",
            "陽川尚将","井領雅貴","オースティン","鈴木誠也","サンタナ","千賀滉大","石川歩","ニール","田中将大","バーヘイゲン","山岡泰輔","東浜巨","小島和哉","松本航","則本昂大","杉浦稔大","田嶋大樹",
            "石川柊太","美馬学","高橋光成","涌井秀章","上沢直之","山本由伸","武田翔太","岩下大輝","平井克典","早川隆久","加藤貴之","宮城大弥","和田毅","二木康太","今井達也","岸孝之","伊藤大海","山﨑福也",
            "嘉弥真新也","東條大樹","森脇亮介","酒居知史","井口和朋","比嘉幹貴","モイネロ","唐川侑己","平良海馬","ブセニッツ","宮西尚生","ヒギンス","泉圭輔","小野郁","ギャレット","牧田和久","堀瑞輝","山田修義",
            "岩嵜翔","佐々木千隼","宮川哲","宋家豪","B.ロドリゲス","富山凌雅","森唯斗","益田直也","増田達至","松井裕樹","秋吉亮","平野佳寿","甲斐拓也","田村龍弘","森友哉","太田光","宇佐見真吾","若月健矢",
            "中村晃","井上晴哉","山川穂高","銀次","頓宮裕真","周東佑京","レアード","外崎修汰","浅村栄斗","渡邉諒","モヤ","牧原大成","中村奨吾","呉念庭","鈴木大地","野村佑希","福田周平",
            "松田宣浩","安田尚憲","中村剛也","黒川史陽","中島卓也","宗佑磨","今宮健太","藤岡裕大","源田壮亮","茂木栄五郎","石井一成","安達了一","グラシアル","荻野貴司","スパンジェンバーグ","小深田大翔","近藤健介","紅林弘太郎",
            "デスパイネ","角中勝也","栗山巧","村林一輝","淺間大基","吉田正尚","長谷川勇也","藤原恭大","若林楽人","島内宏明","王柏融","佐野皓大",
            "柳田悠岐","岡大海","金子侑司","辰己涼介","西川遥輝","ジョーンズ","栗原陵矢","マーティン","愛斗","岡島豪郎","大田泰示","杉本裕太郎"]

a1_players=["サンチェス","今村信貴","菅野智之","畠世周","戸郷翔征","高梨雄平","中川皓太","大竹寛","鍵谷陽平","デラロサ","大城卓三","中島宏之","吉川尚輝","岡本和真","坂本勇人","ウィーラー","亀井善行","丸佳浩","松原聖弥","梶谷隆幸",
            "青柳晃洋","福谷浩司","平良拳太郎","森下暢仁","石川雅規","秋山拓巳","柳裕也","濵口遥大","大瀬良大地","スアレス","西勇輝","大野雄大","大貫晋一","九里亜蓮","小川泰弘","チェン ウェイン","松葉貴大","上茶谷大河","遠藤淳志","原樹里",
            "髙橋遥人","勝野昌慶","阪口皓亮","野村祐輔","高梨裕稔","馬場皐輔","谷元圭介","山﨑康晃","菊池保則","梅野雄吾","岩崎優","福敬登","エスコバー","塹江敦哉","清水昇","岩貞祐太","祖父江大輔","平田真吾","ケムナ誠","マクガフ","エドワーズ",
            "又吉克樹","中田廉","梅野雄吾","スアレス","R.マルティネス","三嶋一輝","栗林良吏","石山泰稚","梅野隆太郎","木下拓哉","戸柱恭孝","會澤翼","西田明央",
            "マルテ","A.マルティネス","ソト","クロン","糸原健斗","ビシエド","牧秀悟","菊池涼介","坂口智隆","大山悠輔","阿部寿樹","柴田竜拓","堂林翔太","松本友",
            "木浪聖也","高橋周平","宮﨑敏郎","田中広輔","山田哲人","中野拓夢","京田陽太","大和","小園海斗","村上宗隆","サンズ","福田永将","長野久義","西浦直亨",
            "近本光司","根尾昂","佐野恵太","松山竜平","青木宣親","糸井嘉男","大島洋平","神里和毅","西川龍馬","塩見泰隆","佐藤輝明","平田良介","桑原将志","山崎晃大朗",
            "オースティン","鈴木誠也","雄平","千賀滉大","石川歩","ニール","田中将大","バーヘイゲン","山岡泰輔","東浜巨","小島和哉","松本航","則本昂大","杉浦稔大","田嶋大樹",
            "石川柊太","美馬学","高橋光成","涌井秀章","上沢直之","山本由伸","笠谷俊介","岩下大輝","浜屋将太","塩見貴洋","加藤貴之","増井浩俊","和田毅","二木康太","今井達也","岸孝之","河野竜生","山﨑福也",
            "嘉弥真新也","東條大樹","森脇亮介","酒居知史","井口和朋","比嘉幹貴","モイネロ","唐川侑己","平良海馬","ブセニッツ","宮西尚生","ヒギンス","泉圭輔","小野郁","ギャレット","牧田和久","堀瑞輝","山田修義",
            "高橋礼","松永昂大","宮川哲","宋家豪","公文克彦","吉田凌","森唯斗","益田直也","増田達至","松井裕樹","秋吉亮","平野佳寿","甲斐拓也","田村龍弘","森友哉","太田光","宇佐見真吾","若月健矢",
            "中村晃","井上晴哉","山川穂高","銀次","周東佑京","レアード","外崎修汰","浅村栄斗","渡邉諒","T-岡田","中村奨吾","鈴木大地","野村佑希","福田周平",
            "松田宣浩","安田尚憲","中村剛也","中島卓也","宗佑磨","今宮健太","藤岡裕大","源田壮亮","茂木栄五郎","石井一成","安達了一","グラシアル","荻野貴司","スパンジェンバーグ","小深田大翔","近藤健介","紅林弘太郎",
            "デスパイネ","角中勝也","栗山巧","村林一輝","淺間大基","吉田正尚","長谷川勇也","藤原恭大","若林楽人","島内宏明","佐野皓大",
            "柳田悠岐","金子侑司","辰己涼介","西川遥輝","ジョーンズ","栗原陵矢","マーティン","田中和基","大田泰示","杉本裕太郎"]

s2_players=["マルティネス","三森大貴","嘉弥真新也","石川柊太","栗原陵矢","モイネロ","松田宣浩","甲斐拓也","グラシアル","小島和哉","中村奨吾","唐川侑己","岩下大輝","マーティン","益田直也","安田尚憲","田村龍弘","荻野貴司",
           "今井達也","外崎修汰","平良海馬","松本航","愛斗","増田達至","中村剛也","森友哉","栗山巧","早川隆久","浅村栄斗","宋家豪","則本昂大","岡島豪郎","松井裕樹","茂木栄五郎","炭谷銀仁朗","島内宏明",
           "池田隆英","渡邉諒","堀瑞輝","伊藤大海","近藤健介","杉浦稔大","野村佑希","清水優心","西川遥輝","田嶋大樹","安達了一","富山凌雅","宮城大弥","杉本裕太郎","平野佳寿","宗佑磨","伏見寅威","吉田正尚",
           "菅野智之","吉川尚輝","中川皓太","戸郷翔征","梶谷隆幸","ビエイラ","岡本和真","大城卓三","松原聖弥","西勇輝","糸原健斗","岩崎優","ガンケル","佐藤輝明","スアレス","大山悠輔","梅野隆太郎","サンズ",
           "小笠原慎之介","阿部寿樹","又吉克樹","大野雄大","福留孝介","R.マルティネス","高橋周平","木下拓哉","福田永将","今永昇太","牧秀悟","山﨑康晃","大貫晋一","オースティン","三嶋一輝","宮﨑敏郎","伊藤光","佐野恵太",
           "大瀬良大地","菊池涼介","塹江敦哉","九里亜蓮","鈴木誠也","栗林良吏","林晃汰","坂倉将吾","西川龍馬","金久保優斗","山田哲人","清水昇","田口麗斗","サンタナ","マクガフ","村上宗隆","中村悠平","青木宣親"]

a2_players=["マルティネス","岩嵜翔","嘉弥真新也","今宮健太","栗原陵矢","石川柊太","武田翔太","甲斐拓也","グラシアル","小島和哉","佐々木千隼","唐川侑己","岩下大輝","マーティン","鈴木昭汰","角中勝也","田村龍弘","藤岡裕大",
           "今井達也","ギャレット","平良海馬","松本航","愛斗","平井克典","源田壮亮","森友哉","栗山巧","早川隆久","酒居知史","宋家豪","則本昂大","岡島豪郎","岸孝之","小深田大翔","太田光","島内宏明",
           "池田隆英","河野竜生","堀瑞輝","伊藤大海","近藤健介","バーヘイゲン","石井一成","清水優心","西川遥輝","田嶋大樹","ヒギンス","富山凌雅","宮城大弥","杉本裕太郎","山﨑福也","紅林弘太郎","伏見寅威","吉田正尚",
           "菅野智之","鍵谷陽平","中川皓太","戸郷翔征","梶谷隆幸","今村信貴","坂本勇人","大城卓三","松原聖弥","西勇輝","岩貞祐太","岩崎優","ガンケル","佐藤輝明","秋山拓巳","中野拓夢","梅野隆太郎","サンズ",
           "小笠原慎之介","福敬登","又吉克樹","大野雄大","福留孝介","福谷浩司","京田陽太","木下拓哉","福田永将","今永昇太","エスコバー","山﨑康晃","大貫晋一","オースティン","阪口皓亮","大和","伊藤光","佐野恵太",
           "大瀬良大地","コルニエル","塹江敦哉","九里亜蓮","鈴木誠也","床田寛樹","小園海斗","坂倉将吾","西川龍馬","金久保優斗","今野龍太","清水昇","田口麗斗","サンタナ","奥川恭伸","元山飛優","中村悠平","青木宣親"]

if st.button('予想'):
        import numpy as np
        one=["千賀滉大","マーティン","森友哉","則本昂大","上沢直之","吉田正尚","菅野智之","佐藤輝明","ビシエド","ソト","栗林良吏","村上宗隆"]
        two=["柳田悠岐","藤原恭大","外崎修汰","松井裕樹","伊藤大海","山本由伸","岡本和真","藤浪晋太郎","大野雄大","オースティン","鈴木誠也","奥川恭伸"]
        
        if toba=="野﨑康誠":
                one=["戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝"]
                two=["戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝","戸柱恭孝"]
        if toba=="佐藤廉":
                one=["源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮"]
                two=["源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮","源田壮亮"]
        if toba=="大槻亮介":
                one=["宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌","宮田愛萌"]
                two=["斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里","斉藤優里"]

        if simulation=="60連目をシミュレーション":
                s=0
                a=0
                b=0
                k=10
                while k>1:
                        main(1)
                        y=np.random.randint(1,1001)
                        se=np.random.randint(1,31)
                        bse=np.random.randint(1,33)
                        if se<=21:
                            play=0
                            series="Series1"
                            se=str(se)
                        elif 21<se:
                            play=1
                            series="Series2"
                            se=str(se-21)
                        if bse<=23:
                            bseries="Series1"
                            bse=str(bse)
                        elif 23<bse:
                            bseries="Series2"
                            bse=str(bse-23)
                        if y<=25:
                                z=np.random.randint(1,11)
                                if z<=5:
                                        s+=1
                                        st.write("S　アニバ　"+one[np.random.randint(0,12)])
                                        k-=1
                                else:
                                        s+=1
                                        if play==0:
                                            st.write("S　"+series+"　"+s1_players[np.random.randint(0,252)])
                                        else:
                                            st.write("S　"+series+"　"+s2_players[np.random.randint(0,109)])
                                        k-=1
                        elif 25<y<=110:
                                z=np.random.randint(1,11)
                                if z<=3:
                                        a+=1
                                        st.write("A　アニバ　"+one[np.random.randint(0,12)])
                                        k-=1
                                else:
                                        a+=1
                                        if play==0:
                                            st.write("A　"+series+"　"+a1_players[np.random.randint(0,238)])
                                        else:
                                            st.write("A　"+series+"　"+a2_players[np.random.randint(0,109)])
                                        k-=1
                        else:
                                b+=1
                                st.write("B")
                                k-=1
                if k==1:
                        main(1)
                        st.write("S　アニバ　"+one[int(te)])
        main(1)
    
        if simulation=="累計報酬をシミュレーション":
                st.write(one[np.random.randint(0,12)])

   
        if toba=="野崎康誠":
                st.write("文字、間違えてませんか？？")

        if toba=="調子くん":
                st.write("アタリが引けるといいね！！")

        if toba=="調子カス":
                st.write("ハズレが引けるといいね！！")
