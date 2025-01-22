from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Define test cases
        test_cases = [
            {"statement": "I am glad this happened", "dominant_emotion": "joy"},
            {"statement": "I am really mad about this", "dominant_emotion": "anger"},
            {"statement": "I feel disgusted just hearing about this", "dominant_emotion": "disgust"},
            {"statement": "I am so sad about this", "dominant_emotion": "sadness"},
            {"statement": "I am really afraid that this will happen", "dominant_emotion": "fear"}
        ]

        for test_case in test_cases:
            result = emotion_detector(test_case["statement"])
            self.assertEqual(result["dominant_emotion"], test_case["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()