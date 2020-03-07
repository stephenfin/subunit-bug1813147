import logging
import sys

from oslotest import base

LOG = logging.getLogger(__name__)


def log_rubbish():
    for x in range(10000):
        LOG.debug('This is debug message %d', x)
        LOG.info('This is info message %d', x)
        LOG.warning('This is warning message %d', x)
        LOG.error('This is error message %d', x)
        print(u'This is a unicode error', file=sys.stderr)
        print(b'This is a bytestring error', file=sys.stderr)
        print(u'This is a unicode print', file=sys.stdout)
        print(b'This is a bytestring print', file=sys.stdout)
        print('This is a long error ' + ('foobar ' * 1000), file=sys.stderr)
        print('This is a long print ' + ('foobar ' * 5000), file=sys.stdout)

    raise Exception(b'foo')


class TestUM(base.BaseTestCase):

    def test_assert_raises(self):
        self.assertRaises(Exception, log_rubbish())
