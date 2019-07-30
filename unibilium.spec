#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unibilium
Version  : 2.0.0
Release  : 2
URL      : https://github.com/mauke/unibilium/archive/v2.0.0.tar.gz
Source0  : https://github.com/mauke/unibilium/archive/v2.0.0.tar.gz
Summary  : A terminfo parsing library
Group    : Development/Tools
License  : LGPL-3.0-only
Requires: unibilium-lib = %{version}-%{release}

%description
Overview
========
Unibilium is a very basic terminfo library. It can read and write
ncurses-style terminfo files, and it can interpret terminfo format strings.
It doesn't depend on curses or any other library. It also doesn't use global
variables, so it should be thread-safe.

%package dev
Summary: dev components for the unibilium package.
Group: Development
Requires: unibilium-lib = %{version}-%{release}
Provides: unibilium-devel = %{version}-%{release}
Requires: unibilium = %{version}-%{release}

%description dev
dev components for the unibilium package.


%package lib
Summary: lib components for the unibilium package.
Group: Libraries

%description lib
lib components for the unibilium package.


%prep
%setup -q -n unibilium-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564500646
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags} PREFIX=/usr LIBDIR=/usr/lib64


%install
export SOURCE_DATE_EPOCH=1564500646
rm -rf %{buildroot}
%make_install PREFIX=/usr LIBDIR=/usr/lib64

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libunibilium.so
/usr/lib64/pkgconfig/unibilium.pc
/usr/share/man/man3/unibi_add_ext_bool.3.gz
/usr/share/man/man3/unibi_add_ext_num.3.gz
/usr/share/man/man3/unibi_add_ext_str.3.gz
/usr/share/man/man3/unibi_count_ext_bool.3.gz
/usr/share/man/man3/unibi_count_ext_num.3.gz
/usr/share/man/man3/unibi_count_ext_str.3.gz
/usr/share/man/man3/unibi_del_ext_bool.3.gz
/usr/share/man/man3/unibi_destroy.3.gz
/usr/share/man/man3/unibi_dummy.3.gz
/usr/share/man/man3/unibi_dump.3.gz
/usr/share/man/man3/unibi_format.3.gz
/usr/share/man/man3/unibi_from_env.3.gz
/usr/share/man/man3/unibi_from_fd.3.gz
/usr/share/man/man3/unibi_from_file.3.gz
/usr/share/man/man3/unibi_from_fp.3.gz
/usr/share/man/man3/unibi_from_mem.3.gz
/usr/share/man/man3/unibi_from_term.3.gz
/usr/share/man/man3/unibi_get_aliases.3.gz
/usr/share/man/man3/unibi_get_bool.3.gz
/usr/share/man/man3/unibi_get_ext_bool.3.gz
/usr/share/man/man3/unibi_get_ext_bool_name.3.gz
/usr/share/man/man3/unibi_get_ext_num.3.gz
/usr/share/man/man3/unibi_get_ext_num_name.3.gz
/usr/share/man/man3/unibi_get_ext_str.3.gz
/usr/share/man/man3/unibi_get_ext_str_name.3.gz
/usr/share/man/man3/unibi_get_name.3.gz
/usr/share/man/man3/unibi_get_num.3.gz
/usr/share/man/man3/unibi_get_str.3.gz
/usr/share/man/man3/unibi_int_from_var.3.gz
/usr/share/man/man3/unibi_name_bool.3.gz
/usr/share/man/man3/unibi_name_num.3.gz
/usr/share/man/man3/unibi_name_str.3.gz
/usr/share/man/man3/unibi_num_from_var.3.gz
/usr/share/man/man3/unibi_run.3.gz
/usr/share/man/man3/unibi_set_aliases.3.gz
/usr/share/man/man3/unibi_set_bool.3.gz
/usr/share/man/man3/unibi_set_ext_bool.3.gz
/usr/share/man/man3/unibi_set_ext_bool_name.3.gz
/usr/share/man/man3/unibi_set_ext_num.3.gz
/usr/share/man/man3/unibi_set_ext_num_name.3.gz
/usr/share/man/man3/unibi_set_ext_str.3.gz
/usr/share/man/man3/unibi_set_ext_str_name.3.gz
/usr/share/man/man3/unibi_set_name.3.gz
/usr/share/man/man3/unibi_set_num.3.gz
/usr/share/man/man3/unibi_set_str.3.gz
/usr/share/man/man3/unibi_short_name_bool.3.gz
/usr/share/man/man3/unibi_short_name_num.3.gz
/usr/share/man/man3/unibi_short_name_str.3.gz
/usr/share/man/man3/unibi_str_from_var.3.gz
/usr/share/man/man3/unibi_terminfo_dirs.3.gz
/usr/share/man/man3/unibi_var_from_num.3.gz
/usr/share/man/man3/unibi_var_from_str.3.gz
/usr/share/man/man3/unibilium.h.3.gz

%files lib
%defattr(-,root,root,-)
/usr/lib64/libunibilium.so.4
/usr/lib64/libunibilium.so.4.0.0
