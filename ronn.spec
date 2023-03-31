Name:		ronn
Version:	0.7.3
Release:	3
Summary:	Man page generation tool
Source0:	https://rubygems.org/downloads/ronn-%{version}.gem
License:	MIT
BuildRequires:	ruby
BuildRequires:	rubygem-hpricot
BuildRequires:	rubygem-rdiscount
BuildRequires:	rubygem-mustache
Requires:	rubygem-hpricot
Requires:	rubygem-rdiscount
Requires:	rubygem-mustache
BuildArch:	noarch

%description
Ronn builds manuals. It converts simple, human readable textfiles to roff for
terminal display, and also to HTML for the web.

The source format includes all of Markdown but has a more rigid structure
and syntax extensions for features commonly found in manpages (definition
lists, link notation, etc.). The ronn-format(7) manual page defines the
format in detail.

%prep
%setup -q -c -T

%install
%gem_install -d %{buildroot} -n %{SOURCE0}

%files
%{_bindir}/ronn
%{_libdir}/ruby/gems/*/specifications/ronn-%{version}.gemspec
%{_libdir}/ruby/gems/*/cache/ronn-%{version}.gem
%{_libdir}/ruby/gems/*/gems/ronn-%{version}
%doc %{_libdir}/ruby/gems/*/doc
