%global tl_name tabto-generic
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Tab to a measured position in the line
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/tabto.tex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-generic.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
\tabto{<length>} moves the typesetting position to <length> from the
left margin of the paragraph. If the typesetting position is already
further along, \tabto starts a new line.

