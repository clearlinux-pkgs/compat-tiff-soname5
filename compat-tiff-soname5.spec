#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
#
Name     : compat-tiff-soname5
Version  : 4.4.0
Release  : 62
URL      : https://gitlab.com/libtiff/libtiff/-/archive/v4.4.0/libtiff-v4.4.0.tar.gz
Source0  : https://gitlab.com/libtiff/libtiff/-/archive/v4.4.0/libtiff-v4.4.0.tar.gz
Summary  : Tag Image File Format (TIFF) library.
Group    : Development/Tools
License  : libtiff
Requires: compat-tiff-soname5-lib = %{version}-%{release}
Requires: compat-tiff-soname5-license = %{version}-%{release}
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains various contributions from libtiff users.

%package lib
Summary: lib components for the compat-tiff-soname5 package.
Group: Libraries
Requires: compat-tiff-soname5-license = %{version}-%{release}

%description lib
lib components for the compat-tiff-soname5 package.


%package lib32
Summary: lib32 components for the compat-tiff-soname5 package.
Group: Default
Requires: compat-tiff-soname5-license = %{version}-%{release}

%description lib32
lib32 components for the compat-tiff-soname5 package.


%package license
Summary: license components for the compat-tiff-soname5 package.
Group: Default

%description license
license components for the compat-tiff-soname5 package.


%prep
%setup -q -n libtiff-v4.4.0
cd %{_builddir}/libtiff-v4.4.0
pushd ..
cp -a libtiff-v4.4.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686764852
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%reconfigure --disable-static --with-docdir=/usr/share/doc/tiff
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --with-docdir=/usr/share/doc/tiff  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1686764852
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-tiff-soname5
cp %{_builddir}/libtiff-v%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/compat-tiff-soname5/a2f64f2a85f5fd34bda8eb713c3aad008adbb589 || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/fax2ps
rm -f %{buildroot}*/usr/bin/fax2tiff
rm -f %{buildroot}*/usr/bin/pal2rgb
rm -f %{buildroot}*/usr/bin/ppm2tiff
rm -f %{buildroot}*/usr/bin/raw2tiff
rm -f %{buildroot}*/usr/bin/tiff2bw
rm -f %{buildroot}*/usr/bin/tiff2pdf
rm -f %{buildroot}*/usr/bin/tiff2ps
rm -f %{buildroot}*/usr/bin/tiff2rgba
rm -f %{buildroot}*/usr/bin/tiffcmp
rm -f %{buildroot}*/usr/bin/tiffcp
rm -f %{buildroot}*/usr/bin/tiffcrop
rm -f %{buildroot}*/usr/bin/tiffdither
rm -f %{buildroot}*/usr/bin/tiffdump
rm -f %{buildroot}*/usr/bin/tiffinfo
rm -f %{buildroot}*/usr/bin/tiffmedian
rm -f %{buildroot}*/usr/bin/tiffset
rm -f %{buildroot}*/usr/bin/tiffsplit
rm -f %{buildroot}*/usr/include/tiff.h
rm -f %{buildroot}*/usr/include/tiffconf.h
rm -f %{buildroot}*/usr/include/tiffio.h
rm -f %{buildroot}*/usr/include/tiffio.hxx
rm -f %{buildroot}*/usr/include/tiffvers.h
rm -f %{buildroot}*/usr/lib32/libtiff.so
rm -f %{buildroot}*/usr/lib32/libtiffxx.so
rm -f %{buildroot}*/usr/lib32/pkgconfig/32libtiff-4.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/libtiff-4.pc
rm -f %{buildroot}*/usr/lib64/libtiff.so
rm -f %{buildroot}*/usr/lib64/libtiffxx.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/libtiff-4.pc
rm -f %{buildroot}*/usr/share/doc/tiff/COPYRIGHT
rm -f %{buildroot}*/usr/share/doc/tiff/ChangeLog
rm -f %{buildroot}*/usr/share/doc/tiff/README.md
rm -f %{buildroot}*/usr/share/doc/tiff/RELEASE-DATE
rm -f %{buildroot}*/usr/share/doc/tiff/TODO
rm -f %{buildroot}*/usr/share/doc/tiff/VERSION
rm -f %{buildroot}*/usr/share/doc/tiff/html/TIFFTechNote2.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/addingtags.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/bugs.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/build.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/contrib.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/document.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/images.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/back.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/bali.jpg
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/cat.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/cover.jpg
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/cramps.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/dave.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/info.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/jello.jpg
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/jim.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/note.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/oxford.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/quad.jpg
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/ring.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/smallliz.jpg
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/strike.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/images/warning.gif
rm -f %{buildroot}*/usr/share/doc/tiff/html/index.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/internals.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/intro.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/libtiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFClose.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFDataWidth.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFError.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFFieldDataType.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFFieldName.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFFieldPassCount.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFFieldReadCount.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFFieldTag.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFFieldWriteCount.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFFlush.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFGetField.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFOpen.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFPrintDirectory.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFRGBAImage.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadDirectory.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadEncodedStrip.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadEncodedTile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadRGBAImage.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadRGBAStrip.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadRGBATile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadRawStrip.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadRawTile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadScanline.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFReadTile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFSetDirectory.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFSetField.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWarning.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWriteDirectory.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWriteEncodedStrip.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWriteEncodedTile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWriteRawStrip.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWriteRawTile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWriteScanline.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFWriteTile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFbuffer.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFcodec.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFcolor.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFmemory.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFquery.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFsize.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFstrip.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFswab.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/TIFFtile.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/fax2ps.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/fax2tiff.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/index.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/libtiff.3tiff.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/pal2rgb.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/ppm2tiff.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/raw2tiff.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiff2bw.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiff2pdf.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiff2ps.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiff2rgba.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffcmp.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffcp.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffcrop.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffdither.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffdump.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffgt.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffinfo.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffmedian.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffset.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/man/tiffsplit.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/misc.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/support.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/tools.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta007.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta016.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta018.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta024.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta028.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta029.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta031.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta032.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta033.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta034.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta035.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.4beta036.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.5.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.5.2.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.5.3.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.5.4.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.5.5.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.5.6-beta.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.5.7.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.6.0.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.6.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.0.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.0alpha.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.0beta.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.0beta2.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.2.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.3.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.7.4.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.8.0.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.8.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.8.2.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.9.0beta.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.9.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v3.9.2.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.0.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.1.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.10.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.2.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.3.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.4.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.4beta.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.5.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.6.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.7.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.8.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.0.9.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.1.0.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.2.0.html
rm -f %{buildroot}*/usr/share/doc/tiff/html/v4.3.0.html
rm -f %{buildroot}*/usr/share/man/man1/fax2ps.1
rm -f %{buildroot}*/usr/share/man/man1/fax2tiff.1
rm -f %{buildroot}*/usr/share/man/man1/pal2rgb.1
rm -f %{buildroot}*/usr/share/man/man1/ppm2tiff.1
rm -f %{buildroot}*/usr/share/man/man1/raw2tiff.1
rm -f %{buildroot}*/usr/share/man/man1/tiff2bw.1
rm -f %{buildroot}*/usr/share/man/man1/tiff2pdf.1
rm -f %{buildroot}*/usr/share/man/man1/tiff2ps.1
rm -f %{buildroot}*/usr/share/man/man1/tiff2rgba.1
rm -f %{buildroot}*/usr/share/man/man1/tiffcmp.1
rm -f %{buildroot}*/usr/share/man/man1/tiffcp.1
rm -f %{buildroot}*/usr/share/man/man1/tiffcrop.1
rm -f %{buildroot}*/usr/share/man/man1/tiffdither.1
rm -f %{buildroot}*/usr/share/man/man1/tiffdump.1
rm -f %{buildroot}*/usr/share/man/man1/tiffgt.1
rm -f %{buildroot}*/usr/share/man/man1/tiffinfo.1
rm -f %{buildroot}*/usr/share/man/man1/tiffmedian.1
rm -f %{buildroot}*/usr/share/man/man1/tiffset.1
rm -f %{buildroot}*/usr/share/man/man1/tiffsplit.1
rm -f %{buildroot}*/usr/share/man/man3/TIFFClose.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFDataWidth.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFError.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFFieldDataType.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFFieldName.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFFieldPassCount.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFFieldReadCount.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFFieldTag.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFFieldWriteCount.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFFlush.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFGetField.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFOpen.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFPrintDirectory.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFRGBAImage.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadDirectory.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadEncodedStrip.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadEncodedTile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadRGBAImage.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadRGBAStrip.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadRGBATile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadRawStrip.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadRawTile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadScanline.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFReadTile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFSetDirectory.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFSetField.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWarning.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWriteDirectory.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWriteEncodedStrip.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWriteEncodedTile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWriteRawStrip.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWriteRawTile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWriteScanline.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFWriteTile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFbuffer.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFcodec.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFcolor.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFmemory.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFquery.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFsize.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFstrip.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFswab.3tiff
rm -f %{buildroot}*/usr/share/man/man3/TIFFtile.3tiff
rm -f %{buildroot}*/usr/share/man/man3/libtiff.3tiff

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtiff.so.5
/usr/lib64/libtiff.so.5.8.0
/usr/lib64/libtiffxx.so.5
/usr/lib64/libtiffxx.so.5.8.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtiff.so.5
/usr/lib32/libtiff.so.5.8.0
/usr/lib32/libtiffxx.so.5
/usr/lib32/libtiffxx.so.5.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-tiff-soname5/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
