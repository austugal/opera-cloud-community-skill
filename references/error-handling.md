# Error Handling, Status Codes, and Rate Limits

HTTP meanings below are general guidance, not a complete OHIP contract. Exact error bodies, rate
limits, retry headers, and behavior vary by endpoint, gateway, release, and integration. The
endpoint's current specification and response are authoritative.

## Read the body, not just the status

An API may return an error body and correlation/request identifier with the HTTP status. Inspect
the response and the endpoint documentation; do not assume every failure has a structured body or
that it is safe to log without redaction.

## HTTP status codes you will see

| Status | Meaning | Typical cause and action |
|--------|---------|--------------------------|
| 200 / 201 | Success | Request completed; confirm the response body and operation contract. |
| 202 | Accepted | Often indicates accepted work, but follow the documented operation lifecycle. |
| 400 | Bad request | Malformed payload or invalid field. Fix the request; do not retry unchanged. |
| 401 | Unauthorized | Check token, client configuration, and the endpoint's authentication requirements. Retry only if safe and the cause is understood. |
| 403 | Forbidden | Authenticated but not permitted (scope, property entitlement, or a control). Check entitlements; do not retry blindly. |
| 404 | Not found | The resource may not exist or may not be visible at that path/context. Verify the documented endpoint and identifier. |
| 405 | Method not allowed | Wrong HTTP verb for the endpoint. |
| 409 | Conflict | A conflict may require a state reread or reconciliation; inspect the operation response. |
| 422 | Unprocessable entity | Often indicates a validation/business-rule rejection; inspect the body if present. |
| 429 | Too many requests | Follow any documented retry delay and throttling guidance. |
| 500 | Server error | Determine whether the operation may have completed before retrying. |
| 503 | Service unavailable | Follow documented retry guidance; protect non-idempotent operations from duplicate effects. |

## Distinguishing retryable from non-retryable

- A status alone does not determine retry safety. For any timeout or server/gateway error, the
  operation may have succeeded even if the response was lost.
- Respect the endpoint's retry guidance. Before retrying a state-changing request, use its
  idempotency support or reconcile state to prevent duplicate effects.
- Correct authentication, entitlement, path, payload, or state problems before retrying unchanged.

## Rate limits

OHIP enforces rate limits. When exceeded, calls return 429. Practical handling:

- Respect documented retry headers or operation-specific guidance where present.
- Use exponential backoff with jitter rather than a fixed immediate retry.
- Smooth bursty workloads (for example a bulk load) into a steady rate rather than firing all calls
  at once.
- For large operations, prefer the asynchronous APIs over many rapid synchronous calls.

### Exponential backoff pattern (concept)

1. On a retryable error, wait an initial delay.
2. Double the delay on each subsequent retry, up to a cap.
3. Add random jitter so many clients do not retry in lockstep.
4. Stop after a maximum number of attempts and surface the failure.

## Common error scenarios

- 401 immediately after working calls: the token expired; refresh and retry once.
- 403 on a specific property only: the integration is not entitled to that property, or a control
  blocks the action.
- 422 on create/modify: a business rule rejected the payload; the body names the rule.
- 429 under load: you are exceeding the rate limit; throttle and back off.
- Async job stuck: you are polling too soon or too often, or the job genuinely failed; read the job
  status body.

## Logging guidance

- Log the status, a sanitized error detail, and a correlation/request identifier if returned and
  permitted by policy.
- Never log tokens, secrets, full authorization headers, or unnecessary guest/payment data.
- Keep sufficient redacted context to diagnose the method, API operation, environment, and property
  scope.

## Authoritative reference

- [Oracle Hospitality Integration Platform documentation](https://docs.oracle.com/en/industries/hospitality/integration-platform/)
