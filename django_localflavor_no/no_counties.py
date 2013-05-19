# -*- coding: utf-8 -*-
"""
An alphabetical list of Norwegian counties (fylker) for use as `choices` in a
formfield.

This exists in this standalone file so that it's only imported into memory when
explicitly needed.
"""
from __future__ import unicode_literals

COUNTY_CHOICES = (
    ('akershus', 'Akershus'),
    ('austagder', 'Aust-Agder'),
    ('buskerud', 'Buskerud'),
    ('finnmark', 'Finnmark'),
    ('hedmark', 'Hedmark'),
    ('hordaland', 'Hordaland'),
    ('janmayen', 'Jan Mayen'),
    ('moreogromsdal', 'Møre og Romsdal'),
    ('nordtrondelag', 'Nord-Trøndelag'),
    ('nordland', 'Nordland'),
    ('oppland', 'Oppland'),
    ('oslo', 'Oslo'),
    ('rogaland', 'Rogaland'),
    ('sognogfjordane', 'Sogn og Fjordane'),
    ('svalbard', 'Svalbard'),
    ('sortrondelag', 'Sør-Trøndelag'),
    ('telemark', 'Telemark'),
    ('troms', 'Troms'),
    ('vestagder', 'Vest-Agder'),
    ('vestfold', 'Vestfold'),
    ('ostfold', 'Østfold')
)
