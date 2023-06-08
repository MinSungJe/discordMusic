import pyautogui # 라이브러리 import

# 대기창 실행 -> 확인 / 취소 여부 대기
select = pyautogui.confirm(text='디스코드 채팅에 커서를 두고 확인 버튼을 눌러주세요.\n!!! 영어 입력 필수 !!!', title='대기 중', buttons=['OK', 'Cancel'])


# OK
if select == 'OK':
    # open()을 이용해 같은 경로의 music.txt를 읽기 전용으로 열음
    with open('music.txt', 'rt', encoding='UTF8') as m:
        songs = m.readlines()
        for i in range(len(songs)):
            print(songs[i].strip('\n'))
            pyautogui.write('+p '+songs[i].strip('\n')) # 유튜브 링크 한 줄 앞에 +p를 붙인 명령어를 자동 입력
            pyautogui.press('enter') # 엔터키 입력

            # 다음 곡 입력 여부 확인 / 디스코드 자체 렉을 고려
            if i == len(songs)-1 or pyautogui.confirm(text='다음 곡을 입력할까요?', title='대기 중', buttons=['OK', 'Cancel']) == 'Cancel':
                break
        pyautogui.alert(text='입력을 마칩니다.', title='완료', button='OK') # 모든 입력이 마쳤다면 알림창 표시

# Cancel
else:
    exit()