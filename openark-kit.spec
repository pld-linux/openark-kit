Summary:	Common utilities for MySQL
Name:		openark-kit
Version:	196
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	https://openarkkit.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	ca76b0de75c1ceb1d14c598e3f720f55
URL:		https://code.google.com/p/openarkkit/
BuildRequires:	python >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	mysql-devel
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-MySQLdb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The openark kit provides common utilities to administer, diagnose and
audit MySQL databases.

The available tools are:
- oak-apply-ri: apply referential integrity on two columns with
  parent-child relationship.
- oak-block-account: block or release MySQL users accounts, disabling
  them or enabling them to login.
- oak-chunk-update: perform long, non-blocking UPDATE/DELETE operation
  in auto managed small chunks.
- oak-get-slave-lag: print slave replication lag and terminate with
  respective exit code.
- oak-hook-general-log: hook up and filter general log entries based
  on entry type or execution plan criteria.
- oak-kill-slow-queries: terminate long running queries.
- oak-modify-charset: change the character set (and collation) of a
  textual column.
- oak-online-alter-table: perform a non-blocking ALTER TABLE
  operation.
- oak-prepare-shutdown: make for a fast and safe MySQL shutdown.
- oak-purge-master-logs: purge master logs, depending on the state of
  replicating slaves.
- oak-repeat-query: repeat query execution until some condition holds.
- oak-security-audit: audit accounts, passwords, privileges and other
  security settings.
- oak-show-limits: show AUTO_INCREMENT "free space".
- oak-show-replication-status: show how far behind are replicating
  slaves on a given master.

%prep
%setup -q

socket=$(mysql_config --socket)
grep -rl /var/run/mysqld/mysql.sock . | xargs sed -i -e "s,/var/run/mysqld/mysql.sock,$socket,"

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_bindir}/oak-apply-ri
%attr(755,root,root) %{_bindir}/oak-block-account
%attr(755,root,root) %{_bindir}/oak-chunk-update
%attr(755,root,root) %{_bindir}/oak-get-slave-lag
%attr(755,root,root) %{_bindir}/oak-hook-general-log
%attr(755,root,root) %{_bindir}/oak-kill-slow-queries
%attr(755,root,root) %{_bindir}/oak-modify-charset
%attr(755,root,root) %{_bindir}/oak-online-alter-table
%attr(755,root,root) %{_bindir}/oak-prepare-shutdown
%attr(755,root,root) %{_bindir}/oak-purge-master-logs
%attr(755,root,root) %{_bindir}/oak-repeat-query
%attr(755,root,root) %{_bindir}/oak-security-audit
%attr(755,root,root) %{_bindir}/oak-show-limits
%attr(755,root,root) %{_bindir}/oak-show-replication-status
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/openark_kit-%{version}-py*.egg-info
%endif
