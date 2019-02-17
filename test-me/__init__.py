# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'minorw'

LOGGER = getLogger(__name__)


class TestMeSkill(MycroftSkill):
    def __init__(self):
        super(TestMeSkill, self).__init__(name="TestMeSkill")

    def initialize(self):
        test_me_on_intent = IntentBuilder("TestMeOnIntent"). \
            require("TestMeOnKeyword").build()
        self.register_intent(test_me_on_intent, 
                             self.handle_test_me_on_intent)

        test_me_off_intent = IntentBuilder("TestMeOffIntent"). \
            require("TestMeOffKeyword").build()
        self.register_intent(test_me_off_intent, 
                             self.handle_test_me_off_intent)

    def handle_test_me_on_intent(self, message):
        self.speak_dialog("test.me.on")
#        print ("test.me.on")
        
	   def handle_test_me_off_intent(self, message):
        self.speak_dialog("test.me.off")
#        print ("test.me.off")

    def stop(self):
        pass

def create_skill():
    return TestMeSkill()
