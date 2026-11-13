class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _asettele_allekkain(self, lista):
        if len(lista) == 0:
            return "-"
        
        teksti = ""
        for asia in lista:
            teksti += f"\n- {asia}"
        return teksti

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license}\n"
            f"\nAuthors:{self._asettele_allekkain(self.authors)}\n"
            f"\nDependencies:{self._asettele_allekkain(self.dependencies)}\n"
            f"\nDevelopment dependencies:{self._asettele_allekkain(self.dev_dependencies)}"
        )
        
