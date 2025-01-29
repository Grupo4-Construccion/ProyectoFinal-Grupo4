import unittest
from unittest.mock import MagicMock
from drowsiness_processor.drowsiness_features.processor import DrowsinessProcessor
from drowsiness_processor.drowsiness_features.processing import FeaturesDrowsinessProcessing  # Reemplaza "your_module" con el nombre real del archivo


class TestFeaturesDrowsinessProcessing(unittest.TestCase):
    def setUp(self):
        """ Configura la instancia de FeaturesDrowsinessProcessing con mocks en lugar de las clases reales. """
        self.processor = FeaturesDrowsinessProcessing()

        # Mockeamos los procesadores para evitar dependencia en su implementación real
        for key in self.processor.features_drowsiness:
            self.processor.features_drowsiness[key] = MagicMock(spec=DrowsinessProcessor)
            self.processor.features_drowsiness[key].process.return_value = f"processed_{key}"

    def test_initial_state(self):
        """ Verifica que el diccionario de características procesadas se inicializa en None. """
        expected_state = {
            'eye_rub_first_hand': None,
            'eye_rub_second_hand': None,
            'flicker_and_micro_sleep': None,
            'pitch': None,
            'yawn': None
        }
        self.assertEqual(self.processor.processed_feature, expected_state)

    def test_main_with_all_inputs(self):
        """ Verifica que el método `main` procesa correctamente todas las características cuando se proporcionan datos. """
        distances = {
            'first_hand': {'thumb': 30},
            'second_hand': {'thumb': 35},
            'eyes': {'blink_rate': 0.2},
            'head': {'angle': 10},
            'mouth': {'open_ratio': 0.8}
        }

        result = self.processor.main(distances)

        # Verifica que cada procesador ha sido llamado con los datos correspondientes
        self.processor.features_drowsiness['eye_rub_first_hand'].process.assert_called_with(distances['first_hand'])
        self.processor.features_drowsiness['eye_rub_second_hand'].process.assert_called_with(distances['second_hand'])
        self.processor.features_drowsiness['flicker_and_micro_sleep'].process.assert_called_with(distances['eyes'])
        self.processor.features_drowsiness['pitch'].process.assert_called_with(distances['head'])
        self.processor.features_drowsiness['yawn'].process.assert_called_with(distances['mouth'])

        # Verifica que el resultado es correcto
        expected_output = {
            'eye_rub_first_hand': "processed_eye_rub_first_hand",
            'eye_rub_second_hand': "processed_eye_rub_second_hand",
            'flicker_and_micro_sleep': "processed_flicker_and_micro_sleep",
            'pitch': "processed_pitch",
            'yawn': "processed_yawn"
        }
        self.assertEqual(result, expected_output)

    def test_main_with_missing_inputs(self):
        """ Verifica que el método `main` maneja correctamente la ausencia de ciertos datos en la entrada. """
        distances = {
            'first_hand': {'thumb': 30},
            'eyes': {'blink_rate': 0.2}
        }

        result = self.processor.main(distances)

        # Verifica que se procesaron las entradas proporcionadas
        self.processor.features_drowsiness['eye_rub_first_hand'].process.assert_called_with(distances['first_hand'])
        self.processor.features_drowsiness['eye_rub_second_hand'].process.assert_called_with({})
        self.processor.features_drowsiness['flicker_and_micro_sleep'].process.assert_called_with(distances['eyes'])
        self.processor.features_drowsiness['pitch'].process.assert_called_with({})
        self.processor.features_drowsiness['yawn'].process.assert_called_with({})

        # Verifica que los valores faltantes son manejados correctamente
        expected_output = {
            'eye_rub_first_hand': "processed_eye_rub_first_hand",
            'eye_rub_second_hand': "processed_eye_rub_second_hand",
            'flicker_and_micro_sleep': "processed_flicker_and_micro_sleep",
            'pitch': "processed_pitch",
            'yawn': "processed_yawn"
        }
        self.assertEqual(result, expected_output)

    def test_main_with_empty_input(self):
        """ Verifica que `main` maneja correctamente una entrada vacía y usa valores predeterminados. """
        result = self.processor.main({})

        # Verifica que todos los procesadores fueron llamados con un diccionario vacío
        for key in self.processor.features_drowsiness:
            self.processor.features_drowsiness[key].process.assert_called_with({})

        # Verifica que la salida sigue el formato esperado
        expected_output = {
            'eye_rub_first_hand': "processed_eye_rub_first_hand",
            'eye_rub_second_hand': "processed_eye_rub_second_hand",
            'flicker_and_micro_sleep': "processed_flicker_and_micro_sleep",
            'pitch': "processed_pitch",
            'yawn': "processed_yawn"
        }
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
