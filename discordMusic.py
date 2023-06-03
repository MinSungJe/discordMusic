import pyautogui

select = pyautogui.confirm(text='디스코드 채팅에 커서를 두고 확인 버튼을 눌러주세요.\n!!! 영어 입력 필수 !!!', title='대기 중', buttons=['OK', 'Cancel'])

if select == 'OK':
    with open('music.txt', 'rt', encoding='UTF8') as m:
        songs = m.readlines()
        for i in range(len(songs)):
            print(songs[i].strip('\n'))
            pyautogui.write('+p '+songs[i].strip('\n'))
            pyautogui.press('enter')
            if i == len(songs)-1 or pyautogui.confirm(text='다음 곡을 입력할까요?', title='대기 중', buttons=['OK', 'Cancel']) == 'Cancel':
                break
        pyautogui.alert(text='입력을 마칩니다.', title='완료', button='OK')

else:
    exit()