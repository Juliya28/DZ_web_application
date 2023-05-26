import requests


def gett(token):
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token}, params={'owner': 'notMe'})  # params={'owner': 'notMe''page': 17
    listcont = [i['content'] for i in g.json()['data']]
    return listcont
 

def test_2(login, text1):
    assert text1 in gett(login)
    
    
def newpost(token):
    a = requests.post('https://test-stand.gb.ru/getway/posts', headers={'X-Auth-Token': token}, 
                      data={ 'title':'Просто новый пост!',
            'description':'Тестируем создание нового поста.',
            'content': 'Создаем новый пост, а потом проверяем его наличие.'} )
    return a.json()


def findpost(token):
    b = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    listmy = [i['description'] for i in b.json()['data']]
    return listmy


def test_3(login, text2):
    assert text2 in findpost(login)