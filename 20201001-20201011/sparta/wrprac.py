# 2020.10.02

# 파일 쓰기
# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타!\n")
#
# for i in [1, 2, 3, 4, 5]:
#     f.write(f"{i}번째 줄이에요\n")
# f.close()

# 파일 열기
# 데이터 클렌징
text = ''
with open("kakao_chat.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        # text += line
        input_line = line.split('","')[1][:-2].replace('ㅋ','').replace('ㅜ','')
        input_line += '\n'
        text += input_line.replace('이모티콘\n','').replace('사진\n', '')

print(text)



# wordcloud 만들기
# from wordcloud import WordCloud
#
# wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

# 마스킹된 워드 클라우드 만들기
from wordcloud import WordCloud
from PIL import Image
import numpy as np

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")

# 현재 맥북에 설치되어, 사용가능한 폰트 확인
# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)


