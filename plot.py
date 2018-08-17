#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import json

class ExpPlot:
    # default settings
    _settings = {
        # drawing settings
        'show': True,                       # whether display the figure
        'legend': True,                     # whether display legend in figure
        'figsize': (8,4),                   # figure size
        'xlim': None,                       # scope of x axis
        'ylim': None,                       # scope of y axis
        'xlabel': 'x',                      # label of x axis
        'ylabel': 'y',                      # label of y axis
        'labelFont': {                      # font style of label
            'size': 15
        }, 
        'save': False,                      # whether save the figure
            'figformat': 'pdf',             # format of the figure
            'savepath': './',               # save path of the figure
            'figname': 'fig',

        # line settings
        'marker': True,                     # whether display markers
        'color': True                       # whether display in different colors
    }

    # color list for lines
    _colorList = [
        'red',
        'blue',
        'black',
        'cyan',
        'magenta',
        'green',
        'gray',
        'yellow',
        'pink'
    ]

    _markerList = [
        '.',         # point marker
        ',',         # pixel marker
        'o',         # circle marker
        'v',         # triangle_down marker
        '^',         # triangle_up marker
        '<',         # triangle_right marker
        '>',         # tri_down marker
        '1',         # tri_up marker
        '2',         # tri_down marker
        '3',         # tri_left marker
        '4',         # tri_right marker
        's',         # square marker
        'p',         # pentagon marker
        '*',         # star marker
        'h',         # hexagon1 marker
        'H',         # hexagon2 marker
        '+',         # plus marker
        'x',         # x marker
        'D',         # diamond marker
        'd',         # thin_diamond marker
        '|',         # vline marker
        '_'          # hline marker
    ]

    def __init__(self, settings_self):
        # 整合settings设置
        if settings_self is not None:
            self._settings = dict(self._settings, **settings_self)

    def _setting(self, key):
        if self._settings.has_key(key):
            return self._settings[key]

    def _getMarker(self, index):
        return self._markerList[index % len(self._markerList)]
    
    def _getColor(self, index):
        return self._colorList[index % len(self._colorList)]
    
    # Example:
    # {
    #     'x': [1,2,3,4],
    #     'y_list': [{
    #         'y':[1,2,3,4],
    #         'settings': {
    #             'label': 'algorithm',
    #             'color': 'red',
    #             'linestyle': '-'
    #             ...
    #         }
    #     },    
    #     {
    #         'y':[1,2,3,4]
    #     }]
    # }
    def plot(self, x, y_list):
        # 按照配置画图
        plt.figure(figsize = self._setting('figsize'))
        # 曲线 marker markersize color label linestyle linewidth
        lineSetting = {
            # 'markersize': None,
            # 'label': None,
            # 'linestyle': None,
            # 'linewidth': None,
            # 'label': None,
            # 'color': 'black'
        }
        index = 0
        for y_info in y_list:
            # 替换settings
            if not self._setting('marker'):
                lineSetting['marker'] = self._getMarker(index)
            if self._setting('color'):
                lineSetting['color'] = self._getColor(index)
            else:
                lineSetting['color'] = 'black'
            if y_info.has_key('settings'):
                lineSetting = dict(lineSetting, **y_info['settings'])
            plt.plot(x, y_info['y'], **lineSetting)
            index += 1
        # 图例
        if self._setting('legend'):
            plt.legend()
        # x, y轴标签
        plt.xlabel(self._setting('xlabel'), self._setting('labelFont'))
        plt.ylabel(self._setting('ylabel'), self._setting('labelFont'))
        # x, y轴的范围
        plt.xlim(self._setting('xlim'))
        plt.ylim(self._setting('ylim'))
        # 保存图片
        if self._setting('save'):
            plt.savefig(self._setting('savepath'))
        # 显示图片
        if self._setting('show'):
            plt.show()

    def start(self):
        str = ''
        with open('./data.json', 'r') as file:
            for line in file:
                str += line.replace('\n', '').replace(' ', '').replace('\'','\"')
        print str    
        data = json.loads(str)
        self.plot(data['x'],data['y_list'])
        

exp=ExpPlot(None)
exp.start()