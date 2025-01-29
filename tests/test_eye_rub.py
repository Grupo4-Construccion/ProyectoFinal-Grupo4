import unittest
import time
from drowsiness_processor.drowsiness_features.eye_rub.processing import EyeRubDetection, EyeRubCounter, EyeRubReportGenerator, EyeRubEstimator  # Reemplaza "your_module" con el nombre real del archivo

class TestEyeRubDetection(unittest.TestCase):
    def setUp(self):
        self.detector = EyeRubDetection()

    def test_check_eye_rub_detects_rub(self):
        eye_distance = {'thumb': 30, 'index_finger': 35, 'middle_finger': 50, 'ring_finger': 60, 'little_finger': 45}
        self.assertTrue(self.detector.check_eye_rub(eye_distance))

    def test_check_eye_rub_no_rub(self):
        eye_distance = {'thumb': 50, 'index_finger': 55, 'middle_finger': 60, 'ring_finger': 70, 'little_finger': 80}
        self.assertFalse(self.detector.check_eye_rub(eye_distance))

    def test_detect_eye_rub_short_duration(self):
        self.detector.start_time = time.time()
        time.sleep(0.5)  # Simula un frotamiento corto
        result, duration = self.detector.detect(True)
        self.assertFalse(result)
        self.assertEqual(duration, 0.0)

    def test_detect_eye_rub_valid_duration(self):
        self.detector.start_time = time.time()
        time.sleep(3)  # Simula un frotamiento válido (>1s)
        self.detector.flag = True
        result, duration = self.detector.detect(False)
        self.assertTrue(result)
        self.assertGreater(duration, 1.0)


class TestEyeRubCounter(unittest.TestCase):
    def setUp(self):
        self.counter = EyeRubCounter()

    def test_increment_count(self):
        self.counter.increment(2.0, "right")
        self.assertEqual(self.counter.eye_rub_count, 1)
        self.assertIn("1 right eye rub: 2.0 seconds", self.counter.eye_rub_durations)

    def test_reset_counter(self):
        self.counter.increment(1.5, "left")
        self.counter.reset()
        self.assertEqual(self.counter.eye_rub_count, 0)
        self.assertEqual(len(self.counter.eye_rub_durations), 1)  # No se borra el historial


class TestEyeRubReportGenerator(unittest.TestCase):
    def setUp(self):
        self.report_generator = EyeRubReportGenerator()

    def test_generate_report(self):
        data = {
            "eye_rub_count": 3,
            "eye_rub_durations": ["1 right eye rub: 2.0 seconds", "2 left eye rub: 3.0 seconds"],
            "elapsed_time": 300,
            "eye_rub_report": True
        }
        report = self.report_generator.generate_report(data)
        self.assertEqual(report['eye_rub_count'], 3)
        self.assertIn("1 right eye rub: 2.0 seconds", report['eye_rub_durations'])
        self.assertTrue(report['eye_rub_report'])


class TestEyeRubEstimator(unittest.TestCase):
    def setUp(self):
        self.estimator = EyeRubEstimator()

    def test_process_detects_rub(self):
        hands_points = {
            'hand_to_right_eye': {'thumb': 30, 'index_finger': 35},
            'hand_to_left_eye': {'thumb': 50, 'index_finger': 55}
        }
        report = self.estimator.process(hands_points)
        self.assertIn("report_message", report)
        self.assertFalse(report['eye_rub_report'])

    def test_process_generates_report(self):
        self.estimator.start_report -= 300  # Simula que han pasado 300 segundos
        hands_points = {'hand_to_right_eye': {}, 'hand_to_left_eye': {}}
        report = self.estimator.process(hands_points)
        self.assertTrue(report['eye_rub_report'])

if __name__ == '__main__':
    unittest.main()
