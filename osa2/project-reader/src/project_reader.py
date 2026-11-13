from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url
        

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        tiedot = tomli.loads(content)

        projekti_lokero = tiedot["project"]

        nimi = projekti_lokero["name"]
        kuvaus = projekti_lokero["description"]
        lisenssi = projekti_lokero["license"]
        kirjoittajat = []
        for tekija in projekti_lokero["authors"]:
            kirjoittajat.append(tekija["name"])
        riippuvuudet = []
        for riippuvuus in projekti_lokero["dependencies"]:
            riippuvuudet.append(riippuvuus.split(">=")[0])
        kehitys_riippuvuudet = []
        for riippuvuus in tiedot["dependency-groups"]["dev"]:
            kehitys_riippuvuudet.append(riippuvuus.split(">=")[0])


        return Project(nimi, kuvaus, lisenssi, kirjoittajat, riippuvuudet, kehitys_riippuvuudet)
