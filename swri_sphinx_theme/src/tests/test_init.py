# -*- coding: utf-8 -*-
"""
    unittest for sphinxjp.themes.basicstrap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import mock


class TestGetPath(object):

    def _get_target(self):
        from sphinxjp.themes.basicstrap import get_path
        return get_path

    def _call_fut(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_it(self):
        from sphinxjp.themes import basicstrap
        assert basicstrap.template_path == self._call_fut()


class TestSetup(object):

    def _get_target(self):
        from sphinxjp.themes.basicstrap import setup
        return setup

    def _call_fut(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_it(self):
        dummy_app = "dummy_app"

        with mock.patch('sphinxjp.themes.basicstrap.directives.setup',
                        return_value=True, autospec=True) as mock_func:

            self._call_fut(dummy_app)
            mock_func.assert_called_with(dummy_app)
