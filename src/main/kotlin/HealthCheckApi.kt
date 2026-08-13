/*
 * SPDX-FileCopyrightText: 2026 The eq-graph Authors
 * SPDX-License-Identifier: LicenseRef-Proprietary
 */

package rs.shoulde.eqgraph

import com.xemantic.neo4j.driver.Neo4jOperations
import com.xemantic.neo4j.driver.asInstant
import io.ktor.http.HttpStatusCode
import io.ktor.server.application.Application
import io.ktor.server.plugins.di.dependencies
import io.ktor.server.response.respond
import io.ktor.server.routing.get
import io.ktor.server.routing.routing

fun Application.healthCheckApi() {

    val neo4j: Neo4jOperations by dependencies

    routing {

        get("/health") {
            try {
                val (isHealthy, timestamp) = neo4j.read { tx ->
                    val record = tx.run("RETURN 1 AS check, datetime() AS timestamp").single()
                    val isHealthy = record["check"].asInt() == 1
                    val timestamp = record["timestamp"].asInstant()
                    isHealthy to timestamp
                }
                if (isHealthy) {
                    call.respond(
                        HttpStatusCode.OK,
                        mapOf(
                            "status" to "healthy",
                            "timestamp" to timestamp.toString()
                        )
                    )
                } else {
                    call.respond(
                        HttpStatusCode.ServiceUnavailable,
                        mapOf("status" to "unhealthy")
                    )
                }
            } catch (e: Exception) {
                call.respond(
                    HttpStatusCode.ServiceUnavailable,
                    mapOf(
                        "status" to "unhealthy",
                        "error" to (e.message ?: "Unknown error")
                    )
                )
            }
        }

    }

}