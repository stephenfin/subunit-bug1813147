from oslotest import base


class TestUM(base.BaseTestCase):

    def test_numbers_3_4(self):
        self.assertEqual(12, 3 * 4)
