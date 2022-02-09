import datetime
import string

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