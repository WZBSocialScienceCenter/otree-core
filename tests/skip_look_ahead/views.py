# -*- coding: utf-8 -*-
from __future__ import division, absolute_import
from . import models
from otree.api import WaitPage
from tests.utils import BlankTemplatePage as Page
from .models import Constants


class MyWait(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.display_next_page = False


class Page1(Page):
    def is_displayed(self):
        return self.player.display_next_page


page_sequence = [
    MyWait,
    Page1,
]
