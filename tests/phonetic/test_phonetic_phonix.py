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

"""abydos.tests.phonetic.test_phonetic_phonix.

This module contains unit tests for abydos.phonetic.Phonix
"""


from abydos.phonetic import Phonix


class TestPhonix:
    """Test Phonix functions.

    test cases for abydos.phonetic.Phonix
    """

    pa = Phonix()

    def test_phonix(self):
        """Test abydos.phonetic.Phonix."""
        assert self.pa.encode('') == '0000'

        # http://cpansearch.perl.org/src/MAROS/Text-Phonetic-2.05/t/007_phonix.t
        assert self.pa.encode('Müller') == 'M400'
        assert self.pa.encode('schneider') == 'S530'
        assert self.pa.encode('fischer') == 'F800'
        assert self.pa.encode('weber') == 'W100'
        assert self.pa.encode('meyer') == 'M000'
        assert self.pa.encode('wagner') == 'W250'
        assert self.pa.encode('schulz') == 'S480'
        assert self.pa.encode('becker') == 'B200'
        assert self.pa.encode('hoffmann') == 'H755'
        assert self.pa.encode('schäfer') == 'S700'
        assert self.pa.encode('schmidt') == 'S530'

        # http://cpansearch.perl.org/src/MAROS/Text-Phonetic-2.05/t/007_phonix.t:
        # testcases from Wais Module
        assert self.pa.encode('computer') == 'K513'
        assert self.pa.encode('computers') == 'K513'
        assert Phonix(5).encode('computers') == 'K5138'
        assert self.pa.encode('pfeifer') == 'F700'
        assert self.pa.encode('pfeiffer') == 'F700'
        assert self.pa.encode('knight') == 'N300'
        assert self.pa.encode('night') == 'N300'

        # http://cpansearch.perl.org/src/MAROS/Text-Phonetic-2.05/t/007_phonix.t:
        # testcases from
        # http://www.cl.uni-heidelberg.de/~bormann/documents/phono/
        # They use a sliglty different algorithm (first char is not included in
        # num code here)
        assert self.pa.encode('wait') == 'W300'
        assert self.pa.encode('weight') == 'W300'
        assert self.pa.encode('gnome') == 'N500'
        assert self.pa.encode('noam') == 'N500'
        assert self.pa.encode('rees') == 'R800'
        assert self.pa.encode('reece') == 'R800'
        assert self.pa.encode('yaeger') == 'v200'

        # http://books.google.com/books?id=xtWPI7Is9wIC&lpg=PA29&ots=DXhaL7ZkvK&dq=phonix%20gadd&pg=PA29#v=onepage&q=phonix%20gadd&f=false
        assert self.pa.encode('alam') == 'v450'
        assert self.pa.encode('berkpakaian') == 'B212'
        assert self.pa.encode('capaian') == 'K150'

        # http://books.google.com/books?id=LZrT6eWf9NMC&lpg=PA76&ots=Tex3FqNwGP&dq=%22phonix%20algorithm%22&pg=PA75#v=onepage&q=%22phonix%20algorithm%22&f=false
        assert self.pa.encode('peter') == 'P300'
        assert self.pa.encode('pete') == 'P300'
        assert self.pa.encode('pedro') == 'P360'
        assert self.pa.encode('stephen') == 'S375'
        assert self.pa.encode('steve') == 'S370'
        assert self.pa.encode('smith') == 'S530'
        assert self.pa.encode('smythe') == 'S530'
        assert self.pa.encode('gail') == 'G400'
        assert self.pa.encode('gayle') == 'G400'
        assert self.pa.encode('christine') == 'K683'
        assert self.pa.encode('christina') == 'K683'
        assert self.pa.encode('kristina') == 'K683'

        # max_length bounds tests
        assert Phonix(max_length=-1).encode('Niall') == 'N4' + '0' * 62
        assert Phonix(max_length=0).encode('Niall') == 'N400'

        # zero_pad tests
        assert Phonix(max_length=-1, zero_pad=False).encode('Niall') == 'N4'
        assert Phonix(max_length=0, zero_pad=False).encode('Niall') == 'N4'
        assert Phonix(max_length=0, zero_pad=True).encode('Niall') == 'N400'
        assert Phonix(max_length=4, zero_pad=False).encode('') == '0'
        assert Phonix(max_length=4, zero_pad=True).encode('') == '0000'

        # encode_alpha
        assert self.pa.encode_alpha('Müller') == 'ML'
        assert self.pa.encode_alpha('schneider') == 'SNT'
        assert self.pa.encode_alpha('fischer') == 'FS'
        assert self.pa.encode_alpha('weber') == 'WP'
