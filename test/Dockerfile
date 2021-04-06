FROM registry.access.redhat.com/ubi8/ubi

ENV USER_UID=1001 \
    USER_NAME=openshift-python\
    HOME=/opt/osrcp

RUN yum install -y \
      glibc-langpack-en \
      git \
      make \
      python3 \
      python3-devel \
      python3-pip \
      python3-setuptools \
 && pip3 install --no-cache-dir --upgrade setuptools pip wheel \
 && yum clean all

COPY . /opt/osrcp

WORKDIR /opt/osrcp


RUN pip install -e . && \
    pip install -r test-requirements.txt

RUN echo "${USER_NAME}:x:${USER_UID}:0:${USER_NAME} user:${HOME}:/sbin/nologin" >> /etc/passwd \
 && chown -R "${USER_UID}:0" "${HOME}" \
 && chmod -R ug+rwX "${HOME}" \
 && mkdir /go \
 && chown -R "${USER_UID}:0" /go \
 && chmod -R ug+rwX /go

USER ${USER_UID}
