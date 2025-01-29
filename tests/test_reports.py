import os
import unittest
from drowsiness_processor.reports.main import DrowsinessReports

class TestDrowsinessReports(unittest.TestCase):
    def setUp(self):
        self.file_name = 'test_reports.csv'
        self.reports = DrowsinessReports(self.file_name)

    def tearDown(self):
        # Limpia el archivo de pruebas después de cada test
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_create_csv_file(self):
        # Verifica que el archivo CSV se crea correctamente
        self.assertTrue(os.path.exists(self.file_name))

    def test_main_adds_row(self):
        # Prueba la escritura de filas en el archivo CSV
        report_data = {
            'eye_rub_first_hand': {'eye_rub_report': True, 'eye_rub_count': 1, 'eye_rub_durations': [0.5]},
            'eye_rub_second_hand': {'eye_rub_report': False, 'eye_rub_count': 0, 'eye_rub_durations': []},
            'flicker_and_micro_sleep': {'flicker_report': False, 'flicker_count': 0, 'micro_sleep_report': True, 'micro_sleep_count': 1, 'micro_sleep_durations': [1.2]},
            'pitch': {'pitch_report': False, 'pitch_count': 0, 'pitch_durations': []},
            'yawn': {'yawn_report': True, 'yawn_count': 1, 'yawn_durations': [2.3]}
        }
        self.reports.main(report_data)

        with open(self.file_name, 'r') as file:
            rows = file.readlines()
            self.assertEqual(len(rows), 2)  # Encabezado + 1 fila escrita

if __name__ == "__main__":
    unittest.main()
