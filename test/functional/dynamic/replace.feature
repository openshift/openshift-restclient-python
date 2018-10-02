Feature: Replace

    Examples:
    | filename                                              | namespace    | update                                                        |
    | definitions/route.openshift.io_v1_Route_test.yaml     | test-replace | definitions/route.openshift.io_v1_Route_test_replace.yaml     |
    | definitions/route.openshift.io_v1_RouteList_test.yaml | test-replace | definitions/route.openshift.io_v1_RouteList_test_replace.yaml |

    Scenario Outline: Replace a resource that does not exist
        Given I have edit permissions in <namespace>
        And The content of <filename> does not exist in <namespace>
        When I try to replace <filename> with <update> in <namespace>
        Then It throws a NotFoundError

    Scenario Outline: Replace a resource that exists
        Given I have edit permissions in <namespace>
        And I have created <filename> in <namespace>
        When I replace <filename> with <update> in <namespace>
        Then The resources in <filename> in <namespace> should match the content of <update>
