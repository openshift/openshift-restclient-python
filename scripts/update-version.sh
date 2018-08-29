set -x
SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
SOURCE_ROOT="${SCRIPT_ROOT}/../"
CLIENT_ROOT="${SOURCE_ROOT}/${PACKAGE_NAME}"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
KUBERNETES_CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" KUBERNETES_CLIENT_VERSION)
echo "--- updating version information..."
sed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^Version:.*/Version:    ${CLIENT_VERSION}/" "${SCRIPT_ROOT}/../python-openshift.spec"
sed -i'' "s/^kubernetes ~= .*/kubernetes ~= ${KUBERNETES_CLIENT_VERSION}/" "${SCRIPT_ROOT}/../requirements.txt"
sed -i'' "s/^__k8s_client_version__ = .*/__k8s_client_version__ = \\\"${KUBERNETES_CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^kubernetes .=.*/kubernetes == ${KUBERNETES_CLIENT_VERSION}/" ${SOURCE_ROOT}/requirements.txt
