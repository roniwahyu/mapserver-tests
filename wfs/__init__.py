# -*- coding: utf-8 -*-

import httplib2
from unittest import TestCase

class TestWFS(TestCase):
    url = "http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&"
    http = httplib2.Http()
    
    def _post(self, body):
        resp, content = http.request(self.url, method='POST', body=body);
        self.assertEquals(int(response['status']), 200)
        return content

    def _assert_result_equals(self, content, value):
        for test in zip(unicode(value.decode('utf-8')).split('\n'),
#                unicode(content.decode('utf-8')).split('\n')):
                unicode(content.decode('utf-8')).split('\n')):
            self.assertEquals(test[0], test[1])
