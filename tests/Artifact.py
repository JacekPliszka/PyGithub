# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Jacek Pliszka (JacekPliszka@github)                           #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import datetime

import github.GithubObject.Artifact

from . import Framework


class ArtifactFile(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.artifactFile = github.GithubObject.ArtifactFile(
            {
                'Content-disposition': 'fdsf; dsfd; filename=correct.txt; fdf'
            },
            b'123'
        )

    def testFilename(self):
        self.assertEqual(self.artifactFile.filename, 'correct.txt')

    def testOutput(self):
        self.assertEqual(self.artifactFile.data, b'123')


class Artifact(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.artifacts = self.g.get_repo("PyGithub/PyGithub").get_artifacts()