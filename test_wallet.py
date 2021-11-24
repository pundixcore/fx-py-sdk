import unittest

import wallet


class MyTestCase(unittest.TestCase):
    def test_seed_to_address(self):
        priv_key = wallet.seed_to_privkey(
            'lonely trumpet tiny soccer brief holiday eye warm credit focus correct april between '
            'armed spoon dice save visit endorse wonder record swim course field')
        self.assertEqual(wallet.privkey_to_address(priv_key), 'fx12fv300avzf266qp930ur4g50agajuz6jcsj5tz')


if __name__ == '__main__':
    unittest.main()
