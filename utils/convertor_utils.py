class ConvertorItem:
    def __init__(self, abv: str, name: str, value: float):
        self.abv = abv
        self.name = name
        self.value = value


class ConvertorCategory:
    def __init__(self, name: str, items: list[ConvertorItem], ):
        self.name = name
        self.items = items
        self.selectedFrom = items[0]
        self.selectedTo = items[0]

    def get_conversion(self, value):
        return self.selectedFrom.value / self.selectedTo.value * value


class ConvertorData(ConvertorCategory):
    def __init__(self, name: str, items: list[ConvertorItem]):
        super().__init__(name, items)

    @staticmethod
    def to_base10(value, base: int):
        if base == 2:
            return bin(int(value))
        if base == 8:
            return oct(int(value))
        if base == 16:
            return hex(int(value))

    def get_conversion(self, value):
        if self.selectedFrom.value == 10:
            return self.to_base10(value, int(self.selectedFrom.value))


categories = [
    ConvertorCategory("Distance",
                      [
                          ConvertorItem("KM", "Kilometre", 1000.0),
                          ConvertorItem("HM", "Hectometre", 100.0),
                          ConvertorItem("DAM", "Deca-metre", 10.0),
                          ConvertorItem("M", "metre", 1.0),
                          ConvertorItem("DM", "Decimetre", 0.1),
                          ConvertorItem("CM", "Centimetre", 0.01),
                          ConvertorItem("MM", "Millimetre", 0.001),
                      ],

                      ),
    # ConvertorData("Donnees", [
    #     ConvertorItem("BIN", "Binaire", 2),
    #     ConvertorItem("DEC", "Decimal", 10),
    #     ConvertorItem("OCT", "Octal", 8),
    #     ConvertorItem("HEX", "Hexadecimal", 16),
    #
    # ], )
]
