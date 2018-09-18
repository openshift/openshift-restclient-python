Feature: Create

    Examples:
    | group_version | kind | namespace | name |
    | v1            | Pod  | test      | test |

    Scenario Outline: Create a resource for the first time
        Given I have edit permissions in <namespace>
        And <group_version>.<kind> <name> does not exist in <namespace>
        When I create <group_version>.<kind> <name> in <namespace>
        Then <group_version>.<kind> <name> exists in <namespace>

    Scenario Outline: Create a resource again
        Given I have edit permissions in <namespace>
        And I have created <group_version>.<kind> <name> in <namespace>
        When I try to create <group_version>.<kind> <name> in <namespace>
        Then It throws a ConflictError
