Feature: Replace

    Examples:
    | group_version | kind | namespace | name | update       |
    | v1            | Pod  | test      | test | test_replace |

    Scenario Outline: Replace a resource that does not exist
        Given I have edit permissions in <namespace>
        And <group_version>.<kind> <name> does not exist in <namespace>
        When I try to replace <group_version>.<kind> <name> in <namespace> with <update>
        Then It throws a NotFoundError

    Scenario Outline: Replace a resource that exists
        Given I have edit permissions in <namespace>
        And I have created <group_version>.<kind> <name> in <namespace>
        When I replace <group_version>.<kind> <name> in <namespace> with <update>
        Then <group_version>.<kind> <name> in <namespace> should match the content of <update>
