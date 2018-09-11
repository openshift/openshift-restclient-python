Feature: Patch

    Examples:
    | group_version | kind | namespace | name | update     |
    | v1            | Pod  | test      | test | test_patch |

    Scenario Outline: Patch a resource that does not exist
        Given I have edit permissions in <namespace>
        And <group_version>.<kind> <name> does not exist in <namespace>
        When I try to patch <group_version>.<kind> <name> in <namespace> with <update>
        Then It throws a NotFoundError

    Scenario Outline: Patch a resource that exists
        Given I have edit permissions in <namespace>
        And <group_version>.<kind> <name> exists in <namespace>
        When I patch <group_version>.<kind> <name> in <namespace> with <update>
        Then <group_version>.<kind> <name> in <namespace> should match the content of <update>
