# A tiny Makefile :-)
# $Id$

BINDIR=/usr/bin
MANDIR=/usr/share/man
DATADIR=/usr/share

PROGNAME=tskmount
VERSION=0.02


all: docs

docs: docs/man/tskmount.8 docs/html/tskmount.8.html

docs/man/tskmount.8: docs/sgml/tskmount.sgml
	docbook2man --output docs/man docs/sgml/tskmount.sgml

docs/html/tskmount.8.html: docs/sgml/tskmount.sgml
	docbook2html --output docs/html/ docs/sgml/tskmount.sgml
	mv -f docs/html/index.html docs/html/tskmount.8.html

install-all: install install-docs

install: tskmount docs/man/tskmount.8
	install -d $(DESTDIR)$(BINDIR)
	install -d $(DESTDIR)$(MANDIR)/man8
	install -m 0755 tskmount $(DESTDIR)$(BINDIR)/
	install -m 0644 docs/man/tskmount.8 $(DESTDIR)$(MANDIR)/man8/

install-docs: docs/html/tskmount.8.html
	install -d $(DESTDIR)$(DATADIR)/doc/$(PROGNAME)-$(VERSION)
	install -m 0644 README $(DESTDIR)$(DATADIR)/doc/$(PROGNAME)-$(VERSION)/
	install -m 0644 COPYING $(DESTDIR)$(DATADIR)/doc/$(PROGNAME)-$(VERSION)/
	install -m 0644 ChangeLog $(DESTDIR)$(DATADIR)/doc/$(PROGNAME)-$(VERSION)/
	install -m 0644 docs/html/tskmount.8.html $(DESTDIR)$(DATADIR)/doc/$(PROGNAME)-$(VERSION)/

uninstall-all:	uninstall uninstall-docs

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/tskmount
	rm -f $(DESTDIR)$(MANDIR)/man8/tskmount.8

uninstall-docs:
	rm -rf $(DESTDIR)$(DATADIR)/doc/$(PROGNAME)-$(VERSION)

clean:
	rm -f docs/man/tskmount.8 docs/html/tskmount.8.html

