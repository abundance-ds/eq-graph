# Development

Maintenance notes for working on the Gradle build itself.
From time to time it is worth updating the build tooling and the dependencies.
For what the backend is and how to run it, see the [README](README.md#the-backend).

## Update the gradlew wrapper

```shell
./gradlew wrapper --gradle-version latest --distribution-type bin
```

## Update all the dependencies to the latest versions

All the Gradle dependencies are managed by the [libs.versions.toml](gradle/libs.versions.toml) file in the `gradle` dir.

To resolve the latest versions, and apply them automatically to [libs.versions.toml](gradle/libs.versions.toml), run the [version-catalog-update](https://github.com/littlerobots/version-catalog-update-plugin) plugin:

```shell
./gradlew versionCatalogUpdate
```

To review and pick the updates one by one instead of applying them all,
use the interactive mode:

```shell
./gradlew versionCatalogUpdate --interactive
```

which writes the proposed changes to `gradle/libs.versions.updates.toml` for editing,
and then apply the staged changes with:

```shell
./gradlew versionCatalogApplyUpdates
```

> [!NOTE]
> The plugin is configured in [build.gradle.kts](build.gradle.kts)
> to preserve the manual ordering of `libs.versions.toml` (`sortByKey = false`),
> and to keep the `kotlinTarget` and `javaTarget` version constants,
> which have no `version.ref` and would otherwise be removed as unused.
> It selects stable versions by default, so alpha, beta and release-candidate builds are not proposed —
> this replaces the hand-written rejection rule the old `com.github.ben-manes.versions` plugin needed.

Bumping the Kotlin version means bumping `kotlinTarget` as well if the language level should follow;
the build compiles with `extraWarnings` and `progressiveMode` enabled, so a Kotlin upgrade can surface new warnings that were not there before.

## Conventions

The build applies [xemantic-conventions](https://github.com/xemantic/xemantic-conventions) through the `xemantic { }` block,
which supplies the JAR manifest attributes and the AX-oriented test reporting —
failing tests are printed as a `<test-failure>` block carrying the assertion message, the captured output and the stack trace,
and passing tests stay silent.
Do not reintroduce those by hand in [build.gradle.kts](build.gradle.kts).
