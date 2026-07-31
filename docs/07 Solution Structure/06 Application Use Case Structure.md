# Application Use Case Structure

> Part of the **[Solution Structure](README.md)**.

## Purpose

Application use case structure defines how commands, results and use case handlers should be organised.

It helps application workflows remain discoverable, reviewable and easy to map to API contracts.

## Guidance

Application use cases should be organised by capability and action.

Commands, results and handlers should be discoverable as first-class source artefacts rather than hidden inside broad service files.

### Organise by Capability and Action

Use cases should be grouped by the business capability they support and the action they perform.

Example:

```text
Application/
  UseCases/
    Workspaces/
      CreateWorkspace/
        CreateWorkspaceCommand.cs
        CreateWorkspaceResult.cs
        CreateWorkspaceUseCase.cs
    Funding/
      AllocateFunding/
        AllocateFundingCommand.cs
        AllocateFundingResult.cs
        AllocateFundingUseCase.cs
```

This structure makes workflow ownership visible and keeps related request, response and orchestration code together.

### Avoid Broad Use Case Files

Files such as `WorkspaceUseCases.cs`, `FundingUseCases.cs` or `FundActivityUseCases.cs` become difficult to review once they contain multiple actions.

Small prototypes may colocate commands, results and handlers temporarily.

Production implementation should separate files once a capability has more than one action or is exposed through API contracts.

### Keep One Top-Level Type Per File

Use one top-level class, interface, enum, record or struct per file, including internal types.

This applies to production code, shared test doubles and substantial test fixtures.

Small nested helper types may be used only when they are private implementation details and improve readability.

### Prefer Responsibility-Based Placement

Place files where their responsibility is clearest.

Do not create catch-all files or folders for convenience.

Examples to avoid:

- `Persistence.cs`
- `Extensions.cs`
- `EntityPolicies.cs`
- `Common/`
- `Misc/`
- `Utils/`

Extension methods should live near the responsibility they support.

Dependency injection extensions should live under `Registration` or `DependencyInjection` only when that is their primary responsibility.

## Key Takeaways

- Use cases should be organised by capability and action.
- Commands, results and use cases should be first-class files.
- Broad use case files should not grow into mini modules.
- Use one top-level type per file, including internal types.
- Placement should follow responsibility.

## Related Reading

- [02 Source Structure](02%20Source%20Structure.md)
- [04 Naming and Organisation](04%20Naming%20and%20Organisation.md)
- [Application Response Model](../08%20Engineering%20Standards/07%20Application%20Response%20Model.md)

---

## Navigation

**Previous**

- [05 Configuration and Environments](05%20Configuration%20and%20Environments.md)

**Next**

- [Engineering Standards](../08%20Engineering%20Standards/README.md)

**Book**

- [Solution Structure](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid.Engineering](../../README.md)
