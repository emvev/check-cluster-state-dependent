#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools  # pylint:disable=F0401

setuptools.setup(
	name='check_cluster_state_dependent',
	version="0.13",
	description='Cluster State dependent Nagios Check Wrapper Plugin',
	author="Cygnus Networks GmbH",
	author_email="info@cygnusnetworks.de",
	scripts=['check_cluster_state_dependent'],
	install_requires=[],
)
