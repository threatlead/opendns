from .context import opendns
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_tld_list(self):
        tlds = opendns.OpenDns.tld_list()
        self.assertGreater(len(tlds), 1500, 'Found a total of {0} threat types'.format(len(tlds)))

    def test_domain_list(self):
        zones = opendns.OpenDns.domain_list()
        self.assertGreater(len(zones), 10000, 'Found a total of {0} threat types'.format(len(zones)))


if __name__ == '__main__':
    unittest.main()
