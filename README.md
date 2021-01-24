# Extending `JSONField` for Various Databases in Django

Sage Muhammad Abdullah - 1706979455 - Computer Science Universitas Indonesia (2017)

----------

## Abstract

In web development, it is a common practice to use a web framework to build web
applications. One of the most popular web frameworks is Django, a free and
open-source web framework written in Python. Among the wide range of features
in Django, the object-relational mapping (ORM) system is the most complex. The
ORM system in Django maps data models to relational database tables. The data
models are defined as Python classes that have attributes known as model
fields. One of the model fields available in Django is `JSONField` that allows
programmers to store and query semi-structured data using the JSON data format
in a relational database. Before this research, `JSONField` was only available
for the PostgreSQL database system. Meanwhile, Django officially supports
PostgreSQL, MariaDB, MySQL, SQLite, and Oracle Database. This research aimed to
implement a new `JSONField` that is compatible with all database systems
supported by Django. The implementation was created as part of the Google
Summer of Code 2019 program and was merged into the Django codebase for the
release of Django 3.1. In addition to the implementation, this research also
covers some examples of `JSONField` usage with Django's built-in model
validation feature to validate JSON data in a `JSONField`.

## Acknowledgements

See [`pengantar.tex`](pengantar.tex).

## References

See [`references.bib`](references.bib).
