---
layout: documentation
title: ofed
category: documentation
subcategory: 14.6.0/components
menu: 'components.md'
---
### NAME

NCM::ofed - NCM ofed configuration component

### SYNOPSIS

- Configure()

    This component configures OFED.

- `/software/components/ofed/openib`
- config 
Config file loaction for openib (default `/etc/infiniband/openib.conf`).
- options
Config options
- modules
Modules to load
- hardware
Hardware modules to load

### DEPENDENCIES

#### Components to be run before:

none.

#### Components to be run after:

none.

### BUGS

none known.

Stijn De Weirdt &lt;&gt;

### SEE ALSO

ncm-ncd(1), ofed(1)
