# Add Apply to Python Client

## Problem
   Current merge/patch strategy in the Ansible modules is not sufficient for a variety of reasons.
   1. There is no way to remove a field from the Ansible module without doing a full replace on the object
   2. The idempotence of the module is entirely reliant on the idempotence of the server. If a task to create a resource is run twice, two `GET`s and
   two `PATCH`es will be issued, even if there was no content change. This is particularly an issue for the
   Operater use-case, as tasks will be run repeatedly every 8 seconds or so, and the `PATCH` requests are not
   cacheable.
   3. There are several core resources that a blind, full-object patch does not work well with, including Deployments
   or any resource that has a `ports` field, as the default merge strategy of `strategic-merge-patch` is bugged
   on the server for those resources.
   4. The `strategic-merge-patch` also does not work at all for CustomResources, requiring the user to add a directive to use a different patch strategy for CustomResource operations.


## Proposal
   Mimic the logic from `kubectl apply` to allow more intelligent patch strategies in the client. This implementation would be a stop-gap, as `apply` is slated to move to the server at some undefined point in the future, at which point we would probably just use the server-side apply.

   `kubectl apply` makes use of a fairly complex 3-way diffing algorithm to generate a patch that performs deletions between the new configuration and the `LastAppliedConfiguration` (stored in the `kubectl.kubernetes.io/last-applied-configuration` annotation), while preserving non-conflicting additions to the real state of the object (ie, system defaulting or manual changes made to pieces of the spec).

   This algorithm is fairly well-documented and cleanly written, but has a large number of edge cases and a fairly high branching factor.

   The basic algorithm is as follows:

   Given: a desired definition for an object to apply to the cluster

   1. `GET` the current state of the object from Kubernetes
   2. Pull the `LastAppliedConfiguration` from the current object
   3. If the `LastAppliedConfiguration` does not exist, diff the desired definition and the current object and send the resulting patch to the server.
   4. Otherwise, diff the `LastAppliedConfiguration` and the desired definition to compute the deletions. 
   5. diff the current object and the desired definition to get the delta
   6. Combine the deletions (from step 4) and the delta (from step 5) to a single patch
   7. If the patch is not empty, send it to the server

   Much of the complexity comes from diffing complex nested objects, and a variety of patch strategies that may be used (ie, adding vs replacing lists, reordering of lists or keys, deep vs shallow object comparisons)

   Resources for golang implementation:
   - https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#kubectl-apply
   - https://github.com/kubernetes/kubernetes/blob/master/pkg/kubectl/cmd/apply/apply.go
   - https://github.com/kubernetes/kubernetes/blob/master/pkg/kubectl/apply.go
   - https://github.com/kubernetes/apimachinery/blob/master/pkg/util/strategicpatch/patch.go#L2011



## Estimates
  Based on a cursory exploration of the golang implementation of `apply`:

  - Up to 1 week for a basic prototype implementation, that can handle the majority of definitions
  - 1 week to test/harden against edge cases
  - 1 week to update and test the Ansible modules. This week may overlap with the hardening/testing period, since the process of integration will likely reveal many common edge-cases

  Total: 2-3 weeks. I would be surprised if it took any more time than that for a working implementation.
