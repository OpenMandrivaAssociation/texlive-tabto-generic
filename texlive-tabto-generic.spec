# revision 15878
# category Package
# catalog-ctan /macros/generic/misc/tabto.tex
# catalog-date 2009-09-13 19:05:07 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-tabto-generic
Version:	20090913
Release:	1
Summary:	"Tab" to a measured position in the line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/misc/tabto.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-generic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
\tabto{<length>} moves the typesetting position to <length>
from the left margin of the paragraph. If the typesetting
position is already further along, \tabto starts a new line.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tabto-generic/tabto.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
