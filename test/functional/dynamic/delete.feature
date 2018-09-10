Feature: Delete

    Examples:
    | group_version | kind | namespace | name |
    | v1            | Pod  | test      | test |

    Scenario Outline: Delete a resource that exists
        Given I have edit permissions in <namespace>
        And <group_version>.<kind> <name> exists in <namespace>
        When I delete <group_version>.<kind> <name> in <namespace>
        Then <group_version>.<kind> <name> does not exist in <namespace>

    Scenario Outline: Delete a resource that does not exist
        Given I have edit permissions in <namespace>
        And <group_version>.<kind> <name> does not exist in <namespace>
        When I try to delete <group_version>.<kind> <name> in <namespace>
        Then It throws a NotFoundError
