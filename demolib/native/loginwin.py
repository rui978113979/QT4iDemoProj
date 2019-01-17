#-*- coding:utf-8 -*-

from qt4i.icontrols import Window
from qt4i.icontrols import Element
from qt4i.qpath import QPath


class LoginWin(Window):
    '''DemoApp 登录页面
    '''

    def __init__(self, app):
        Window.__init__(self, app)
        self._device = self._app.device

        locators = {
              '用户': {'type': Element, 'root': self,
                      'locator': QPath("/classname = 'TextField' & value = 'Email' & visible = true & maxdepth = 8")},
              '密码': {'type': Element, 'root': self,
                     'locator': QPath("/classname = 'TextField' & value = 'Password' & visible = true & maxdepth = 8")},
              '登录': {'type': Element, 'root': self, 
                     'locator': 'Login'},
        }

        self.updateLocator(locators)

    def login(self, user, pwd):
        '''登录
        '''
        user_text_field = self.Controls['用户']
        user_text_field.click()
        user_text_field.value = user
        user_text_field.send_keys('\n')
        pwd_text_field = self.Controls['密码']
        pwd_text_field.click()
        pwd_text_field.value = pwd
        pwd_text_field.send_keys('\n')
        self.Controls['登录'].click()
        return True