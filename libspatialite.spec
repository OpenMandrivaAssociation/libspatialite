Name: libspatialite
Version: 3.0.1
Release: 1
Summary: SpatiaLite extension enables SQLite to support spatial data 
Group: System/Libraries
License: MPL
URL: http://www.gaia-gis.it
Source0: %{name}-%{version}.tar.gz
Patch0: libspatialite-3.0.1-mdv-linking.patch
BuildRequires: sqlite3-devel
BuildRequires: geos-devel
BuildRequires: proj-devel >= 4.5
BuildRequires: freexl-devel

%description
Core package.

#------------------------------------------------------------------------------

%define major 2
%define libname %mklibname spatialite %{major}

%package -n	%{libname}
Summary: SpatiaLite extension enables SQLite to support spatial data
Group: System/Libraries

%description -n	%{libname}
The SpatiaLite extension enables SQLite to support spatial data too [aka
GEOMETRY], in a way conformant to OpenGis specifications supports standard
WKT and WKB formats: 
- implements SQL spatial functions such as AsText(), GeomFromText(), Area(),
PointN() and alike
- the complete set of OpenGis functions is supported via GEOS, this
comprehending sophisticated spatial analysis functions such as Overlaps(),
Touches(), Union(), Buffer() ..
- supports full Spatial metadata along the OpenGis specifications
- supports importing and exporting from / to shapefiles
- supports coordinate reprojection via PROJ.4 and EPSG geodetic parameters
dataset
- supports locale charsets via GNU libiconv
- implements a true Spatial Index based on the SQLite's RTree extension

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libspatialite.so.%{major}*

#------------------------------------------------------------------------------

%define develname %mklibname -d spatialite

%package -n	%{develname}
Summary: Devel files for spatialite library
Group: Development/C
Provides: %{name}-devel = %{EVRD}
Provides: spatialite-devel =  %{EVRD}
Requires: %{libname} = %{version}

%description -n	%{develname}
Devel files for spatialite library

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
# Create amalgamation 
#make

#cd amalgamation
%configure2_5x \
	--with-proj-include=%_includedir \
	--with-proj-lib=%_libdir \
	--with-geos-include=%_includedir \
	--with-geos-lib=%_libdir \
	--disable-static


%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la
