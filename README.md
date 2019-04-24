**Beets - VT Album Artist**
=========================

This is a plugin for [Beets](https://github.com/beetbox/beets).
It provides a customizable flexible field/tag, vt_albumartist,
which defaults to the track's albumartist. With this tag you'll
be able to group different artists under a same group if your
music player supports custom tags
(e.g.: [MusicBee](https://musicbee.fandom.com/wiki/Custom_Tags)). 

*Plugin only lightly tested by me. Use at your own risk!*


**Install**
===========

To install it, use pip:

    pip install beets-vtalbumartist

or

    git clone https://github.com/rafaelparente/beets-vtalbumartist.git
    cd beets-vtalbumartist
    python setup.py install


**Configuration**
=================

Enable the plugin in beets' config.yaml

    plugins: vtalbumartist

How to use it
-------------

It works primarily as an extra import stage, after Apply-like actions,
which allows the user to Edit the "Virtual Album Artist", saving
this value under the field/tag "vt_albumartist". If not edited,
its value will be the same as the album's artist field/tag (default value)
or some previously set value (current value).

To set or change this field/tag for already imported tracks,
a new command is provided: ``vtalbumartist``. To run it, just type
``beet vtalbumartist QUERY`` where ``QUERY`` matches the tracks to be set.
By default the command will match only albums (and its tracks) which have
at least one track missing the vt_albumartist field/tag for that QUERY.
Additional command-line options include:

* ``--singletons`` or ``-s``: match singleton tracks instead of albums

* ``-reset`` or ``-r``: match even those with field/tag already set

* ``-quiet`` or ``-q``: never prompt for input: set field/tag automatically
  It will try to set the field/tag to a current value, if any,
  or else it will use the default value.

It's compatible with built-in plugins that modify tags, like ``scrub``
and ``mbsync``, as long as the field is still saved on the library.

Therefore, if so needed, you can remove the tag from the files by first
removing the field from the library. For that you can use the default
modify function on beets like it's explained in the
[Docs](https://beets.readthedocs.io/en/stable/reference/cli.html#modify).
For example:

    beet modify vt_albumartist! QUERY

will remove the field for all tracks that match QUERY. Then, to remove
the tag from the file, you can use the built-in plugin ``scrub``:
[Scrub](https://beets.readthedocs.io/en/stable/plugins/scrub.html#manual-scrubbing).
Like so:

    beet scrub QUERY
    
but be aware that it will also remove other tags on the file if
they are not saved on the library's database.