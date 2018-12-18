Feature: Delete

    Examples:
    | filename                         | namespace    |
    | definitions/v1_Pod_test.yaml     | test-delete  |
    | definitions/v1_PodList_test.yaml | test-delete2 |
    | definitions/v1_List_test.yaml    | test-delete  |

    Scenario Outline: Delete a resource that exists
        Given I have edit permissions in <namespace>
        And The content of <filename> exists in <namespace>
        When I delete <filename> in <namespace>
        Then The content of <filename> does not exist in <namespace>

    Scenario Outline: Delete a resource that does not exist
        Given I have edit permissions in <namespace>
        And The content of <filename> does not exist in <namespace>
        When I try to delete <filename> in <namespace>
        Then It throws a NotFoundError
