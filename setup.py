#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer - The distributed application framework
# ==============================================
# Copyright (C) 2011-2018 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup, find_packages

setup(name="isomer-wiki",
      version="0.0.2",
      description="isomer-wiki",
      author="Isomer Community",
      author_email="riot@c-base.org",
      url="https://github.com/isomeric/wiki",
      license="GNU Affero General Public License v3",
      packages=find_packages(),
      long_description="""Isomer - Wiki
=============

A modern, opensource approach to wiki management.

This software package is a plugin module for Isomer.
""",
      dependency_links=[],
      install_requires=[
          'isomer>=1.2.0',
          # 'docutils==0.12'
      ],
      entry_points="""[isomer.components]
    wiki=isomer.wiki.wiki:Wiki
[isomer.schemata]
    wikipage=isomer.wiki.wikipage:WikiPage
    wikitemplate=isomer.wiki.wikipage:WikiTemplate
[isomer.provisions]
    wikipages=isomer.wiki.provisions.pages:provision
    wikitemplate=isomer.wiki.provisions.templates:provision
    """,
      test_suite="tests.main.main",
      )
