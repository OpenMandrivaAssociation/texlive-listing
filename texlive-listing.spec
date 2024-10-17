Name:		texlive-listing
Version:	17373
Release:	2
Summary:	Produce formatted program listings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listing.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listing.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The listing environment is provided and is similar to figure
and table, although it is not a floating environment. Includes
support for \caption, \label, \ref, and introduces
\listoflistings, \listingname, \listlistingname. It produces a
.lol file. It does not change \@makecaption (unless the option
bigcaptions is used), so packages that change the layout of
\caption still work.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/listing/listing.sty
%doc %{_texmfdistdir}/doc/latex/listing/listing.pdf
%doc %{_texmfdistdir}/doc/latex/listing/listing.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
