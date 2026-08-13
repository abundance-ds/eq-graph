/*
 * SPDX-FileCopyrightText: 2026 The eq-graph Authors
 * SPDX-License-Identifier: LicenseRef-Proprietary
 */

package rs.shoulde.eqgraph

import com.xemantic.neo4j.driver.Neo4jOperations
import org.intellij.lang.annotations.Language
import org.neo4j.driver.Driver

/**
 * Tests run against a real Neo4j instance addressed by the same environment variables
 * `application.yaml` reads, so a local run and a deployed run resolve the same database.
 *
 * There is no embedded alternative: the schema rests on `IS NODE KEY`, existence and
 * property type constraints, all of which are Enterprise features that Community rejects,
 * and no embedded Enterprise harness is publicly obtainable — `com.neo4j.test:neo4j-harness-enterprise`
 * is customer-only and every Neo4j artifact host it lived on has been retired.
 */
object TestNeo4j {

    init {
        initializeLogging()
    }

    private val config: Neo4jConfig by lazy {
        Neo4jConfig(
            uri = requiredEnv("NEO4J_URI"),
            user = requiredEnv("NEO4J_USER"),
            password = requiredEnv("NEO4J_PASSWORD"),
            maxConcurrentSessions = 90
        )
    }

    /** Deliberately the production factory: connectivity check and migrations included. */
    private val driver: Driver by lazy {
        neo4jDriver(config)
    }

    val operations: Neo4jOperations by lazy {
        neo4jOperations(
            driver = driver,
            config = config
        )
    }

    suspend fun populate(
        @Language("cypher") query: String
    ) {
        operations.populate(query)
    }

}

private fun requiredEnv(
    name: String
): String = checkNotNull(System.getenv(name)) {
    "$name is not set. Tests connect to a real Neo4j instance and read the same " +
        "NEO4J_URI / NEO4J_USER / NEO4J_PASSWORD variables that application.yaml does."
}
