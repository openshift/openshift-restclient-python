from openshift.helper import KubernetesObjectHelper

project_helper = KubernetesObjectHelper('v1', 'project')
print(project_helper.get_object('default'))

service_helper = KubernetesObjectHelper('v1', 'service')
print(service_helper.get_object('router', 'default'))
