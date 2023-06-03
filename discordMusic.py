with open('music.txt', 'rt', encoding='UTF8') as m:
    songs = m.readlines()
    print(songs)
    for i in songs:
        print(i.strip('\n'))