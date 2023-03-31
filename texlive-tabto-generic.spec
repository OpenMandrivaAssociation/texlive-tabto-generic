Name:		texlive-tabto-generic
Version:	15878
Release:	2
Summary:	"Tab" to a measured position in the line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/misc/tabto.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-generic.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
\tabto{<length>} moves the typesetting position to <length>
from the left margin of the paragraph. If the typesetting
position is already further along, \tabto starts a new line.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tabto-generic

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
