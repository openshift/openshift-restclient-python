Feature: Create

    Examples:
    | filename                         | namespace    |
    | definitions/v1_Pod_test.yaml     | test-create  |
    | definitions/v1_PodList_test.yaml | test-create2 |
    | definitions/v1_List_test.yaml    | test-create  |


    Scenario Outline: Create a resource for the first time
        Given I have edit permissions in <namespace>
        And The content of <filename> does not exist in <namespace>
        When I create <filename> in <namespace>
        Then The content of <filename> exists in <namespace>

    Scenario Outline: Create a resource again
        Given I have edit permissions in <namespace>
        And I have created <filename> in <namespace>
        When I try to create <filename> in <namespace>
        Then It throws a ConflictError
