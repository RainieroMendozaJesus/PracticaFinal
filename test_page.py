import unittest

class TestHtml(unittest.TestCase):
    def test_hola_mundo(self):
        with open("index.html", "r") as file:
            content = file.read()
        self.assertIn("<h1>Hola Mundo</h1>", content)

if __name__ == "__main__":
    unittest.main()
