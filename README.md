# JSONField for Django-Supported Databases

Sage Abdullah\
Computer Science Universitas Indonesia

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

In addition, this thesis was initialized using
[Template LaTeX Tugas Akhir UI][latex-template] by [@ichlaffterlalu][affan].

## References

See [`references.bib`](references.bib).

## Addendum

This bachelor thesis is far from perfect. There are parts of this thesis that
could be elaborated further and parts that could be more succint. As Django is
still actively developed, there are bugfixes and updates in later Django
versions which modified (or removed) some of the code explored in this thesis.
There are also honest mistakes that I made in some of the code explanations.
If I had more time and creative freedom, I would write this thesis differently.

The following are several things I would like to note.

- Several titles were considered, some of them were:
  - Implementing JSONField for (All|Various) Database(s| Systems) Supported by
    Django
  - Extending JSONField for (All|Various) Databases in Django
  - Implementing Cross-Database JSONField in Django
  - Implementing Multiple Databases Support in Django's JSONField
  - etc.

  One of those is probably better than the final title. It doesn't really
  matter. The content does.
- The explanation regarding SQL `NULL` vs JSON `null` could be made clearer.
  In particular, [this paragraph][null-paragraph].
- Disabling Psycopg 2's automatic JSON decoding (described in section 4.1) is
  no longer done by casting the value to text (using the `select_format()` and
  `json_cast_text_sql` methods). Instead, Django registers a stub `loads()`
  function to Psycopg 2 during the connection initialization as of
  [this change][stub-loads].
- The `KeyTransform.preprocess_lhs()` function no longer has an `lhs_only`
  argument. See [this cleanup PR][cleanup-pr] for more information.
- The `KeyTransformIsNull` lookup is incorrect when used with `True` as the
  `rhs` (`__isnull=True`) on SQLite and Oracle. This was fixed in
  [this patch][isnull-fix].
- The secondary research objective, explained in the fifth chapter, is not
  highly cohesive and probably would be better off as a separate writing (e.g.
  a blog post). The main reason for this is that the chapter was not originally
  planned as part of the thesis. The `JSONField` implementation was mostly done
  as part of Google Summer of Code (GSoC) 2019. That was a year before I
  started writing this thesis and I hadn't even decided to graduate with a
  thesis (it was optional). Hence, my research during GSoC was not conducted
  under the supervision of my advisors. I was asked to include something new so
  that my advisors could supervise the research process, and the fifth chapter
  is the result of that.
- The fifth chapter could probably use a simpler scenario and/or better
  validation examples.
- A benchmark of `JSONField` performance across all the database systems was
  originally going to be a part of the "new addition" to the thesis.
  Unfortunately, I was unable to find (or construct) a proper testbed that
  could be used to benchmark the performance objectively. I also do not like
  the idea of people referring to my benchmark as the "ultimate proof" of
  `JSONField` performance as I do not actually have the professional
  capability to do benchmarks. However, I do think that this could be a fun
  experiment for a casual blog post and not to be taken very seriously.

## See also

The [django-jsonfield-backport][backport] package is a backport of the
`JSONField` implementation as a separate package that can be used with Django
versions prior to 3.1. It retains most of the code and behavior from the
Django codebase. Since it's a standalone package, the code might be easier to
read (as you don't have to dive deep into the Django codebase), while still
using the same essential concepts explained in this thesis.

[latex-template]: https://gitlab.com/ichlaffterlalu/latex-skripsi-ui-2017
[affan]: https://github.com/ichlaffterlalu
[null-paragraph]: https://github.com/laymonage/thesis/blob/f783ae00b86c6edcb0477fb2c12d7783f7cafb1e/bab3.tex#L169-L175
[stub-loads]: https://github.com/django/django/pull/13358/files#diff-56374f35499bd669398d3100ef7fcea371a8e9e38f92dbd3569d75b8cea2ad93
[cleanup-pr]: https://github.com/django/django/pull/13749
[isnull-fix]: https://github.com/django/django/pull/13757
[backport]: https://github.com/laymonage/django-jsonfield-backport
