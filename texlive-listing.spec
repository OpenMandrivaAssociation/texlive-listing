# revision 17373
# category Package
# catalog-ctan /macros/latex/contrib/listing
# catalog-date 2010-03-09 13:13:30 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-listing
Version:	1.2
Release:	1
Summary:	Produce formatted program listings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listing.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The listing environment is provided and is similar to figure
and table, although it is not a floating environment. Includes
support for \caption, \label, \ref, and introduces
\listoflistings, \listingname, \listlistingname. It produces a
.lol file. It does not change \@makecaption (unless the option
bigcaptions is used), so packages that change the layout of
\caption still work.

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
%{_texmfdistdir}/tex/latex/listing/listing.sty
%doc %{_texmfdistdir}/doc/latex/listing/listing.pdf
%doc %{_texmfdistdir}/doc/latex/listing/listing.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
