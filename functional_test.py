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
        self.browser.get('http: // localhost: 8000/CV')

        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn(
            'My CV', header_text)

        # They are redirected to a log-in page with 2 fields and a login button,
        # they enter but they do not have creditentials and so log-in fails

        # They return to main page by clicking on the title header

        # They check out the posts and see a list of blog posts

        # They notice the structure of the post having a published date, a title and a body

        # They click on the first post, and is lead to a detailed page

        # They now click on the CV icon next to the header title, and is redirected to my CV page.

        # After reading the contents, they conclude their visit, and exit.

        # assert 'Phan Cuong CV Blog' in browser.title, "Browser title was " + browser.title
if __name__ == '__main__':
    unittest.main(warnings='ignore')
