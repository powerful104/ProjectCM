from get_color_code import get_color_code
from get_color_value import get_color_value
from get_image import get_image
from get_main_text import get_main_text
from upload_insta import upload_insta

def main():
    print("----- @color__mixed 자동화 프로그램 입니다. -----")
    print("색을 지정할 건지, 랜덤으로 할건지 골라 주십시오.")
    print("1: 색 지정  2: 랜덤")
    print("선택 : ",end='')
    
    flag = int(input())
    if flag == 1:
        print("색을 지정해주십시오 (16진수 RGB 코드로 적어주셔야 합니다.)")
        print("위의 색 : ",end='')
        up_color_code = input()
        print("아래의 색 : ",end='')
        down_color_code = input()
        up_color = (int("0x" + up_color_code[-2:], 16),int("0x" + up_color_code[2:-2], 16),int("0x" + up_color_code[:2], 16))
        down_color = (int("0x" + down_color_code[-2:], 16),int("0x" + down_color_code[2:-2], 16),int("0x" + down_color_code[:2], 16))
    else:
        up_color, down_color = get_color_value()
        up_color_code, down_color_code = get_color_code(up_color, down_color)
    print("오늘의 색")
    print("위: #" + up_color_code)
    print("아래: #" + down_color_code)
    print()
    print("이미지를 생성합니다...")
    get_image(up_color, down_color)
    print("오늘의 글을 적어주십시오.")
    print("입력 : ",end='')
    daily_text = input()
    main_text = get_main_text(up_color_code, down_color_code, daily_text)
    upload_insta(main_text)
    
main()