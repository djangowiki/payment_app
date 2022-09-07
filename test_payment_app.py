import unittest

from payment_app import PaymentApp


class PaymentAppTestCase(unittest.TestCase):
    # Test Setup
    def setUp(self):
        self.service = PaymentApp(["gabriel", "david", "jeff", "chibie"])

    # Test for adding
    def test_add_user(self):
        self.service.add_user("chioma")
        self.assertIn("chioma", self.service.accounts)

    # Test depositing funds
    def test_deposit(self):
        self.assertEqual(self.service.accounts["gabriel"], 0)
        self.service.deposit("gabriel", 100)
        self.assertEqual(self.service.accounts["gabriel"], 100)

    # Test user withdrawing funds
    def test_withdraw(self):
        self.assertEqual(self.service.accounts["chibie"], 0)
        self.service.deposit("chibie", 40)
        self.service.withdraw("chibie", 30)
        self.assertEqual(self.service.accounts["chibie"], 10)

    # Test user checking balance.
    def test_get_balance(self):
        self.service.deposit("david", 100)
        self.assertEqual(self.service.get_balance("david"), 100)

    # Test user making transfer
    def test_transfer(self):
        self.service.deposit("gabriel", 10)
        self.service.deposit("david", 20)
        self.service.transfer("david", "gabriel", 20)
        self.assertEqual(self.service.accounts["gabriel"], 30)
        self.assertEqual(self.service.accounts["david"], 0)

    # Test user having insufficient funds
    def test_cannot_send_money_with_insufficient_balance(self):
        self.service.deposit("david", 20)
        self.service.deposit("gabriel", 10)

        with self.assertRaises(Exception) as context:
            self.service.transfer("gabriel", "david", 20)

        self.assertTrue("gabriel has insufficient balance" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
