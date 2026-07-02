import unittest

from model import LinearModel


class LinearModelTests(unittest.TestCase):
    def test_fit_and_predict(self):
        model = LinearModel().fit([1, 2, 3], [3, 5, 7])
        self.assertEqual(model.predict([4, 5]), [9.0, 11.0])

    def test_fit_validates_input_lengths(self):
        with self.assertRaises(ValueError):
            LinearModel().fit([1, 2], [1])

    def test_predict_requires_fit(self):
        with self.assertRaises(ValueError):
            LinearModel().predict([1, 2])


if __name__ == "__main__":
    unittest.main()
