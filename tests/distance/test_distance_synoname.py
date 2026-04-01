# Copyright 2018-2020 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_synoname.

This module contains unit tests for abydos.distance.Synoname
"""

import pytest

from abydos.distance import Synoname


class TestSynoname:
    """Test Synoname functions.

    abydos.distance.Synoname
    """

    cmp = Synoname()

    def test_synoname_strip_punct(self):
        """Test abydos.distance.Synoname._synoname_strip_punct."""
        # Base case
        assert self.cmp._synoname_strip_punct('') == ''  # noqa: SF01

        assert self.cmp._synoname_strip_punct('abcdefg') == 'abcdefg'  # noqa: SF01
        assert self.cmp._synoname_strip_punct("a'b-c,d!e:f%g") == 'abcdefg'  # noqa: SF01

    def test_synoname_word_approximation(self):
        """Test abydos.distance.Synoname._synoname_word_approximation."""
        # Base case
        assert self.cmp._synoname_word_approximation('', '') == 0  # noqa: SF01

        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'di Domenico di Bonaventura',
            'di Tomme di Nuto',
            'Cosimo',
            'Luca',
        ) == 0.4
        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'Antonello da Messina',
            'Messina',
            '',
            'Antonello da',
            {
                'gen_conflict': False,
                'roman_conflict': False,
                'src_specials': [(35, 'b'), (35, 'c')],
                'tar_specials': [(35, 'b'), (35, 'c')],
            },
        ) == 0
        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'louis ii',
            'louis ii',
            'sr jean',
            'sr  pierre',
            {
                'gen_conflict': False,
                'roman_conflict': False,
                'src_specials': [(49, 'b'), (68, 'd'), (121, 'b')],
                'tar_specials': [(49, 'b'), (68, 'd'), (121, 'b')],
            },
        ) == 0
        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'louis ii',
            'louis ii',
            'il giovane',
            'sr cadet',
            {
                'gen_conflict': False,
                'roman_conflict': False,
                'src_specials': [
                    (46, 'a'),
                    (49, 'b'),
                    (52, 'a'),
                    (68, 'd'),
                ],
                'tar_specials': [
                    (8, 'a'),
                    (49, 'b'),
                    (68, 'd'),
                    (121, 'a'),
                ],
            },
        ) == 1
        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'louis ii',
            'louis ii',
            'ste.-geo ste.',
            'ste.-jo ste.',
            {
                'gen_conflict': False,
                'roman_conflict': False,
                'src_specials': [
                    (49, 'b'),
                    (68, 'd'),
                    (127, 'b'),
                    (127, 'X'),
                ],
                'tar_specials': [
                    (49, 'b'),
                    (68, 'd'),
                    (127, 'b'),
                    (127, 'X'),
                ],
            },
        ) == pytest.approx(abs=1e-7, expected=2 / 3)
        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'louis ii',
            'louis',
            'ste.-geo ste.',
            '',
            {
                'gen_conflict': False,
                'roman_conflict': False,
                'src_specials': [
                    (49, 'b'),
                    (68, 'd'),
                    (127, 'b'),
                    (127, 'X'),
                ],
                'tar_specials': [],
            },
        ) == pytest.approx(abs=1e-7, expected=0)
        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'lou ii', 'louis', 'louis iv', 'ste.', {}
        ) == pytest.approx(abs=1e-7, expected=0)
        assert self.cmp._synoname_word_approximation(  # noqa: SF01
            'ren',
            'loren ste.',
            '',
            '',
            {
                'tar_specials': [(68, 'd'), (127, 'X')],
                'src_specials': [(0, '')],
            },
        ) == 1

    def test_synoname_sim_type(self):
        """Test abydos.distance.Synoname.sim_type."""
        assert self.cmp.sim_type('', '') == 1
        assert Synoname(tests=['exact']).sim_type('', '') == 1
        assert Synoname(tests=[]).sim_type('', '') == 13
        assert Synoname(tests=['nonsense-test']).sim_type('', '') == 13
        assert Synoname(ret_name=True).sim_type('', '') == 'exact'

        # Types 1-12
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel', 'Pieter', ''), ('Brueghel', 'Pieter', '')
        ) == 'exact'

        assert Synoname(ret_name=True).sim_type(
            ('Brueghel II', 'Pieter', ''), ('Brueghel I', 'Pieter', '')
        ) == 'no_match'
        assert Synoname(ret_name=True).sim_type(
            ('Breghel', 'Pieter', ''), ('Brueghel', 'Pieter', '')
        ) == 'omission'
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel', 'Pieter', ''), ('Breghel', 'Pieter', '')
        ) == 'omission'
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel', 'Piter', ''), ('Brueghel', 'Pieter', '')
        ) == 'omission'
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel', 'Pieter', ''), ('Brueghel', 'Piter', '')
        ) == 'omission'
        assert Synoname(ret_name=True).sim_type(
            ('Brughel', 'Pieter', ''), ('Breghel', 'Pieter', '')
        ) == 'substitution'
        assert Synoname(ret_name=True).sim_type(
            ('Breughel', 'Peter', ''), ('Breughel', 'Piter', '')
        ) == 'substitution'
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel', 'Pieter', ''), ('Breughel', 'Pieter', '')
        ) == 'transposition'
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel', 'Peiter', ''), ('Brueghel', 'Pieter', '')
        ) == 'transposition'

        assert Synoname(ret_name=True).sim_type(
            ('Brueghel:', 'Pieter', ''), ('Brueghel', 'Pi-eter', '')
        ) == 'punctuation'
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel,', 'Pieter', ''), ('Brueghel', 'Pieter...', '')
        ) == 'punctuation'
        assert Synoname(ret_name=True).sim_type(
            ('Seu rat', 'George Pierre', ''),
            ('Seu-rat', 'George-Pierre', ''),
        ) == 'punctuation'
        assert Synoname(ret_name=True).sim_type(
            ('Picasso', '', ''), ('Picasso', 'Pablo', '')
        ) == 'no_first'
        assert Synoname(ret_name=True).sim_type(
            ('Pereira', 'I. R.', ''), ('Pereira', 'Irene Rice', '')
        ) == 'initials'
        assert Synoname(ret_name=True).sim_type(
            ('Pereira', 'I.', ''), ('Pereira', 'Irene Rice', '')
        ) == 'initials'
        assert Synoname(ret_name=True).sim_type(
            ('Pereira', 'I. R.', ''), ('Pereira', 'I. Smith', '')
        ) != 'initials'
        assert Synoname(ret_name=True).sim_type(
            ('Pereira', 'I. R. S.', ''), ('Pereira', 'I. S. R.', '')
        ) != 'initials'
        assert Synoname(ret_name=True).sim_type(
            ('de Goya', 'Francisco', ''),
            ('de Goya y Lucientes', 'Francisco', ''),
        ) == 'extension'
        assert Synoname(ret_name=True).sim_type(
            ('Seurat', 'George', ''), ('Seurat', 'George-Pierre', '')
        ) == 'extension'
        assert Synoname(ret_name=True).sim_type(
            ('Gericault', 'Theodore', ''),
            ('Gericault', 'Jean Louis Andre Theodore', ''),
        ) == 'inclusion'
        assert Synoname(ret_name=True).sim_type(
            ('Dore', 'Gustave', ''),
            ('Dore', 'Paul Gustave Louis Christophe', ''),
        ) == 'inclusion'

        assert Synoname(ret_name=True).sim_type(
            ('Rosetti', 'Dante Gabriel', ''),
            ('Rosetti', 'Gabriel Charles Dante', ''),
        ) == 'word_approx'
        assert Synoname(ret_name=True).sim_type(
            ('di Domenico di Bonaventura', 'Cosimo', ''),
            ('di Tomme di Nuto', 'Luca', ''),
        ) == 'no_match'
        assert Synoname(ret_name=True).sim_type(
            ('Pereira', 'I. R.', ''), ('Pereira', 'I. Smith', '')
        ) == 'word_approx'
        assert Synoname(ret_name=True).sim_type(
            ('Antonello da Messina', '', ''),
            ('Messina', 'Antonello da', ''),
        ) == 'confusions'
        assert Synoname(ret_name=True).sim_type(
            ('Brueghel', 'Pietter', ''), ('Bruegghel', 'Pieter', '')
        ) == 'char_approx'

    def test_synoname_dist_abs(self):
        """Test abydos.distance.Synoname.dist_abs."""
        # Base cases
        assert self.cmp.dist_abs('', '') == 1
        assert Synoname(tests=['exact']).dist_abs('', '') == 1
        assert Synoname(tests=[]).dist_abs('', '') == 13
        assert Synoname(tests=['nonsense-test']).dist_abs('', '') == 13

        # Test input formats
        assert self.cmp.dist_abs(
            ('Brueghel II (the Younger)', 'Pieter', 'Workshop of'),
            ('Brueghel II (the Younger)', 'Pieter', 'Workshop of'),
        ) == 1
        assert self.cmp.dist_abs(
            'Brueghel II (the Younger)#Pieter#' + 'Workshop of',
            'Brueghel II (the Younger)#Pieter#' + 'Workshop of',
        ) == 1
        assert self.cmp.dist_abs(
            '22#Brueghel II (the Younger)#Pieter#' + 'Workshop of',
            '44#Brueghel II (the Younger)#Pieter#' + 'Workshop of',
        ) == 1

        # approx_c tests
        assert self.cmp.dist_abs(
            (
                'Master of Brueghel II (the Younger)',
                'Pieter',
                'Workshop of',
            ),
            ('Brueghel I (the Elder)', 'Pieter', 'Workshop of'),
        ) == 13
        assert self.cmp.dist_abs(
            ('Master of Brueghel II', 'Pieter', 'Workshop of'),
            ('Master known as the Brueghel II', 'Pieter', 'Workshop of'),
        ) == 10

    def test_synoname_dist(self):
        """Test abydos.distance.Synoname.dist."""
        # Base cases
        assert self.cmp.dist('', '') == pytest.approx(abs=1e-7, expected=1 / 14)
        assert self.cmp.dist(
            '22#Brueghel II (the Younger)#Pieter#' + 'Workshop of',
            '44#Brueghel II (the Younger)#Pieter#' + 'Workshop of',
        ) == pytest.approx(abs=1e-7, expected=1 / 14)
        assert self.cmp.dist(
            (
                'Master of Brueghel II (the Younger)',
                'Pieter',
                'Workshop of',
            ),
            ('Brueghel I (the Elder)', 'Pieter', 'Workshop of'),
        ) == pytest.approx(abs=1e-7, expected=13 / 14)
        assert self.cmp.dist(
            ('Master of Brueghel II', 'Pieter', 'Workshop of'),
            ('Master known as the Brueghel II', 'Pieter', 'Workshop of'),
        ) == pytest.approx(abs=1e-7, expected=10 / 14)

    def test_synoname_sim(self):
        """Test abydos.distance.Synoname.sim."""
        # Base cases
        assert self.cmp.sim('', '') == pytest.approx(abs=1e-7, expected=13 / 14)
        assert self.cmp.sim(
            '22#Brueghel II (the Younger)#Pieter#' + 'Workshop of',
            '44#Brueghel II (the Younger)#Pieter#' + 'Workshop of',
        ) == pytest.approx(abs=1e-7, expected=13 / 14)
        assert self.cmp.sim(
            (
                'Master of Brueghel II (the Younger)',
                'Pieter',
                'Workshop of',
            ),
            ('Brueghel I (the Elder)', 'Pieter', 'Workshop of'),
        ) == pytest.approx(abs=1e-7, expected=1 / 14)
        assert self.cmp.sim(
            ('Master of Brueghel II', 'Pieter', 'Workshop of'),
            ('Master known as the Brueghel II', 'Pieter', 'Workshop of'),
        ) == pytest.approx(abs=1e-7, expected=4 / 14)
