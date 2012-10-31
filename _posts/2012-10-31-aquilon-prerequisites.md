---
layout: article
title: Aquilon Prerequisites
category: documentation
---

Prerequisites and dependencies for aquilon on an SL6 server - lifted from RAL Aquilon server machine type.

## Prerequisites

	# Apache to store profiles
	include { 'rpms/web_server' };
	
	# PostgreSQL
	'/software/repositories' = add_repositories(list('postgres-91-el6-x86_64'));
	
	variable POSTGRESQL_VERSION = "9.1.3-1PGDG.rhel6";
	
	"/software/packages"=pkg_repl("postgresql91", POSTGRESQL_VERSION, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("postgresql91-libs",POSTGRESQL_VERSION, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("postgresql91-server",POSTGRESQL_VERSION, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("postgresql91-contrib",POSTGRESQL_VERSION, PKG_ARCH_DEFAULT);
	
	# Dependencies of postgresql91-contrib
	"/software/packages"=pkg_repl("uuid");
	
	# Aquilon dependencies - move out in time)
	"/software/packages"=pkg_repl("python-psycopg2", "2.4.4-1.rhel6", PKG_ARCH_DEFAULT); # Use version from postgresql repo
	"/software/packages"=pkg_repl("git");
	"/software/packages"=pkg_repl("git-daemon");
	"/software/packages"=pkg_repl("krb5-workstation");
	"/software/packages"=pkg_repl("knc", "1.6.1-2", PKG_ARCH_DEFAULT); # Kerberised Net Cat
	"/software/packages"=pkg_repl("python-setuptools");
	"/software/packages"=pkg_repl("python-virtualenv", "1.7-1.el6", "noarch"); # From epel
	"/software/packages"=pkg_repl("gcc"); # For compling python modules during installation
	"/software/packages"=pkg_repl("libxml2-devel"); # For compiling lxml during installation
	"/software/packages"=pkg_repl("libxslt-devel"); # For compiling lxml during installation
	"/software/packages"=pkg_repl("make"); # For building stuff (including protocols)
	
	# Webserver dependencies
	"/software/packages"=pkg_repl("dbus");
	"/software/packages"=pkg_repl("libtool-ltdl");
	
	# Subversion so we can move things back and forth with SCDB
	"/software/packages"=pkg_repl("subversion");
	
	# Add pan syntax highlighting for vim
	include { 'site/quattor/vimfiles' };
	
	# Add colordiff for highlighted diffing
	'/software/packages'=pkg_add('colordiff', '1.0.9-3.el6', 'noarch');
	
	
	# Dependencies of subversion
	"/software/packages"=pkg_repl("apr-util");
	"/software/packages"=pkg_repl("pakchois");
	"/software/packages"=pkg_repl("libtasn1");
	"/software/packages"=pkg_repl("neon");
	"/software/packages"=pkg_repl("libproxy-python");
	"/software/packages"=pkg_repl("libproxy-bin");
	"/software/packages"=pkg_repl("libproxy");
	"/software/packages"=pkg_repl("gnutls");
	"/software/packages"=pkg_repl("apr");
	
	# Dependencies of git-daemon
	"/software/packages"=pkg_repl("xinetd");
	
	# Dependencies of libxml2-devel
	"/software/packages"=pkg_repl("zlib-devel");
	
	# Dependencies of libxslt-devel
	"/software/packages"=pkg_repl("libgcrypt-devel");
	"/software/packages"=pkg_repl("libxslt");
	"/software/packages"=pkg_repl("libgpg-error-devel");
	
	# Python VirtualEnv dependencies
	"/software/packages"=pkg_repl("python-devel");
	"/software/packages"=pkg_repl("openssl");
	"/software/packages"=pkg_repl("zlib");
	"/software/packages"=pkg_repl("libselinux");
	"/software/packages"=pkg_repl("expat");
	"/software/packages"=pkg_repl("sqlite");
	"/software/packages"=pkg_repl("readline");
	"/software/packages"=pkg_repl("gdbm");
	"/software/packages"=pkg_repl("krb5-libs");
	"/software/packages"=pkg_repl("keyutils-libs");
	"/software/packages"=pkg_repl("libcom_err");
	"/software/packages"=pkg_repl("db4");
	"/software/packages"=pkg_repl("python-libs");
	"/software/packages"=pkg_repl("python");
	"/software/packages"=pkg_repl("ncurses-libs");
	"/software/packages"=pkg_repl("bzip2-libs");
	"/software/packages"=pkg_repl("libffi");
	
	# gcc dependencies
	"/software/packages"=pkg_repl("cloog-ppl");
	"/software/packages"=pkg_repl("glibc-devel");
	"/software/packages"=pkg_repl("glibc");
	"/software/packages"=pkg_repl("mpfr");
	"/software/packages"=pkg_repl("openssl098e");
	"/software/packages"=pkg_repl("glibc-headers");
	"/software/packages"=pkg_repl("libgomp");
	"/software/packages"=pkg_repl("cpp");
	"/software/packages"=pkg_repl("ppl");
	"/software/packages"=pkg_repl("lm_sensors");
	"/software/packages"=pkg_repl("kernel-headers");
	"/software/packages"=pkg_repl("glibc-common");
	
	# Protocol Buffers
	variable protobuf_version = "2.3.0-7.el6";
	"/software/packages"=pkg_repl("protobuf", protobuf_version, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("protobuf-compiler", protobuf_version, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("protobuf-devel", protobuf_version, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("protobuf-python", protobuf_version, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("protobuf-vim", protobuf_version, PKG_ARCH_DEFAULT);
	"/software/packages"=pkg_repl("pkgconfig");

	# Git dependencies
	"/software/packages"=pkg_repl("perl-Git");
	"/software/packages"=pkg_repl("perl-Error");
	"/software/packages"=pkg_repl("rsync");
	
	#Add packaging-utils for development
	"/software/packages"=pkg_repl("yum");
	"/software/packages"=pkg_repl("yum-autoupdate");
	"/software/packages"=pkg_repl("yum-metadata-parser");
	"/software/packages"=pkg_repl("python-urlgrabber");
	"/software/packages"=pkg_repl("python-lxml");
	"/software/packages"=pkg_repl("m2crypto");
	"/software/packages"=pkg_repl("python-iniparse");
	
	# Directories
	variable AQUILON_ROOT = "/opt/aquilon";
	variable QUATTOR_ROOT = "/var/quattor";
	
	"/software/components/dirperm/paths" = push(
	nlist(
	    "path", AQUILON_ROOT,
	    "owner", "root:root",
	    "perm", "0755",
	    "type", "d",
	  ),
	  nlist(
	    "path", QUATTOR_ROOT,
	    "owner", "root:root",
	    "perm", "0755",
	    "type", "d",
	  ),
	  nlist(
	    "path", QUATTOR_ROOT + "/template-king/",
	    "owner", "root:root",
	    "perm", "0755",
	    "type", "d",
	  ),
	);


