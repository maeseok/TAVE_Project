import os

def exists(path):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        os.stat(path)
    except (OSError, ValueError):
        return False
    return True
def get_keywords(keywords_file='keywords.txt'):
    # read search keywords from file
    with open(keywords_file, 'r', encoding='utf-8-sig') as f:
        text = f.read()
        lines = text.split('\n')
        lines = filter(lambda x: x != '' and x is not None, lines)
        keywords = sorted(set(lines))

    print('{} keywords found: {}'.format(len(keywords), keywords))

    # re-save sorted keywords
    with open(keywords_file, 'w+', encoding='utf-8') as f:
        for keyword in keywords:
            f.write('{}\n'.format(keyword))

    return keywords


target="여자배우"
keywords = get_keywords("{}.txt".format(target))

for keyword in keywords:
    CheckData = 0
    dir_name = '{}/{}'.format(target, keyword)
    google_done = os.path.exists(os.path.join(os.getcwd(), dir_name, 'google_done'))
    naver_done = os.path.exists(os.path.join(os.getcwd(), dir_name, 'naver_done'))

    if not google_done and not naver_done:
        CheckData=1
    elif not google_done:
        CheckData=2
    elif not naver_done:
        CheckData=3
    with open("오류명단.txt", 'a+', encoding='utf-8') as f:
        if CheckData==1:
            f.write('{}, 구글, 네이버 미수집\n'.format(keyword))
        elif CheckData==2:
            f.write('{}, 구글 미수집\n'.format(keyword))
        elif CheckData==3:
            f.write('{}, 네이버 미수집\n'.format(keyword))
print("\n[%] 오류명단.txt 생성 완료!")
        