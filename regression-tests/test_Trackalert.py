import requests
import socket
import re
import os
import time
import json
import mmap
from test_helper import ApiTestCase

class TestTrackalert(ApiTestCase):

    def test_wforceToTrackalert(self):
        self.writeCmdToConsole("addWebHook(ta_events, tack)")
        r = self.reportFunc('wforce2trackalert', '1.4.3.2', '1234', False); 
        j = r.json()
        self.assertEquals(j['status'], 'ok')
        time.sleep(5)
        logfile = open('/tmp/trackalert.log', 'r')
        s = mmap.mmap(logfile.fileno(), 0, access=mmap.ACCESS_READ)
        for mystring in [ 'login=wforce2trackalert', 'remote=1.4.3.2' ]:
            regex = re.escape(mystring)
            result = re.search(regex, s);
            self.assertNotEquals(result, None)
        s.close()
        logfile.close()

    def test_trackalertReport(self):
        attrs = dict()
        attrs['accountStatus'] = "normal"
        r = self.taReportFuncAttrs('tareportuser', '127.0.0.1', 'foo', True, attrs)
        j = r.json()
        time.sleep(5)
        logfile = open('/tmp/trackalert.log', 'r')
        s = mmap.mmap(logfile.fileno(), 0, access=mmap.ACCESS_READ)
        for mystring in [ 'login=tareportuser', 'remote=127.0.0.1' ]:
            regex = re.escape(mystring)
            result = re.search(regex, s);
            self.assertNotEquals(result, None)
        s.close()
        logfile.close()