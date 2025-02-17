# -*- coding: utf-8 -*-

from lib.drawable import Drawable
from lib.ui.color import Color
from lib.ui.fonts import FONT_PRIMARY_MEDIUM

class UptimeManagerView(Drawable):
    def __init__(self, uptime_manager):
        self._uptime_manager = uptime_manager
        super().__init__()

    @property
    def width(self):
        return FONT_PRIMARY_MEDIUM.size(u'运行时间 : ' + self._uptime_manager.uptime_text)[0]

    @property
    def height(self):
        return FONT_PRIMARY_MEDIUM.size(u'运行时间 : ' + self._uptime_manager.uptime_text)[1]

    def draw(self, surface):
        surface.blit(FONT_PRIMARY_MEDIUM.render(u'运行时间 : ' + self._uptime_manager.uptime_text, True, Color.WHITE), (512 - self.width / 2, 10))
