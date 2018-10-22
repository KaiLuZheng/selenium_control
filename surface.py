#!/usr/bin/python3
#-*- encoding: utf8 -*-

###############
# use python3.6
###############

import logging
import tkinter
from tkinter import *


class element_mode():
    ID = 0
    CLASS = 1
    XPATH = 2

ELEMENT_MODE_ID = 0
ELEMENT_MODE_CLASS = 1
ELEMENT_MODE_XPATH = 2


class selenium_operate():
    def __init__(self):
        top = tkinter.Tk()
        top.geometry('1450x700')
        top.title('selenium operate')
        top.resizable(0, 0)
        self.top = top
        
        self.__drawUrlline()
        self.__drawResult()
        self.__drawControls()
       
 
        self.__buttonsStatusInit() 
        self.line_count = 0


    def __drawControls(self):
        click_element_by_id = Button(self.top, text = 'click by id', width = 10, command = self.click_element_by_id)
        click_element_by_id.place(x = 30, y = 60) 
        click_element_by_class = Button(self.top, text = 'click by class', width = 10, command = self.click_element_by_class)
        click_element_by_class.place(x = 30, y = 100)
        
        element_item = Entry(self.top, width = 100)
        element_item.place(x = 150, y = 64)

        self.click_element_by_id = click_element_by_id
        self.click_element_by_class = click_element_by_class
        self.element_item = element_item

        send_keys_by_id = Button(self.top, text = 'send keys', width = 10, command = self.send_keys_by_id)
        send_keys_by_id.place(x = 30, y = 140)
        send_keys_by_class = Button(self.top, text = 'send keys', width = 10, command = self.send_keys_by_class)
        send_keys_by_class.place(x = 30, y = 180)

        keys_value = Entry(self.top, width = 100)
        keys_value.place(x = 150, y = 144)

        self.send_keys_by_id = send_keys_by_id
        self.send_keys_by_class = send_keys_by_class
        self.keys_value = keys_value


        _2frame_id = Button(self.top, text = 'frame id', width = 10, command = self.switch2frame_id)       
        _2frame_id.place(x = 30, y = 220)
        _2frame_class = Button(self.top, text = 'frame class', width = 10, command = self.switch2frame_class)       
        _2frame_class.place(x = 30, y = 260)
        _2frame_xpath = Button(self.top, text = 'frame xpath', width = 10, command = self.switch2frame_xpath)       
        _2frame_xpath.place(x = 30, y = 300)
        _back2frame = Button(self.top, text = 'frame back', width = 10, command = self.back2frame)
        _back2frame.place(x = 30, y = 340)

        self._2frame_id = _2frame_id
        self._2frame_class = _2frame_class
        self._back2frame = _back2frame

    def switch2frame_id(self):
        self.switch2frame(ELEMENT_MODE_ID)
       
    def switch2frame_class(self):
        self.switch2frame(ELEMENT_MODE_CLASS)

    def switch2frame_xpath(self):
        self.switch2frame(ELEMENT_MODE_XPATH)
 
    def switch2frame(self, mode):
        item = self.element_item.get()
        flag = self.check_element(item, mode)
        if flag is False:
            self.__insertResultText('check element failed.')
            return False
        elif flag is True:
            self.__insertResultText('element found ok.')

        if mode == ELEMENT_MODE_ID:
            logging.info('switch frame id')
        elif mode == ELEMENT_MODE_CLASS:
            logging.info('switch frame class')
        elif mode == ELEMENT_MODE_XPATH:
            logging.info('switch frame XPATH')

    def back2frame(self):
        logging.info('back upper frame')

    def send_keys_by_id(self):
        self.send_keys(ELEMENT_MODE_ID)

    def send_keys_by_class(self):
        self.send_keys(ELEMENT_MODE_CLASS)

    def send_keys(self, mode):
        # mode : element_mode
        keys = self.keys_value.get()
        item = self.element_item.get()
        flag = self.check_element(item, mode)
        if flag is False:
            self.__insertResultText('check element failed.')
            return False
        elif flag is True:
            self.__insertResultText('element found ok.')

        if mode == ELEMENT_MODE_ID:
            logging.info('send keys by id')
        elif mode == ELEMENT_MODE_CLASS:
            logging.info('send keys by class')
        elif mode == ELEMENT_MODE_XPATH:
            logging.info('send keys by XPATH')
       
 
    def click_element_by_id(self):
        self.click_element(ELEMENT_MODE_ID)

        
    def click_element_by_class(self):
        self.click_element(ELEMENT_MODE_CLASS)

    def click_element(self, mode):
        # mode : element_mode

        item = self.element_item.get()
        flag = self.check_element(item, mode)
        if flag is False:
            self.__insertResultText('check element failed.')
            return False
        elif flag is True:
            self.__insertResultText('element found ok.')

        if mode == ELEMENT_MODE_ID:
            logging.info('click element by id')
        elif mode == ELEMENT_MODE_CLASS:
            logging.info('click element by class')
        elif mode == ELEMENT_MODE_XPATH:
            logging.info('click element by XPATH')


    def check_element(self, item, mode):
        # mode : element_mode
        if mode == ELEMENT_MODE_ID:
            logging.info('check element by id')
        elif mode == ELEMENT_MODE_CLASS:
            logging.info('check element by class')
        elif mode == ELEMENT_MODE_XPATH:
            logging.info('check element by xpath')
        else:
            logging.warning('check mode error?')
            return False
        return True 

    def __buttonsStatusInit(self):
        logging.debug('init status of buttons.')

    def browserSet(self):
        logging.info('browser set ?')

    def openBrowser(self):
        self.__insertResultText('url test')
        url = self.url_entry.get()
        self.__insertResultText('connect to ' + url)
        try:
            logging.debug('open page %s'%url)
        except Exception as e:
            logging.error('open failed %s'%e)
            return False

        logging.debug('enable buttons')

    def __insertResultText(self, text):
        self.result_block.insert('end', '\r') 
        self.line_count += 1
        br_line = '\n======== new infos above count: %d========\n'%self.line_count
        self.result_block.insert(0.0, text+br_line)
 
    def run(self):
        self.top.mainloop()

    def __drawUrlline(self):
        url_button = Button(self.top, text = 'open', width = 10, command = self.openBrowser)
        url_entry = Entry(self.top, width = 100)
        url_button.place(x = 30, y = 20)
        url_entry.place(x = 150, y = 24)

        self.url_button = url_button
        self.url_entry = url_entry

    def __drawResult(self):
        result_block = Text(self.top, width = 50, height = 30, state = 'normal')
        result_block.place(x = 1000, y = 20)
        self.result_block = result_block

       



if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)
    a = selenium_operate()
    a.run()
