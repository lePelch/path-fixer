# Maintainer: Cédrick Pelchat
pkgname=path-fixer-git
_pkgname=path-fixer
pkgver=c5e94a1
pkgrel=1
pkgdesc="Tool for extracting Windows backups to Linux (fixes paths and recreates directory structure)"
arch=("any")
url="https://github.com/lePelch/path-fixer.git"
license=("MIT")

depends=(
  "python"
  "python-typer"
  "python-tqdm"
)
makedepends=(
  "git"
  "python-build"
  "python-installer"
  "python-wheel"
)

provides=("path-fixer")
conflicts=("path-fixer")

source=("git+$url")
sha256sums=("SKIP")

pkgver() {
  cd "$srcdir/$_pkgname"

  # Version auto: <dernier tag>.r<nb_commits>.g<hash>
  # Ex: 0.1.1.r12.gabc1234
  git describe --long --tags --always |
    sed -E 's/^v?//; s/([^-]*-g)/r\1/; s/-/./g'
}

build() {
  cd "$srcdir/$_pkgname"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/$_pkgname"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
