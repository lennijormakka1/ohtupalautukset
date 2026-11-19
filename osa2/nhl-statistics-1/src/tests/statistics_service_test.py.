import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytamassa_pelaajan(self):
        # Etsitään listalta löytyvää pelaajaa
        pelaaja = self.stats.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")

    def test_search_palauttaa_none_jos_ei_loydy(self):
        # Etsitään pelaajaa jota ei ole olemassa
        pelaaja = self.stats.search("Matti")
        self.assertIsNone(pelaaja)

    def test_team_palauttaa_oikean_maaran_pelaajia(self):
        # EDM-joukkueessa on feikkilistalla 3 pelaajaa (Semenko, Kurri, Gretzky)
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)

    def test_top_palauttaa_parhaan_pelaajan_ensimmaisena(self):
        # Gretzkyllä on eniten pisteitä (35 + 89)
        parhaat = self.stats.top(1)
        self.assertEqual(parhaat[0].name, "Gretzky")