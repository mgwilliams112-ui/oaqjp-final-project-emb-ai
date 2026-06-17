import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        phrase1 = emotion_detector('I am glad this happened')
        phrase2 = emotion_detector('I am really mad about this')
        phrase3 = emotion_detector('I feel disgusted just hearing about this')
        phrase4 = emotion_detector('I am so sad about this')
        phrase5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(phrase1['dominant_emotion'], 'joy')
        self.assertEqual(phrase2['dominant_emotion'], 'anger')
        self.assertEqual(phrase3['dominant_emotion'], 'disgust')
        self.assertEqual(phrase4['dominant_emotion'], 'sadness')
        self.assertEqual(phrase5['dominant_emotion'], 'fear')

unittest.main()
