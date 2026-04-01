# Copyright 2014-2020 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.phonetic.test_phonetic_norphone.

This module contains unit tests for abydos.phonetic.Norphone
"""

from abydos.phonetic import Norphone


pa = Norphone()

def test_norphone():
    """Test abydos.phonetic.Norphone."""
    # Base case
    assert pa.encode('') == ''

    # Examples given at
    # https://github.com/larsga/Duke/blob/master/duke-core/src/test/java/no/priv/garshol/duke/comparators/NorphoneComparatorTest.java
    assert pa.encode('Aarestad') == pa.encode('\u00C5rrestad'
    )
    assert pa.encode('Andreasen') == pa.encode('Andreassen'
    )
    assert pa.encode('Arntsen') == pa.encode('Arntzen')
    assert pa.encode('Bache') == pa.encode('Bakke')
    assert pa.encode('Frank') == pa.encode('Franck')
    assert pa.encode('Christian') == pa.encode('Kristian'
    )
    assert pa.encode('Kielland') == pa.encode('Kjelland'
    )
    assert pa.encode('Krogh') == pa.encode('Krog')
    assert pa.encode('Krog') == pa.encode('Krohg')
    assert pa.encode('Jendal') == pa.encode('Jendahl')
    assert pa.encode('Jendal') == pa.encode('Hjendal')
    assert pa.encode('Jendal') == pa.encode('Gjendal')
    assert pa.encode('Vold') == pa.encode('Wold')
    assert pa.encode('Thomas') == pa.encode('Tomas')
    assert pa.encode('Aamodt') == pa.encode('Aamot')
    assert pa.encode('Aksel') == pa.encode('Axel')
    assert pa.encode('Kristoffersen') == pa.encode('Christophersen'
    )
    assert pa.encode('Voll') == pa.encode('Vold')
    assert pa.encode('Granli') == pa.encode('Granlid')
    assert pa.encode('Gjever') == pa.encode('Giever')
    assert pa.encode('Sannerhaugen') == pa.encode('Sanderhaugen'
    )
    assert pa.encode('Jahren') == pa.encode('Jaren')
    assert pa.encode('Amundsrud') == pa.encode('Amundsr\u00F8d'
    )
    assert pa.encode('Karlson') == pa.encode('Carlson')

    # Additional tests to increase coverage
    assert pa.encode('Århus') == 'ÅRHS'
    assert pa.encode('Skyrim') == 'XRM'
    assert pa.encode('kyss') == 'XS'
    assert pa.encode('Äthelwulf') == 'ÆTLVLF'
    assert pa.encode('eit') == 'ÆT'
    assert pa.encode('Öl') == 'ØL'

    # test cases by larsga (the algorithm's author) posted to Reddit
    # https://www.reddit.com/r/norge/comments/vksb5/norphone_mitt_forslag_til_en_norsk_soundex_vel/
    # modified, where necessary to match the "not implemented" rules
    # and rule added after the Reddit post
    reddit_tests = (
        (
            'MKLSN',
            (
                'MICHALSEN',
                'MIKKELSEN',
                'MIKALSEN',
                'MICHAELSEN',
                'MIKAELSEN',
                'MICKAELSEN',
                'MICHELSEN',
                'MIKELSEN',
            ),
        ),
        (
            'BRKR',
            (
                'BERGER',
                'BORGERUD',
                'BURGER',
                'BORGER',
                'BORGAR',
                'BIRGER',
                'BRAGER',
                'BERGERUD',
            ),
        ),
        (
            'TMS',
            (
                'TOMMAS',
                'THOMAS',
                'THAMS',
                'TOUMAS',
                'THOMMAS',
                'TIMMS',
                'TOMAS',
                'TUOMAS',
            ),
        ),
        (
            'HLR',
            (
                'HOLER',
                'HELLERUD',
                'HALLRE',
                'HOLLERUD',
                'HILLER',
                'HALLERUD',
                'HOLLER',
                'HALLER',
            ),
        ),
        (
            'MS',
            (
                'MASS',
                'MMS',
                'MSS',
                'MOES',
                'MEZZO',
                'MESA',
                'MESSE',
                'MOSS',
            ),
        ),
        (
            'HRST',
            (
                'HIRSTI',
                'HAARSETH',
                'HAARSTAD',
                'HARSTAD',
                'HARESTUA',
                'HERSETH',
                'HERSTAD',
                'HERSTUA',
            ),
        ),
        (
            'SVN',
            (
                'SWANN',
                'SVENI',
                'SWAN',
                'SVEN',
                'SVEIN',
                'SVEEN',
                'SVENN',
                'SVANE',
            ),
        ),
        (
            'SLT',
            (
                'SELTE',
                'SALT',
                'SALTE',
                'SLOTT',
                'SLAATTO',
                'SLETT',
                'SLETTA',
                'SLETTE',
            ),
        ),
        (
            'JNSN',
            (
                'JANSSEN',
                'JANSEN',
                'JENSEN',
                'JONASSEN',
                'JANSON',
                'JONSON',
                'JENSSEN',
                'JONSSON',
            ),
        ),
        (
            'ANRSN',
            (
                'ANDRESSEN',
                'ANDERSSON',
                'ANDRESEN',
                'ANDREASSEN',
                'ANDERSEN',
                'ANDERSON',
                'ANDORSEN',
                'ANDERSSEN',
            ),
        ),
        (
            'BRK',
            (
                'BREKKE',
                'BORCH',
                'BRAKKE',
                'BORK',
                'BRECKE',
                'BROCH',
                'BRICK',
                'BRUK',
            ),
        ),
        (
            'LN',
            (
                'LINDE',
                'LENDE',
                'LUND',
                'LAND',
                'LINDA',
                'LANDE',
                'LIND',
                'LUNDE',
            ),
        ),
        (
            'SF',
            (
                'SOPHIE',
                'SFE',
                'SEFF',
                'SEAFOOD',
                'SOFIE',
                'SAFE',
                'SOFI',
                'SOPHIA',
            ),
        ),
        (
            'BRST',
            (
                'BRUASET',
                'BUERSTAD',
                'BARSTAD',
                'BAARSTAD',
                'BRUSETH',
                'BERSTAD',
                'BORSTAD',
                'BRUSTAD',
            ),
        ),
        (
            'OLSN',
            (
                'OHLSSON',
                'OLESEN',
                'OLSSON',
                'OLAUSSON',
                'OLAUSEN',
                'OLAUSSEN',
                'OLSEN',
                'OLSON',
            ),
        ),
        (
            'MKL',
            (
                'MIKAEL',
                'MICHELA',
                'MEIKLE',
                'MIKAL',
                'MIKKEL',
                'MICHEL',
                'MICHAL',
                'MICHAEL',
            ),
        ),
        (
            'HR',
            (
                'HEIER',
                'HAR',
                'HEER',
                'HARRY',
                'HEIR',
                'HURRE',
                'HERO',
                'HUURRE',
            ),
        ),
        (
            'VLM',
            (
                'VILLUM',
                'WOLLUM',
                'WILLIAM',
                'WILLAM',
                'WALLEM',
                'WILLUM',
                'VALUM',
                'WILMO',
            ),
        ),
        (
            'SNS',
            (
                'SYNNES',
                'SINUS',
                'SNUS',
                'SNEIS',
                'SANNES',
                'SUNAAS',
                'SUNNAAS',
                'SAINES',
            ),
        ),
        (
            'SNL',
            (
                'SANDAL',
                'SANDAHL',
                'SUNDEL',
                'SANDLI',
                'SUNNDAL',
                'SANDELL',
                'SANDLIE',
                'SUNDAL',
            ),
        ),
        (
            'VK',
            ('VEKA', 'VIKA', 'WIIK', 'WOK', 'WIKE', 'WEEK', 'VIK', 'VIAK'),
        ),
        (
            'MTS',
            (
                'METSO',
                'MOTHES',
                'MATHIAS',
                'MATHIS',
                'MATTIS',
                'MYTHES',
                'METOS',
                'MATS',
            ),
        ),
    )
    for encoded, names in reddit_tests:
        for name in names:
            assert encoded == pa.encode(name)
