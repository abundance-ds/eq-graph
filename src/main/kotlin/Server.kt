/*
 * SPDX-FileCopyrightText: 2026 The eq-graph Authors
 * SPDX-License-Identifier: LicenseRef-Proprietary
 */

package rs.shoulde.eqgraph

import io.github.oshai.kotlinlogging.KotlinLogging
import io.ktor.serialization.kotlinx.json.json
import io.ktor.server.application.Application
import io.ktor.server.application.install
import io.ktor.server.config.property
import io.ktor.server.netty.EngineMain
import io.ktor.server.plugins.contentnegotiation.ContentNegotiation
import io.ktor.server.plugins.di.dependencies
import kotlinx.serialization.json.Json
import org.neo4j.driver.Driver
import org.slf4j.bridge.SLF4JBridgeHandler

// NOTE if this file is renamed, the build.gradle.kts Main-Class attribute has to be adjusted
fun main(args: Array<String>) {
    initializeLogging()
    EngineMain.main(args)
}

fun Application.server() {

    serverContentNegotiation()

    val config = property<Neo4jConfig>("neo4j")

    dependencies {
        provide {
            neo4jDriver(config)
        }
        provide {
            neo4jOperations(
                driver = resolve<Driver>(),
                config = config
            )
        }
    }
    healthCheckApi()
}

fun Application.serverContentNegotiation() {
    // we need to return objects as JSON
    install(ContentNegotiation) {
        json(Json {
            explicitNulls = false
        })
    }
}

val logger = KotlinLogging.logger {}

/**
 * Initializes Java Util Logging to slf4j bridge.
 * This function should be called once, as early as possible during application startup.
 *
 * Note: Neo4j is using JUL internally.
 */
fun initializeLogging() {
    SLF4JBridgeHandler.removeHandlersForRootLogger()
    SLF4JBridgeHandler.install()
}
