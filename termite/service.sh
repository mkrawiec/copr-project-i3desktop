PKG_VERSION=11

pkg_service_hook()
{
    git clone -b v$PKG_VERSION --depth 1 --recursive \
        https://github.com/thestinger/termite.git \
        termite-$PKG_VERSION

    tar -cvzf termite-${PKG_VERSION}.tar.gz termite-$PKG_VERSION
    rm -fr termite-$PKG_VERSION
}

pkg_prebuild_hook()
{
    sudo dnf -y copr enable mkrawiec/i3desktop
}
