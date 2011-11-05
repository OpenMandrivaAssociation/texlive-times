# revision 21993
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2011-03-01 21:42:17 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-times
Version:	20110301
Release:	1
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/times.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

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
%{_texmfdistdir}/dvips/times/config.utm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmbi8a.afm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/times/ptmri8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/nntb8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/nntbi8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/nntr8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/nntri8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/ntnb8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/ntnbi8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/ntnr8a.afm
%{_texmfdistdir}/fonts/afm/ibm/times/ntnri8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmb8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmbi8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmr8a.afm
%{_texmfdistdir}/fonts/afm/urw/times/utmri8a.afm
%{_texmfdistdir}/fonts/map/dvips/times/utm.map
%{_texmfdistdir}/fonts/tfm/adobe/times/psyro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbi8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmri8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmro8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrr8re.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrre.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/ptmrrn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zpsycmrv.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7m.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7v.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcm7y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcmr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zptmcmrm.tfm
%{_texmfdistdir}/fonts/tfm/adobe/times/zpzccmry.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmb.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmb8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmbi.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmbi8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmr.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmr8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmri.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/ctmri8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trb10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trb2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trb6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trb7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trb8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trb9t.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/tri10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/tri2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/tri6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/tri7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/tri8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/tri9t.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trj10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trj2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trj6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trj7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trj8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trj9t.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trr10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trr2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trr6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trr7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trr8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/times/trr9t.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/ptmb8z.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/ptmbc8z.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/ptmbi8z.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/ptmr8z.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/ptmrc8z.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/ptmri8z.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmb.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmbi.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmbo.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmr.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmri.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmro.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmrre.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/times/rptmrrn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/times/utmro8t.tfm
%{_texmfdistdir}/fonts/type1/urw/times/utmb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmb8a.pfm
%{_texmfdistdir}/fonts/type1/urw/times/utmbi8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmbi8a.pfm
%{_texmfdistdir}/fonts/type1/urw/times/utmr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmr8a.pfm
%{_texmfdistdir}/fonts/type1/urw/times/utmri8a.pfb
%{_texmfdistdir}/fonts/type1/urw/times/utmri8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbc.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbi8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrc.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmri8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmro8t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrre.vf
%{_texmfdistdir}/fonts/vf/adobe/times/ptmrrn.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zpsycmrv.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7m.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7t.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7v.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcm7y.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcmr.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zptmcmrm.vf
%{_texmfdistdir}/fonts/vf/adobe/times/zpzccmry.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmb.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmb8t.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmbi.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmbi8t.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmr.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmr8t.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmri.vf
%{_texmfdistdir}/fonts/vf/cg/times/ctmri8t.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/times/ptmb8z.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/times/ptmbc8z.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/times/ptmbi8z.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/times/ptmr8z.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/times/ptmrc8z.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/times/ptmri8z.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/times/utmro8t.vf
%{_texmfdistdir}/tex/latex/times/8rutm.fd
%{_texmfdistdir}/tex/latex/times/omlutm.fd
%{_texmfdistdir}/tex/latex/times/omsutm.fd
%{_texmfdistdir}/tex/latex/times/ot1utm.fd
%{_texmfdistdir}/tex/latex/times/t1utm.fd
%{_texmfdistdir}/tex/latex/times/ts1utm.fd
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
