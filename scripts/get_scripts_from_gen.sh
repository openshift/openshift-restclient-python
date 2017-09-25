#!/usr/bin/bash

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
TEMP_FOLDER=$(mktemp -d)
trap "rm -rf ${TEMP_FOLDER}" EXIT SIGINT

if [[ -z ${GEN_ROOT:-} ]]; then
    GEN_ROOT="${TEMP_FOLDER}/gen"
    echo ">>> Cloning gen repo"
    git clone --recursive https://github.com/kubernetes-client/gen.git "${GEN_ROOT}"
else
    echo ">>> Reusing gen repo at ${GEN_ROOT}"
    cur_dir=`pwd`
    cd ${GEN_ROOT}
    git checkout openapi/
    cd ${cur_dir}
fi


echo "--- patching gen repo for openshift compatibility"
sed -i'' "s|{output_dir}:/output_dir|{output_dir}:/output_dir:Z|g" ${GEN_ROOT}/openapi/client-generator.sh
sed -i'' "s/kubernetes.client/${PACKAGE_NAME}.client/g" ${GEN_ROOT}/openapi/python.sh
echo 'chown -R 1000:0 ${output_dir}' >> ${GEN_ROOT}/openapi/generate_client_in_container.sh

head -n -2 ${GEN_ROOT}/openapi/preprocess_spec.py > ${GEN_ROOT}/openapi/preprocess_spec_tmp.py
mv ${GEN_ROOT}/openapi/preprocess_spec_tmp.py ${GEN_ROOT}/openapi/preprocess_spec.py
# sed -i'' "s/for t in operation\['tags'\]:/for t in operation.get('tags', []):/" ${GEN_ROOT}/openapi/preprocess_spec.py
sed -i'' "s/def remove_model_prefixes(spec):/def remove_model_prefixes(spec, pattern):/" ${GEN_ROOT}/openapi/preprocess_spec.py
sed -i'' "s/remove_model_prefixes(spec)/remove_model_prefixes(spec, 'io.k8s')/" ${GEN_ROOT}/openapi/preprocess_spec.py
sed -i'' "s/\"io\.k8s\"/pattern/" ${GEN_ROOT}/openapi/preprocess_spec.py
cat ${SCRIPT_ROOT}/preprocess_spec.py.stub >> ${GEN_ROOT}/openapi/preprocess_spec.py

sed -i'' "s/io.kubernetes/com.openshift/g" ${GEN_ROOT}/openapi/python.xml
sed -i'' "s/client-python/openshift-restclient-python/g" ${GEN_ROOT}/openapi/python.xml
sed -i'' "s/kubernetes.io/openshift.redhat.com/g" ${GEN_ROOT}/openapi/python.xml
sed -i'' "s/kubernetes-incubator/openshift/g" ${GEN_ROOT}/openapi/python.xml

sed -i'' "s/pip install urllib3.*/pip install urllib3 kubernetes python-string-utils/" ${GEN_ROOT}/openapi/Dockerfile

echo "Copying all modified files"
for file in client-generator.sh python.sh preprocess_spec.py python.xml Dockerfile generate_client_in_container.sh custom_objects_spec.json ; do
  cp ${GEN_ROOT}/openapi/${file} ${SCRIPT_ROOT}/from_gen/${file}
done
