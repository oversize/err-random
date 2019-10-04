import random
import re

pytest_plugins = ["errbot.backends.test"]
extra_plugin_dir = '.'


class TestRandom(object):
    extra_plugin_dir = '.'

    def test_random(self, testbot):
        testbot.push_message('!random')
        assert re.match('\d?. \(1, 100\)', testbot.pop_message())
