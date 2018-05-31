#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib import request
from http import cookiejar

account_dict = {
    '0': {'username': 'xxxx', 'password': 'xxx'},
    '1': {'username': 'yyyy', 'password': 'xxx'},
    '2': {'username': 'zzzz', 'password': 'xxx'},
}


def Login(URL, UserData):
    __cookies = ''
    __cookie = cookiejar.CookieJar()
    __handler = request.HTTPCookieProcessor(__cookie)
    __req = request.Request(URL, data=str(UserData).encode('utf-8'))
    request.build_opener(__handler).open(__req)
    for cookie in __cookie:
        __cookies += cookie.name + '=' + cookie.value + ';'
    return __cookies


def GetPage(URL, Header_Cookies):
    __Header = {'Cookie': str(Header_Cookies)}
    __req = request.Request(URL, headers=__Header)
    return request.urlopen(__req).read().decode('utf-8')


def GetCredit(username, password):
    Login_URL = 'http://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
    My_Home = 'http://www.hostloc.com/home.php?mod=spacecp&inajax=1'

    user_data = 'username=' + str(username) + '&' + 'password=' + str(password)
    My_Cookies = Login(Login_URL, user_data)

    if '<td>' + str(username) + '</td>' not in GetPage(My_Home, My_Cookies):
        isLogin = False
        print('[%s] Login Fail!' % username)
    else:
        isLogin = True
        print('[%s] Login Success!' % username)

    if isLogin:
        for __x in range(25297, 25309):
            __url = 'http://www.hostloc.com/space-uid-{}.html'.format(__x)
            GetPage(__url, My_Cookies)


if __name__ == '__main__':
    for __i in range(0, len(account_dict)):
        GetCredit(account_dict[str(__i)]['username'], account_dict[str(__i)]['password'])
