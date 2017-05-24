# pyhtml-invoice - straightforward HTML invoice generator written in Python.

This is a straightforward HTML invoice generator written in Python. One of
the advantages over other methods is that the end-user can redirect the
output of the script using whatever commandline tools preferred.

This could be used as a method of generating email invoices. Perhaps
eventually the CSS file could be incorporated into the script directly
to reduce dependencies.

# Requirements

Specifically, the following packages are required:

* python-3 

# Installation

Dump generate_invoice.py at the location your typical python scripts.

Afterwards, adjust the details and to match your company and client so that
the HTML generated resembles what orders you need to place / deliver.

The generated HTML relies on the relevant CSS file, so it will need to be
included if you want shiny-looking styles.

# Running pyhtml-invoice

Simply execute the script and redirect the contents to the intended
destination (e.g. HTML file or email).

# Authors

This was developed by Robert Bisewski at Ibis Cybernetics. For more
information, contact:

* Website -> www.ibiscybernetics.com

* Email -> contact@ibiscybernetics.com
