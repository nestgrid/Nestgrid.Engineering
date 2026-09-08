# Product Repository Samples

> Part of the **[Samples](README.md)**.

## Purpose

This chapter defines how sample projects should be organised and maintained inside a product repository.

## Guidance

Product repositories may include sample projects when they help consumers, contributors, testers or operators understand and validate the product.

Place sample projects under the product repository's `samples/` directory. Keep each sample sufficiently self-contained to explain its purpose without making it part of the product's production source structure.

A sample project should normally include:

- a clear directory name;
- a `README.md` explaining what it demonstrates and how to run it;
- only the dependencies and supporting files needed for its purpose;
- validation instructions or automated validation where practical;
- links to the product documentation, guide or contract it demonstrates.

Samples may demonstrate different concerns, including:

- consuming a library or package;
- calling an API;
- integrating with a product;
- deploying or configuring an application;
- demonstrating a user workflow;
- exercising a protocol or compatibility boundary.

Do not place sample projects under `docs/`. Documentation explaining a sample may live with the sample, while durable consumer guidance belongs under the product's `docs/guides/` directory.

### .NET Sample Projects

Executable .NET sample projects should normally opt out of packaging explicitly:

```xml
<PropertyGroup>
  <IsPackable>false</IsPackable>
</PropertyGroup>
```

This prevents a sample project inheriting a repository-wide packaging default from `Directory.Build.props` and being published unintentionally as a NuGet package.

A sample that intentionally demonstrates package creation or packaging is an exception. That intention should be explicit in its README and project configuration.

### Validation And Maintenance

Samples should build, run or otherwise validate successfully when their purpose makes that practical. If a sample is illustrative rather than executable, state that clearly.

Sample validation should remain proportionate. A small consumer example does not need the full product test suite, but it should not contain known broken instructions or obsolete API usage.

Review samples when product contracts, package versions, configuration, deployment guidance or relevant EOS standards change.

## Key Takeaways

- Sample projects belong under `samples/` in the product repository.
- Each sample should explain its purpose and how to use it.
- Sample projects should remain separate from production source structure.
- Executable .NET samples should set `IsPackable` to `false` unless package creation is intentional.
- Samples should be validated and maintained in proportion to their purpose.
- Sample documentation should link to the product guidance it demonstrates.

## Related Reading

- [01 Sample Purpose](01%20Sample%20Purpose.md)
- [03 Sample Quality](03%20Sample%20Quality.md)
- [04 Sample Maintenance](04%20Sample%20Maintenance.md)
- [Repository Structure](../07%20Solution%20Structure/01%20Repository%20Structure.md)
- [API Usage Guides](../12%20Documentation/06%20API%20Usage%20Guides.md)

---

## Navigation

**Previous**

- [04 Sample Maintenance](04%20Sample%20Maintenance.md)

**Next**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Book**

- [Samples](README.md)

**Engineering Lifecycle**

- [Engineering Lifecycle](../../ENGINEERING-LIFECYCLE.md)

**Repository**

- [Nestgrid Engineering Operating System](../../README.md)
