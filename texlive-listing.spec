%global tl_name listing
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Produce formatted program listings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listing
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listing.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listing.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The listing environment is provided and is similar to figure and table,
although it is not a floating environment. Includes support for
\caption, \label, \ref, and introduces \listoflistings, \listingname,
\listlistingname. It produces a .lol file. It does not change
\@makecaption (unless the option bigcaptions is used), so packages that
change the layout of \caption still work.

