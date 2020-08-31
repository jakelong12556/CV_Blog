from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_login_page_and_fail_login(self):
        # A potential employer is interested in my personal
        # website and CV page, they visit the homepage

        self.browser.get('http://localhost:8000')

        # They notices the page title mentions it is my CV Blog page
        self.assertIn('Phan Cuong CV Blog', self.browser.title)

        # They notice the header indicates my name and work
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(
            'Cuong Phan / Illustrator / Programmer Blog', header_text)

        # They notice a suitcase icon next to the header and click on it
        self.browser.get('http://localhost:8000/login')

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(
            'Cuong Phan CV', header_text)

        # They return to main page by clicking on the title header
        self.browser.get('http://localhost:8000')

        # They now click on the CV text under the header title, and is redirected to my CV page.
        self.browser.get('http://localhost:8000/CV')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(
            'Cuong Phan CV', header_text)

        # After reading the contents, they conclude their visit, and exit.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
