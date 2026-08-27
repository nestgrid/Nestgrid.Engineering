# API Usage Guide

```yaml
title:
eos_version:
version:
status:
owner:
contributors:
produced_by: Software Engineer
consumed_by: API Consumers, Quality Engineer, Project Sponsor
date:
supersedes:
related_decisions:
related_work_items:
related_repositories:
openapi_reference:
```

## Purpose and Scope

Describe the API, its intended consumers and the workflows covered by this guide.

This guide complements the generated OpenAPI reference. It should explain how to use the API, not duplicate the endpoint contract.

## Prerequisites

Describe required environments, services, accounts, data and configuration.

## Authentication and Context

Describe authentication, authorisation, workspace or tenant context and any required headers or identifiers.

## Workflow Overview

Describe the normal sequence of operations at a business level.

Example:

```text
Create Workspace
  -> Create initial Member
  -> Create Account
  -> Record Transaction
  -> Retrieve Account Summary
```

## Workflow: [Name]

### Purpose

Describe what this workflow achieves.

### Prerequisites

- Prerequisite 1

### Steps

1. Describe the first operation and link to its OpenAPI reference.
2. Describe the next operation and identify any response values required by it.
3. Describe the expected result.

### Example Requests and Responses

Provide concise examples for the important steps. Use representative values and avoid real secrets or sensitive data.

### Failure Scenarios

Describe expected validation, authorisation, conflict, not found and other relevant failures.

## Common Workflows

List the most important supported workflows and link to their detailed sections.

## Error Handling

Explain common response shapes, error identifiers, retry expectations and client handling guidance.

## Development Usage

Describe local configuration, test data and the development OpenAPI or Scalar reference where applicable.

## Version and Compatibility

Describe API versioning, compatibility expectations and breaking-change guidance.

## Related Documentation

- OpenAPI reference:
- Scalar development reference:
- Authentication guidance:
- Deployment Guide:
- Relevant product handbook:
- Relevant decision records:

## Maintenance

Update this guide when workflow order, prerequisites, response identifiers, authorisation, compatibility or failure behaviour changes.

