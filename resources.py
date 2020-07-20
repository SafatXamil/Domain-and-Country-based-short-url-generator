# contains dictionaries
class Resources(object):
    def __init__(self):
        # reserved code words for hostname
        # this was just for the test. you can add short words for any domain
        self.resv_host = {"airbnb": "ABNB",
                          "samsung": "SMSNG",
                          "flipkart": "FLPKRT",
                          "ebay": "EBAY",
                          "alibaba": "ALIBA",
                          "aliexpress": "ALIEXP",
                          "paytm": "PAYTM",
                          "asus": "ASUS",
                          "github": "GITHB",
                          "aws": "AWS",
                          "bagdoom": "BGDOOM",
                          "pickaboo": "PCKBOO",
                          "chaldal": "CHLDAL",
                          "visa": "VISA",
                          "mastercard": "MSTRCD",
                          "amex": "AMEX",
                          "facebook": "FBOOK",
                          "microsoft": "MSFT",
                          "snapdeal": "SNAPDL",
                          "shopclues": "SHPCLS",
                          "nike": "NIKE",
                          "businessinsider": "BINSDR",
                          "tesla": "TESLA",
                          "netflix": "NTFLX",
                          "amazon": "AMAZN",
                          "booking": "BOOKNG",
                          "uber": "UBER",
                          "lyft": "LYFT",
                          "walmart": "WMRT",
                          "wwe": "WWE",
                          "youtube": "YUTBE",
                          "quora": "QUORA",
                          "redit": "REDIT",
                          "stackoverflow": "STKFLW",
                          "bbc": "BBC",
                          "cnn": "CNN",
                          "wikipedia": "WIKI",
                          "google": "GOOGL",
                          }
        
        # ban adult and other harmful websites
        self.banned_host = ["pornhub", "xvideos", "xnxx", "brazzers", "xhamster", "spankbang"]

        self.country_extension = {"ad": "AND", "com.ad": "AND", "co.ad": "AND",
                                  "ae": "UAE", "com.ae": "UAE", "co.ae": "UAE",
                                  "af": "AFG", "com.af": "AFG", "co.af": "AFG",
                                  "ai": "AIA", "com.ai": "AIA", "co.ai": "AIA",
                                  "al": "ALB", "com.al": "ALB", "co.al": "ALB",
                                  "ar": "ARG", "com.ar": "ARG", "co.ar": "ARG",
                                  "am": "ARM", "com.am": "ARM", "co.am": "ARM",
                                  "au": "AUS", "com.au": "AUS", "co.au": "AUS",
                                  "at": "AUT", "com.at": "AUT", "co.at": "AUT",
                                  "az": "AZE", "com.az": "AZE", "co.az": "AZE",
                                  "bd": "BAN", "com.bd": "BAN", "co.bd": "BAN",
                                  "bg": "BGR", "com.bg": "BGR", "co.bg": "BGR",
                                  "bh": "BHR", "com.bh": "BHR", "co.bh": "BHR",
                                  "be": "BEL", "com.be": "BEL", "co.be": "BEL",
                                  "bo": "BOL", "com.bo": "BOL", "co.bo": "BOL",
                                  "br": "BRA", "com.br": "BRA", "co.br": "BRA",
                                  "ca": "CAN", "com.ca": "CAN", "co.ca": "CAN",
                                  "ch": "SWT", "com.ch": "SWT", "co.ch": "SWT",
                                  "cl": "CHL", "com.cl": "CHL", "co.cl": "CHL",
                                  "cn": "CHN", "com.cn": "CHN", "co.cn": "CHN",
                                  "co": "COL", "com.co": "COL", "co.co": "COL",
                                  "cr": "CRI", "com.cr": "CRI", "co.cr": "CRI",
                                  "cu": "CUB", "com.cu": "CUB", "co.cu": "CUB",
                                  "cz": "CZE", "com.cz": "CZE", "co.cz": "CZE",
                                  "cy": "CYP", "com.cy": "CYP", "co.cy": "CYP",
                                  "de": "GER", "com.de": "GER", "co.de": "GER",
                                  "dk": "DEN", "com.dk": "DEN", "co.dk": "DEN",
                                  "dz": "ALG", "com.dz": "ALG", "co.dz": "ALG",
                                  "ec": "ECU", "com.ec": "ECU", "co.ec": "ECU",
                                  "eg": "EGY", "com.eg": "EGY", "co.eg": "EGY",
                                  "es": "SPA", "com.es": "SPA", "co.es": "SPA",
                                  "et": "ETH", "com.et": "ETH", "co.et": "ETH",
                                  "fi": "FIN", "com.fi": "FIN", "co.fi": "FIN",
                                  "fz": "FJI", "com.fz": "FJI", "co.fz": "FJI",
                                  "fr": "FRA", "com.fr": "FRA", "co.fr": "FRA",
                                  "ge": "GEO", "com.ge": "GEO", "co.ge": "GEO",
                                  "gh": "GHA", "com.gh": "GHA", "co.gh": "GHA",
                                  "gr": "GRC", "com.gr": "GRC", "co.gr": "GRC",
                                  "gl": "GRL", "com.gl": "GRL", "co.gl": "GRL",
                                  "hk": "HKG", "com.hk": "HKG", "co.hk": "HKG",
                                  "hr": "CRO", "com.hr": "CRO", "co.hr": "CRO",
                                  "hu": "HUN", "com.hu": "HUN", "co.hu": "HUN",
                                  "id": "IDN", "com.id": "IDN", "co.id": "IDN",
                                  "in": "IND", "com.in": "IND", "co.in": "IND",
                                  "ie": "IRE", "com.ie": "IRE", "co.ie": "IRE",
                                  "iq": "IRQ", "com.iq": "IRQ", "co.iq": "IRQ",
                                  "ir": "IRN", "com.ir": "IRN", "co.ir": "IRN",
                                  "il": "ISR", "com.il": "ISR", "co.il": "ISR",
                                  "it": "ITA", "com.it": "ITA", "co.it": "ITA",
                                  "jm": "JAM", "com.jm": "JAM", "co.jm": "JAM",
                                  "jp": "JPN", "com.jp": "JPN", "co.jp": "JPN",
                                  "kp": "NKR", "com.kp": "NKR", "co.kp": "NKR",
                                  "kr": "SKR", "com.kr": "SKR", "co.kr": "SKR",
                                  "kw": "KWT", "com.kw": "KWT", "co.kw": "KWT",
                                  "lb": "LBN", "com.lb": "LBN", "co.lb": "LBN",
                                  "lk": "SRI", "com.lk": "SRI", "co.lk": "SRI",
                                  "ly": "LBY", "com.ly": "LBY", "co.ly": "LBY",
                                  "lu": "LUX", "com.lu": "LUX", "co.lu": "LUX",
                                  "ma": "MOR", "com.ma": "MOR", "co.ma": "MOR",
                                  "mx": "MEX", "com.mx": "MEX", "co.mx": "MEX",
                                  "my": "MYS", "com.my": "MYS", "co.my": "MYS",
                                  "ng": "NGA", "com.ng": "NGA", "co.ng": "NGA",
                                  "nl": "NLD", "com.nl": "NLD", "co.nl": "NLD",
                                  "no": "NOR", "com.no": "NOR", "co.no": "NOR",
                                  "nz": "NZL", "com.nz": "NZL", "co.nz": "NZL",
                                  "om": "OMN", "com.om": "OMN", "co.om": "OMN",
                                  "pk": "PAK", "com.pk": "PAK", "co.pk": "PAK",
                                  "pe": "PER", "com.pe": "PER", "co.pe": "PER",
                                  "pl": "POL", "com.pl": "POL", "co.pl": "POL",
                                  "ps": "PSE", "com.ps": "PSE", "co.ps": "PSE",
                                  "pt": "PRT", "com.pt": "PRT", "co.pt": "PRT",
                                  "py": "PRY", "com.py": "PRY", "co.py": "PRY",
                                  "qa": "QAT", "com.qa": "QAT", "co.qa": "QAT",
                                  "ro": "ROM", "com.ro": "ROM", "co.ro": "ROM",
                                  "ru": "RUS", "com.ru": "RUS", "co.ru": "RUS",
                                  "sa": "SAU", "com.sa": "SAU", "co.sa": "SAU",
                                  "sd": "SDN", "com.sd": "SDN", "co.sd": "SDN",
                                  "se": "SWE", "com.se": "SWE", "co.se": "SWE",
                                  "sg": "SGP", "com.sg": "SGP", "co.sg": "SGP",
                                  "sn": "SEN", "com.sn": "SEN", "co.sn": "SEN",
                                  "td": "CHD", "com.td": "CHD", "co.td": "CHD",
                                  "th": "THA", "com.th": "THA", "co.th": "THA",
                                  "tr": "TUR", "com.tr": "TUR", "co.tr": "TUR",
                                  "tw": "TWN", "com.tw": "TWN", "co.tw": "TWN",
                                  "ua": "UKR", "com.ua": "UKR", "co.ua": "UKR",
                                  "ug": "UGA", "com.ug": "UGA", "co.ug": "UGA",
                                  "uk": "ENG", "com.uk": "ENG", "co.uk": "ENG",
                                  "us": "USA", "com.us": "USA", "co.us": "USA",
                                  "uy": "URY", "com.uy": "URY", "co.uy": "URY",
                                  "ve": "VEN", "com.ve": "VEN", "co.ve": "VEN",
                                  "vn": "VNM", "com.vn": "VNM", "co.vn": "VNM",
                                  "ye": "YEM", "com.ye": "YEM", "co.ye": "YEM",
                                  "za": "SAF", "com.za": "SAF", "co.za": "SAF",
                                  "zw": "ZWE", "com.zw": "ZWE", "co.zw": "ZWE",
                                  }