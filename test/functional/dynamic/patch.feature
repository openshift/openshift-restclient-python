Feature: Patch

    Examples:
    | filename                         | namespace   | update                                 |
    | definitions/v1_Pod_test.yaml     | test-patch  | definitions/v1_Pod_test_patch.yaml     |
    | definitions/v1_PodList_test.yaml | test-patch2 | definitions/v1_PodList_test_patch.yaml |
    | definitions/v1_List_test.yaml    | test-patch  | definitions/v1_List_test_replace.yaml  |

    Scenario Outline: Patch a resource that does not exist
        Given I have edit permissions in <namespace>
        And The content of <filename> does not exist in <namespace>
        When I try to patch <filename> with <update> in <namespace>
        Then It throws a NotFoundError

    Scenario Outline: Patch a resource that exists
        Given I have edit permissions in <namespace>
        And I have created <filename> in <namespace>
        When I patch <filename> with <update> in <namespace>
        Then The resources in <filename> in <namespace> should match the content of <update>
