# Copyright 2026 by OpenAI.
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

"""Tests for abydos.phonetic.Polyphon."""

from abydos.phonetic import Polyphon, Polyphone


def test_polyphon_examples():
    """Test Polyphon against the public upstream examples."""
    pa = Polyphon()

    assert pa.encode('Литие') == 'лата'
    assert pa.encode('ладо') == 'лата'
    assert pa.encode('литье') == 'лата'
    assert pa.encode('летие') == 'лата'
    assert pa.encode('лeто') == 'лата'
    assert pa.encode('леди') == 'лата'


def test_polyphone_alias():
    """Test the Polyphone compatibility alias."""
    assert Polyphone is Polyphon
