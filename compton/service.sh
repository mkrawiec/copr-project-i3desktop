PKG_VERSION=0.1.$(date +%Y%m%d)gitd7f95b

pkg_service_hook()
{
    git clone --depth 1 git://github.com/chjj/compton compton-$PKG_VERSION

    tar -cvzf compton-${PKG_VERSION}.tar.gz compton-$PKG_VERSION
    rm -fr compton-$PKG_VERSION
}

