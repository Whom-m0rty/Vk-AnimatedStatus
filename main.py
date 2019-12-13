import requests, time
token = '1312313123131231231313' # токен Vk_Api
status = ['NickName: Whom?', 'NickName:  m0rty', 'writing in:  C', 'writing in: Python', 'lzt.org/members/110593/', 'TG: fs_m0rty', 'f_s0ciety'] # Статусы
while True:
    for i in status:
        req = requests.get('https://api.vk.com/method/status.set?text='+ i +'&access_token='+ token +'&v=5.103')
        print(req.text)
        time.sleep(3) # УКАЗЫВАЙТЕ ЗАДЕРЖКУ САМИ( ставьте большую, так как вылетает капча. ) задержка в секундах, учитываете скорость вашего интернета.