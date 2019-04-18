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

    git clone https://github.com/rafaelp-dev/beets-vtalbumartist.git
    cd beets-vtalbumartist
    python setup.py install


**Configuration**
=================

Enable the plugin in beets' config.yaml

    plugins: vtalbumartist

How to use it
-------------

It works as an extra import stage, after Apply-like actions,
which allows the user to Edit the "Virtual Album Artist", saving
this value under the field/tag "vt_albumartist". If not edited,
its value will be the same as the album's artist field/tag.

To change this field/tag for already imported tracks (but not set it),
use the modify function on beets like it's explained here in the
[Docs](https://beets.readthedocs.io/en/stable/reference/cli.html#modify).
For example:

    beet modify vt_albumartist='beastie men' artist:'beastie boys'

will change the tag for all tracks whose artist is "beastie boys".

It's compatible with built-in plugins that modify tags, like
``scrub`` and ``mbsync``. Currently, the only way to set this
field/tag for already imported tracks is by using the plugin
[scrub](https://beets.readthedocs.io/en/stable/plugins/scrub.html).
By running it, tracks without this field/tag will be set
with the default value (albumartist).