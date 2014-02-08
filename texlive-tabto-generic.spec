# revision 15878
# category Package
# catalog-ctan /macros/generic/misc/tabto.tex
# catalog-date 2009-09-13 19:05:07 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-tabto-generic
Version:	20090913
Release:	3
Summary:	"Tab" to a measured position in the line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/misc/tabto.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-generic.tar.xz
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
%{_texmfdistdir}/tex/generic/tabto-generic/tabto.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090913-2
+ Revision: 756435
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090913-1
+ Revision: 719638
- texlive-tabto-generic
- texlive-tabto-generic
- texlive-tabto-generic

