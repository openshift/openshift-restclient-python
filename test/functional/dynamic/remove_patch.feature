Feature: Remove patch

    Examples:
    | filename                                  | namespace  | update                                          |
    | definitions/v1_DeploymentConfig_test.yaml | test-patch | definitions/v1_DeploymentConfig_test_patch.yaml |

    Scenario Outline: Remove patch a resource that does not exist
        Given I have edit permissions in <namespace>
        And The content of <filename> does not exist in <namespace>
        When I try to patch <filename> with <update> in <namespace>
        Then It throws a NotFoundError

    Scenario Outline: Remove patch a resource that exists
        Given I have edit permissions in <namespace>
        And I have created <filename> in <namespace>
        When I patch <filename> with <update> in <namespace>
        Then The resource in <filename> in <namespace> should no longer contain the content of <update>
