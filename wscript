#! /usr/bin/env python
# encoding: utf-8
# Michel Alexandre Salim, 2012
# based on sample Vala wscript by Jaap Haitsma, 2008

# the following two variables are used by the target "waf dist"
VERSION = '0.0.1'
APPNAME = 'ymp-install'

# these variables are mandatory ('/' are converted automatically)
top = '.'
out = 'build'

def options(opt):
	opt.load('compiler_c')
	opt.load('vala')

def configure(conf):
	conf.load('compiler_c vala')
	conf.check_cfg(package='glib-2.0', uselib_store='GLIB', atleast_version='2.10.0', mandatory=1, args='--cflags --libs')
	conf.check_cfg(package='gtk+-3.0', uselib_store='GTK', atleast_version='3.0.0', mandatory=1, args='--cflags --libs')
	conf.check_cfg(package='libxml-2.0', uselib_store='XML', mandatory=1, args='--cflags --libs')

def build(bld):
	bld.recurse('src')

