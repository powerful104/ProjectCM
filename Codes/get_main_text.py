import datetime
import string

"""
get_main_text 함수

매개변수 :
    위의 색정보를 가진 6글자의 문자열
    아래의 색정보를 가진 6글자의 문자열
    그날의 글(문자열)
    게시물 번호(정수)

반환값 :
    인스타 게시물의 본문 부분의 문자열

기능 :
    한글 날짜, 위아래 색 코드, 영어 날짜, 그날의 글, 게시물 번호 등을 포함하여 완성된 글의 형태로 문자열을 반환한다.
    한글 날짜, 영어 날짜는 매개변수로 받아오는게 아닌 해당 모듈에서 datetime을 이용하여 직접 처리한다.
"""

def add_suffix(myDate):
    date_suffix = ["th", "st", "nd", "rd"]
    if myDate % 10 in [1, 2, 3] and myDate not in [11, 12, 13]:
        return str(myDate) + date_suffix[myDate % 10]
    else:
        return str(myDate) + date_suffix[0]

def get_main_text(up_color_code, down_color_code, daily_text, post_num):
    date = datetime.datetime.now()
    main_text = ".\n" + str(date.month) + "월 " + str(date.day) + "일\n색깔\n위 : #" + up_color_code + "\n아래 : #" + down_color_code + \
                "\n\n" + date.strftime("%b ") + add_suffix(int(date.day)) + "\nColor\nUP : #" + up_color_code + "\nDOWN : #" + down_color_code + \
                "\n\n" + daily_text + "\n\n" + "인스타 No." + str(post_num) + " by park_sang\n#색감 #color #"+ up_color_code + \
                " #" + down_color_code + " #색감미술관 #예술 #미술 #감성 #innerpeace #colorsense #colorpalette #art #artist\n@park_sang_daily\n@photo_mixed"
    return main_text

print(get_main_text("6175B9","E0D7B2","좋은하루.", 691))