from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """
    Tests to see if a user/vistor is able
    to view the page and its contents
    in a browser and use its functionality
    """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_view_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Django2-bulma-blog", self.browser.title)
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()
