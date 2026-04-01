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

"""abydos.tests.phonetic.test_phonetic_koelner.

This module contains unit tests for abydos.phonetic.Koelner
"""

from abydos.phonetic import Koelner


pa = Koelner()

def test_koelner_phonetik():
    """Test abydos.phonetic.Koelner."""
    assert pa.encode('') == ''

    # https://de.wikipedia.org/wiki/K%C3%B6lner_Phonetik
    assert pa.encode('Müller-Lüdenscheidt') == '65752682'
    assert pa.encode('Wikipedia') == '3412'
    assert pa.encode('Breschnew') == '17863'

    # http://search.cpan.org/~maros/Text-Phonetic/lib/Text/Phonetic/Koeln.pm
    assert pa.encode('Müller') == '657'
    assert pa.encode('schmidt') == '862'
    assert pa.encode('schneider') == '8627'
    assert pa.encode('fischer') == '387'
    assert pa.encode('weber') == '317'
    assert pa.encode('meyer') == '67'
    assert pa.encode('wagner') == '3467'
    assert pa.encode('schulz') == '858'
    assert pa.encode('becker') == '147'
    assert pa.encode('hoffmann') == '0366'
    assert pa.encode('schäfer') == '837'
    assert pa.encode('cater') == '427'
    assert pa.encode('axel') == '0485'

    # etc. (for code coverage)
    assert pa.encode('Akxel') == '0485'
    assert pa.encode('Adz') == '08'
    assert pa.encode('Alpharades') == '053728'
    assert pa.encode('Cent') == '862'
    assert pa.encode('Acre') == '087'
    assert pa.encode('H') == ''

def test_koelner_phonetik_alpha():
    """Test abydos.phonetic.Koelner.encode_alpha."""
    assert pa.encode_alpha('Müller-Lüdenscheidt') == 'NLRLTNST'
    assert pa.encode_alpha('Wikipedia') == 'FKPT'
    assert pa.encode_alpha('Breschnew') == 'PRSNF'
    assert pa.encode_alpha('Müller') == 'NLR'
    assert pa.encode_alpha('schmidt') == 'SNT'
    assert pa.encode_alpha('schneider') == 'SNTR'
    assert pa.encode_alpha('fischer') == 'FSR'
    assert pa.encode_alpha('weber') == 'FPR'
    assert pa.encode_alpha('meyer') == 'NR'
    assert pa.encode_alpha('wagner') == 'FKNR'
    assert pa.encode_alpha('schulz') == 'SLS'
    assert pa.encode_alpha('becker') == 'PKR'
    assert pa.encode_alpha('hoffmann') == 'AFNN'
    assert pa.encode_alpha('schäfer') == 'SFR'
    assert pa.encode_alpha('cater') == 'KTR'
    assert pa.encode_alpha('axel') == 'AKSL'
