=====================
django_localflavor_no
=====================

Country-specific Django helpers for Norway.

What's in the Norway localflavor?
=================================

* forms.NOSocialSecurityNumber: A form field that validates input as a
  Norwegian social security number (personnummer_).

* forms.NOZipCodeField: A form field that validates input as a Norwegian zip
  code. Valid codes have four digits.

* forms.NOMunicipalitySelect: A ``Select`` widget that uses a list of Norwegian
  municipalities (fylker) as its choices.

.. _personnummer: http://no.wikipedia.org/wiki/Personnummer

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/
