/*
 * Copyright 2025 Kazimierz Pogoda / Xemantic
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

@file:OptIn(ExperimentalKotlinGradlePluginApi::class)

import org.jetbrains.kotlin.gradle.ExperimentalKotlinGradlePluginApi
import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import org.jetbrains.kotlin.gradle.dsl.KotlinVersion

plugins {
    alias(libs.plugins.kotlin.jvm)
    alias(libs.plugins.kotlin.plugin.power.assert)
    alias(libs.plugins.kotlin.plugin.serialization)
    alias(libs.plugins.version.catalog.update)
    alias(libs.plugins.xemantic.conventions)
}

group = "rs.shoulde.eqgraph"

xemantic {
    description = "A research knowledge graph of the EuroQol Research Foundation's funded projects and the publications they produced"
    inceptionYear = "2026"
    organization = "Shoulders"
    organizationUrl = "https://shoulde.rs"
    gitHubAccount = "shoulders-ai"
    applyAllConventions()
}

val javaTarget = libs.versions.javaTarget.get()
val kotlinTarget = KotlinVersion.fromVersion(libs.versions.kotlinTarget.get())

repositories {
    mavenCentral()
}

kotlin {
    compilerOptions {
        apiVersion = kotlinTarget
        languageVersion = kotlinTarget
        jvmTarget = JvmTarget.fromTarget(javaTarget)
        freeCompilerArgs.addAll(
            "-Xjdk-release=$javaTarget"
        )
        optIn.addAll(
            "kotlin.time.ExperimentalTime"
        )
        extraWarnings = true
        progressiveMode = true
    }
    coreLibrariesVersion = libs.versions.kotlin.get()
}

tasks.withType<JavaCompile>().configureEach {
    options.release = javaTarget.toInt()
}

dependencies {
    implementation(libs.neo4j.driver)
    implementation(libs.xemantic.neo4j.kotlin.driver)
    implementation(libs.neo4j.migrations)

    implementation(libs.ktor.server.core)
    implementation(libs.ktor.server.netty)
    implementation(libs.ktor.server.content.negotiation)
    implementation(libs.ktor.server.config.yaml)
    implementation(libs.ktor.server.di)

    implementation(libs.ktor.client.core)
    implementation(libs.ktor.client.cio)
    implementation(libs.ktor.client.content.negotiation)

    implementation(libs.ktor.serialization.kotlinx.json)
    implementation(libs.ktor.serialization.kotlinx.xml)

    implementation(libs.kotlin.logging)
    implementation(libs.jul.to.slf4j)
    implementation(libs.logback.classic)

    testImplementation(platform(libs.junit.bom))
    testRuntimeOnly(libs.junit.platform.launcher)
    testImplementation(libs.kotlin.test)
    testImplementation(libs.xemantic.kotlin.test)
    testImplementation(libs.ktor.server.test.host)
}

tasks.withType<JavaExec> {
    jvmArgs(
        "--enable-native-access=ALL-UNNAMED",
        "--sun-misc-unsafe-memory-access=allow"
    )
}

tasks.register<Jar>("uberjar") {

    group = "build"
    description = "Creates a fat JAR with all dependencies"

    dependsOn("build")

    archiveClassifier.set("uber")
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE

    // Set the main class for execution
    manifest {
        attributes(
            "Main-Class" to "rs.shoulde.eqgraph.ServerKt"
        )
    }

    // Include compiled classes
    from(sourceSets.main.get().output)

    // Include all dependencies
    dependsOn(configurations.runtimeClasspath)
    from({
        configurations.runtimeClasspath.get().filter {
            it.name.endsWith("jar")
        }.map {
            zipTree(it)
        }
    })
}

powerAssert {
    functions = listOf(
        "kotlin.assert",
        "com.xemantic.kotlin.test.assert",
        "com.xemantic.kotlin.test.have"
    )
}

versionCatalogUpdate {
    // preserve the manual, logically-grouped ordering of libs.versions.toml
    sortByKey = false
    keep {
        // kotlinTarget / javaTarget are plain version constants with no version.ref
        versions = setOf("kotlinTarget", "javaTarget")
        keepUnusedVersions = false
    }
}

tasks.test {

    useJUnitPlatform()

    jvmArgs(
        "--enable-native-access=ALL-UNNAMED",
        "--sun-misc-unsafe-memory-access=allow"
    )

}
