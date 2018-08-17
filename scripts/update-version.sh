set -x
SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
SOURCE_ROOT="${SCRIPT_ROOT}/../"
CLIENT_ROOT="${SOURCE_ROOT}/${PACKAGE_NAME}"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
echo "--- updating version information..."
sed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^Version:.*/Version:    ${CLIENT_VERSION}/" "${SCRIPT_ROOT}/../python-openshift.spec"
