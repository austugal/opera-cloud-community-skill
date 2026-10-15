# Asynchronous APIs, Business Events, and Streaming

Use the operation-specific OHIP contract as the source of truth. Submission codes, tracking
resources, event payloads, delivery guarantees, acknowledgement behavior, subscription states, and
retry limits are not universal across APIs or releases. The OHIP behaviour recorded below comes
from the OHIP 26.3 release notes (reviewed 2026-10-13). It was not re-checked against later notes.

## When to use asynchronous APIs

Some operations are too large or slow for a synchronous request/response: bulk rate loads, large
reservation or financial extracts, and similar. OPERA Cloud exposes asynchronous variants for these.

### Standard async flow

1. Submit the request to the asynchronous endpoint. The response is an acknowledgement containing a
   location or identifier to track the job, not the result itself.
2. Poll the status resource until the job reports complete (or failed).
3. Retrieve the result from the completion location once ready.

### Async headers and behaviour

- The submit call typically returns quickly with a tracking handle rather than the payload.
- Honour the documented polling interval. Do not tight-loop. Use a sensible interval and back off
  if the job is still running.
- Treat a failed job status as a real failure with a reason in the body; do not assume success on
  timeout.

### Polling best practice

- Start polling after a short initial delay; the job will not be instant.
- Use exponential or fixed sensible intervals; respect rate limits (see `error-handling.md`).
- Set a maximum wait and a clear timeout behaviour rather than polling forever.

## Business Events

Business Events are OPERA's mechanism for notifying external systems that something changed
(a reservation was created, a profile updated, a rate changed). They turn OPERA from a system you
must poll into one that can push change notifications.

### Concepts

- Events are organised by module and event type. A subscription selects which event types it wants.
- Event payload content varies by event and version. Confirm whether it contains sufficient detail
  for processing or whether the consumer must retrieve the entity separately.
- Events can be delivered by streaming (near real time) or consumed by a polling subscription,
  depending on the integration model.

### Event subscription process

1. Define which event types the integration needs (scope to the minimum).
2. Create the subscription in the OHIP portal for the relevant property or properties.
3. The subscription enters an activation lifecycle; it must be active to deliver events.
4. Optionally apply conditions/filters so only events matching criteria are delivered.

### Subscription and stream status

Use the exact lifecycle values and delivery eligibility rules documented for the subscription.
Check both portal status and consumer-side connection/processing health.

### Conditions and filters

Conditions and filters are product/event-specific. Validate their syntax, supported fields, and
interaction in the current portal documentation; do not assume that a filter is available for every
event or that filtering changes the event payload.

## Streaming

Streaming delivers Business Events to a consumer over a persistent connection for near-real-time
processing.

### Connection pattern

- The consumer maintains a persistent connection to the streaming endpoint and receives events as
  they occur, subject to the documented protocol and subscription configuration.
- A dropped connection can delay delivery or create a reconciliation gap. The effect and recovery
  behavior depend on the subscription contract.

### Inactive stream lifecycle (OHIP 26.3)

In the OHIP 26.3 release notes, Oracle documents automatic handling of inactive event streams:

- After 4 days without a successful streaming connection, a warning email is sent to the
  application email address; it warns streaming may be disabled if the consumer does not connect
  within the next 3 days.
- After 7 days without a successful connection, streaming is automatically disabled. The stream
  configuration and allocation are retained, but event processing stops.
- Re-enabling the portal toggle does not reset the inactivity counter. The counter resets only
  after the streaming consumer successfully connects.
- After 30 days of inactivity, the stream is permanently deleted, including its configuration and
  queued events.

This is a release-specific policy; verify it against the current OHIP release notes before acting
on another environment or version. Treat a disabled or deleted stream as a potential event gap and
follow the integration's recovery/reconciliation procedure.

### Connection monitoring

Monitor consumer connectivity and event-processing health. For the OHIP 26.3 inactivity warning
and disable/delete behavior, see **Inactive stream lifecycle (OHIP 26.3)** above. Do not assume that
reconnecting or re-enabling streaming recovers queued events after a stream has been deleted; verify
the applicable release behavior and reconcile downstream state as needed.

### Operational rules

- Design the consumer to be resilient: reconnect on drop and use the documented replay or
  reconciliation mechanism to address a gap.
- A streaming consumer that cannot keep up risks falling behind; size it for peak event volume.
- Keep a fallback reconciliation path (a periodic full read) so a missed event does not cause
  permanent divergence between OPERA and the external system.

## Polling subscription (alternative to streaming)

Where a documented polling subscription is available, it may be an alternative to streaming. Follow
its exact cursor, acknowledgement, retention, and retry semantics; do not assume that polling or
acknowledging prevents redelivery.

## Choosing between them

- Use streaming when low latency matters and the consumer can hold a reliable persistent connection.
- Use polling when the consumer is simpler, runs on a schedule, or cannot maintain a streaming
  connection.
- Unless Oracle explicitly guarantees stronger semantics for the specific interface, design
  consumers to tolerate duplicate, delayed, and out-of-order notifications. Make state-changing
  processing idempotent where possible and reconcile from the system of record.

## Authoritative references

- [OHIP documentation index](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
- [OHIP release notes](https://docs.oracle.com/en/industries/hospitality/integration-platform/axern/c_feature_summary.htm)
- [OPERA Cloud Services documentation](https://docs.oracle.com/en/industries/hospitality/hotels.html)
