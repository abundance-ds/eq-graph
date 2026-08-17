"""Curated semantic seed for the 20-paper broader test."""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path


STUDIES = {
    "B01": {
        "title": "Determinants of peripheral nerve block use in joint arthroplasty",
        "eq": "none-reported",
        "purposes": ["health-care use", "health inequality", "comparative clinical outcomes"],
        "designs": ["retrospective administrative-claims cohort"],
        "concepts": ["access inequality", "hospital practice variation", "social deprivation"],
        "instruments": [],
        "methods": ["administrative claims analysis", "population-attributable risk"],
        "models": ["mixed-effects logistic regression"],
        "products": [],
    },
    "B02": {
        "title": "Chichewa PedsQL child and teen adaptation study",
        "eq": "none-reported",
        "purposes": ["translation and cultural adaptation", "measurement-property evaluation"],
        "designs": ["cross-sectional psychometric study", "two-stage cultural adaptation"],
        "concepts": ["child and adolescent health", "cross-cultural comparability", "language adaptation"],
        "instruments": [
            ("PedsQL 4.0 GCS child self-report", "translated and psychometrically evaluated"),
            ("PedsQL 4.0 GCS teen self-report", "translated and psychometrically evaluated"),
        ],
        "methods": ["forward and back translation", "cognitive interview", "psychometric assessment"],
        "models": ["Cronbach alpha", "analysis of variance"],
        "products": [
            ("Chichewa PedsQL child self-report", "instrument language version", "adapted and evaluated"),
            ("Chichewa PedsQL teen self-report", "instrument language version", "adapted and evaluated"),
        ],
    },
    "B03": {
        "title": "EQ-HWB-9 proxy recall and perspective study",
        "eq": "used",
        "purposes": ["content-validity research", "proxy-reporting research"],
        "designs": ["qualitative think-aloud study"],
        "concepts": ["proxy reporting", "dementia", "recall consistency", "caregiver judgement"],
        "instruments": [("EQ-HWB-9 proxy version", "content and response process evaluated")],
        "methods": ["cognitive think-aloud interview", "semi-structured interview"],
        "models": [],
        "products": [("EQ-HWB-9 proxy revision evidence", "instrument-development evidence", "produced")],
    },
    "B04": {
        "title": "COVID-19 EQ-5D systematic review and meta-analysis",
        "eq": "used",
        "purposes": ["evidence synthesis", "population-health burden", "utility evidence"],
        "designs": ["systematic review", "meta-analysis"],
        "concepts": ["COVID-19", "long COVID", "health-state utility", "heterogeneity"],
        "instruments": [
            ("EQ-5D-5L", "evidence synthesized"),
            ("EQ-5D-3L", "evidence synthesized"),
            ("EQ VAS", "evidence synthesized"),
        ],
        "methods": ["systematic review", "meta-analysis", "Newcastle-Ottawa Scale"],
        "models": ["DerSimonian-Laird random-effects model", "Egger regression"],
        "products": [("Pooled COVID-19 EQ-5D estimates", "evidence synthesis", "produced")],
    },
    "B05": {
        "title": "Breast-cancer PROM responsiveness study",
        "eq": "used",
        "purposes": ["measurement-property evaluation", "longitudinal clinical outcomes"],
        "designs": ["single-center longitudinal cohort"],
        "concepts": ["breast cancer", "responsiveness", "minimal clinically important difference"],
        "instruments": [
            ("EQ-5D-5L", "administered and responsiveness evaluated"),
            ("EQ VAS", "administered and responsiveness evaluated"),
            ("EORTC QLQ-C30 version 3.0", "administered and responsiveness evaluated"),
        ],
        "methods": ["longitudinal PROM assessment", "responsiveness assessment"],
        "models": ["paired t-test", "Wilcoxon signed-rank test"],
        "products": [("Breast-cancer PROM responsiveness evidence", "measurement-property evidence", "produced")],
    },
    "B06": {
        "title": "Video versus face-to-face cTTO study",
        "eq": "used",
        "purposes": ["valuation-method research", "administration-mode evaluation", "data-quality research"],
        "designs": ["nonrandomized mode comparison"],
        "concepts": ["remote valuation", "interviewer engagement", "states worse than dead", "digital health"],
        "instruments": [("EQ-5D-Y-3L", "valued")],
        "methods": ["cTTO"],
        "models": ["unequal-variance t-test", "test of proportions"],
        "products": [("Video cTTO feasibility evidence", "valuation-method evidence", "produced")],
    },
    "B07": {
        "title": "Direct versus recalled trauma HRQoL study",
        "eq": "used",
        "purposes": ["recall-method research", "measurement correspondence", "longitudinal clinical outcomes"],
        "designs": ["prospective longitudinal cohort"],
        "concepts": ["recall bias", "response shift", "trauma outcomes"],
        "instruments": [
            ("EQ-5D-3L", "administered for direct and recalled health"),
            ("EQ VAS", "administered for direct and recalled health"),
        ],
        "methods": ["repeated direct and recalled HRQoL assessment"],
        "models": ["intraclass correlation coefficient", "Bland-Altman analysis"],
        "products": [("Retrospective EQ-5D use guidance", "method guidance", "produced")],
    },
    "B08": {
        "title": "Paediatric routine PROM implementation co-design study",
        "eq": "used",
        "purposes": ["implementation research", "content and acceptability evaluation", "co-design input"],
        "designs": ["qualitative semi-structured interview study"],
        "concepts": ["routine PROM implementation", "paediatric care", "co-design", "clinical decision support"],
        "instruments": [
            ("EQ-5D-Y-5L", "shown for implementation evaluation"),
            ("EQ VAS", "shown for implementation evaluation"),
        ],
        "methods": ["semi-structured interview", "qualitative framework analysis"],
        "models": [],
        "products": [("P-PROM ROCK co-design requirements", "implementation evidence", "co-design input produced")],
    },
    "B09": {
        "title": "Experience-scale child-health valuation study",
        "eq": "used",
        "purposes": ["valuation-method research", "value-assessment methods"],
        "designs": ["secondary DCE analysis"],
        "concepts": ["experience scale", "child health valuation", "parent perspective", "no-experience anchor"],
        "instruments": [("EQ-5D-Y-3L", "used in valuation tasks")],
        "methods": ["DCE", "kaizen task", "paired comparison"],
        "models": ["conditional logit model", "cluster bootstrap"],
        "products": [("EQ-5D-Y-3L experience-scale estimates", "experimental preference estimates", "produced; not a QALY value set")],
    },
    "B10": {
        "title": "Child-versus-adult person trade-off protocol",
        "eq": "none-reported",
        "status": "planned",
        "purposes": ["valuation-method research", "social-priority research", "protocol"],
        "designs": ["planned mixed-method person trade-off experiment"],
        "concepts": ["social priority", "child versus adult health gains", "fair innings", "social decision-maker perspective"],
        "instruments": [],
        "methods": ["person trade-off", "think-aloud interview", "focus group"],
        "models": ["planned bootstrap percentile interval"],
        "products": [("Person trade-off study protocol", "research protocol", "published; study outputs planned")],
    },
    "B11": {
        "title": "PROM-enhanced readmission prediction study",
        "eq": "used",
        "purposes": ["clinical prediction", "secondary PROM use", "implementation evidence"],
        "designs": ["population-based retrospective linked-data cohort"],
        "concepts": ["clinical prediction", "routine PROM data", "unplanned readmission"],
        "instruments": [
            ("EQ-5D-5L", "used as prediction input"),
            ("EQ VAS", "used as prediction input"),
            ("VR-12", "used as prediction input"),
        ],
        "methods": ["linked-data clinical prediction"],
        "models": ["Cox landmark supermodel", "multiple imputation by chained equations", "time-dependent Cox model"],
        "products": [("PROM-enhanced readmission prediction models", "prediction model", "internally validated; not implemented")],
    },
    "B12": {
        "title": "Indonesian FACIT-COST validation study",
        "eq": "used",
        "purposes": ["measurement-property evaluation", "translated-instrument validation", "longitudinal clinical outcomes"],
        "designs": ["single-center prospective cohort"],
        "concepts": ["financial toxicity", "cancer outcomes", "Indonesian language", "responsiveness"],
        "instruments": [
            ("FACIT-COST version 2", "psychometrically evaluated"),
            ("EQ-HWB", "administered; results reserved for another report"),
            ("EQ-5D-5L", "administered; results reserved for another report"),
            ("WEMWBS", "administered; results reserved for another report"),
            ("FACT-G", "administered; results reserved for another report"),
        ],
        "methods": ["psychometric assessment"],
        "models": ["principal component analysis", "confirmatory factor analysis", "diagonally weighted least squares", "Gwet AC2"],
        "products": [("Indonesian FACIT-COST validation evidence", "measurement-property evidence", "produced")],
    },
    "B13": {
        "title": "Health-state-value uncertainty framework",
        "eq": "mentioned-only",
        "purposes": ["methodological framework", "reporting guidance", "economic-model input analysis"],
        "designs": ["conceptual methodological synthesis"],
        "concepts": ["statistical uncertainty", "heterogeneity", "methodological variation", "evidence flow"],
        "instruments": [
            ("EQ-5D-3L", "used in methodological example"),
            ("EQ-5D-5L", "discussed"),
            ("SF-6D", "discussed"),
            ("HUI", "discussed"),
        ],
        "methods": ["conceptual uncertainty tracing"],
        "models": ["variance-covariance propagation"],
        "products": [
            ("Health-state-value uncertainty taxonomy", "methodological framework", "produced"),
            ("Health-state-value reporting recommendations", "reporting guidance", "produced"),
        ],
    },
    "B14": {
        "title": "OPUF cognitive-validity study",
        "eq": "used",
        "purposes": ["valuation-method evaluation", "cognitive validity", "online data-quality research"],
        "designs": ["qualitative cognitive-debrief study"],
        "concepts": ["digital preference elicitation", "response-process validity", "anchoring dead"],
        "instruments": [
            ("EQ-HWB-S", "self-reported and valued"),
            ("EQ VAS", "used for warm-up and anchoring familiarization"),
        ],
        "methods": ["Online Personal Utility Functions", "cognitive debrief", "think-aloud interview"],
        "models": [],
        "products": [("OPUF cognitive-validity evidence", "valuation-method evidence", "produced")],
    },
    "B15": {
        "title": "CREATE valuation-study reporting checklist",
        "eq": "mentioned-only",
        "purposes": ["reporting-guideline development", "valuation-method research", "research-quality improvement"],
        "designs": ["modified two-round Delphi process"],
        "concepts": ["reporting quality", "critical appraisal", "value-set methods"],
        "instruments": [
            ("EQ-5D", "subject of reporting guidance"),
            ("SF-6D", "subject of reporting guidance"),
            ("HUI", "subject of reporting guidance"),
            ("AQoL", "subject of reporting guidance"),
        ],
        "methods": ["modified Delphi"],
        "models": [],
        "products": [("CREATE", "reporting checklist", "21-item checklist produced")],
    },
    "B16": {
        "title": "Retracted Egyptian EQ-5D-5L value-set study",
        "eq": "used",
        "purposes": ["value-set development", "valuation study"],
        "designs": ["national cross-sectional valuation survey"],
        "concepts": ["states worse than dead", "interviewer quality control", "Egyptian value set"],
        "instruments": [
            ("EQ-5D-5L", "valued and administered for respondent health"),
            ("EQ VAS", "administered for respondent health"),
        ],
        "methods": ["cTTO", "DCE"],
        "models": ["heteroskedastic interval regression", "conditional logit model", "hybrid model"],
        "products": [("Egyptian EQ-5D-5L value set", "native value set", "retracted; do not use operationally")],
    },
    "B18": {
        "title": "Korean public concepts of health and EQ-5D",
        "eq": "used",
        "purposes": ["content-validity research", "qualitative concept elicitation", "cultural interpretation"],
        "designs": ["qualitative semi-structured interview study"],
        "concepts": ["social relationships", "mental health", "vitality", "cultural adaptation", "dementia"],
        "instruments": [
            ("EQ-5D-5L", "shown for content evaluation"),
            ("EQ VAS", "shown for content evaluation"),
        ],
        "methods": ["semi-structured interview", "directed content analysis"],
        "models": [],
        "products": [("Korean cultural content evidence", "content-validity evidence", "produced")],
    },
    "B19": {
        "title": "Swedish experience-based EQ VAS valuation study",
        "eq": "used",
        "purposes": ["experience-based valuation", "longitudinal outcomes", "patient-versus-population comparison"],
        "designs": ["register-based observational study"],
        "concepts": ["patient values", "experience-based valuation", "mental health", "dead-state anchoring"],
        "instruments": [
            ("EQ-5D-3L", "administered to describe health states"),
            ("EQ VAS", "administered and analyzed as experience-based valuation"),
            ("Swedish experience-based EQ-5D-3L VAS value set", "used for scoring"),
        ],
        "methods": ["secondary registry analysis", "experience-based EQ VAS valuation"],
        "models": ["ordinary least-squares regression", "two-level random-slope and random-intercept model", "Spearman rank correlation"],
        "products": [("Patient experience-based EQ-5D valuation evidence", "valuation evidence", "produced; not anchored at dead")],
    },
    "B20": {
        "title": "Individualized knee-arthroplasty decision-aid usability study",
        "eq": "used",
        "purposes": ["implementation research", "usability evaluation", "clinical decision support"],
        "designs": ["mixed-method usability study"],
        "concepts": ["digital health", "shared decision-making", "personalized outcomes", "digital divide"],
        "instruments": [
            ("EQ-5D", "historical data displayed in decision support"),
            ("Preparation for Decision Making Scale", "administered for usability evaluation"),
            ("System Usability Scale", "administered for usability evaluation"),
            ("Acceptability Scale", "administered for usability evaluation"),
        ],
        "methods": ["decision-aid usability test", "content analysis"],
        "models": [],
        "products": [("Individualized TKA decision aid", "digital decision aid", "usability tested; routine implementation recommended")],
    },
}


PROJECT_LINKS = {
    "B01": ("accepted", "travel grant", "direct article funding statement"),
    "B02": ("accepted", "author-level research grant", "direct author funding statement"),
    "B03": ("accepted", "study funding", "direct article funding statement"),
    "B04": ("accepted", "study funding", "direct article funding statement"),
    "B05": ("candidate", None, "article gives no EuroQol funding statement"),
    "B06": ("accepted", "study funding", "direct article funding statement"),
    "B07": ("accepted", "study funding", "direct article funding statement"),
    "B08": ("accepted", "study funding", "direct article funding statement"),
    "B09": ("accepted", "study and dissertation funding", "direct article funding statement"),
    "B10": ("accepted", "study funding", "JATS funding metadata"),
    "B11": ("accepted", "author-level research grant", "JATS funding metadata"),
    "B12": ("accepted", "data-collection funding", "direct article funding statement"),
    "B13": ("accepted", "study funding", "direct article acknowledgement"),
    "B14": ("accepted", "study funding", "direct article funding statement"),
    "B15": ("accepted", "study support", "direct article funding statement"),
    "B16": ("accepted", "study funding", "direct article funding statement"),
    "B17": ("accepted", "parent-study funding correction", "correction notice"),
    "B18": ("candidate", None, "article and JATS give no EuroQol funding statement"),
    "B19": ("accepted", "study funding", "direct article funding statement"),
    "B20": ("accepted", "study funding", "direct article funding statement"),
}


INSTRUMENT_DETAILS = [
    ("B02", "PedsQL 4.0 GCS child self-report", "Chichewa (Malawi)", None, "child form, ages 8 to 12"),
    ("B02", "PedsQL 4.0 GCS teen self-report", "Chichewa (Malawi)", None, "teen form, ages 13 to 17"),
    ("B03", "EQ-HWB-9 proxy version", "English (Australia)", None, "experimental version 1, 2022"),
    ("B05", "EQ-5D-5L", "Dutch", "Dutch EQ-5D-5L value set", None),
    ("B07", "EQ-5D-3L", "Dutch", "Dutch EQ-5D-3L value set", None),
    ("B12", "FACIT-COST version 2", "Indonesian", None, "official 12-item version"),
    ("B16", "EQ-5D-5L", "Egyptian Arabic", None, "EQ-VT software 2.1"),
    ("B18", "EQ-5D-5L", "Korean", None, None),
    ("B19", "EQ-5D-3L", None, "Swedish experience-based EQ-5D-3L VAS value set", None),
]


ADMINISTRATIONS = [
    ("B02", "PedsQL 4.0 GCS child self-report", "child", "self", "self-completed", "paper", "classroom or clinic", "Chichewa", None, "one assessment", None),
    ("B02", "PedsQL 4.0 GCS teen self-report", "adolescent", "self", "self-completed", "paper", "classroom or clinic", "Chichewa", None, "one assessment", None),
    ("B03", "EQ-HWB-9 proxy version", "carer", "proxy-proxy or proxy-patient", "interviewer-administered think-aloud", "Zoom video", "remote", "English", "seven days", "one interview", "paper copy supplied as reference"),
    ("B05", "EQ-5D-5L", "breast-cancer patient", "self", "self-completed", "web", "Erasmus MC PROM platform", "Dutch", None, "baseline, six months, and 12 months", None),
    ("B06", "EQ-5D-Y-3L", "general-public adult", "adult perspective for a ten-year-old child", "interviewer-administered", "face-to-face", "in person", None, None, "one valuation interview", "interviewer operated EQ-VT"),
    ("B06", "EQ-5D-Y-3L", "general-public adult", "adult perspective for a ten-year-old child", "interviewer-administered", "video", "remote", None, None, "one valuation interview", "Skype or Zoom with screen sharing"),
    ("B07", "EQ-5D-3L", "trauma patient", "current or recalled self", "self-completed", "postal paper", "home", "Dutch", None, "one week, three months, and 12 months", None),
    ("B08", "EQ-5D-Y-5L", "adolescent, caregiver, or clinician", "stakeholder view", "interviewer-administered", "video", "remote", "English", None, "one interview", "instrument shown for discussion"),
    ("B09", "EQ-5D-Y-3L", "parent", "adult perspective for child health", "self-completed", "web", "remote", None, None, "one DCE survey", None),
    ("B10", None, "general-public adult", "social decision maker", "self-completed and interviewer-assisted", "web or interview", "remote", None, None, "planned", "planned protocol"),
    ("B11", "EQ-5D-5L", "recently discharged patient", "self", "self-completed", "web or paper", "after discharge", None, None, "one survey", None),
    ("B12", "FACIT-COST version 2", "cancer patient", "self", "self-completed with assistance available", "paper", "hospital", "Indonesian", None, "baseline and follow-up", "fixed questionnaire order"),
    ("B14", "EQ-HWB-S", "adult", "self and hypothetical health", "self-completed think-aloud", "web with Google Meet", "remote", None, None, "one cognitive interview", "screen sharing"),
    ("B16", "EQ-5D-5L", "Egyptian general-public adult", "self and social", "interviewer-administered", "computer-assisted face-to-face", "in person", "Egyptian Arabic", None, "one valuation interview", "visual aids and interviewer reading available"),
    ("B18", "EQ-5D-5L", "Korean general-public adult", "stakeholder view", "interviewer-administered", "face-to-face", "public room or home", "Korean", None, "one interview", "instrument shown for comment"),
    ("B19", "EQ-5D-3L", "register patient or general-population respondent", "self", "source collection varied", "register or survey", "Sweden", None, None, "baseline and one-year follow-up", "collection mode differed between registers"),
    ("B20", "Preparation for Decision Making Scale", "adult with knee osteoarthritis", "self", "self-completed", "web", "home after clinic screening", "English", None, "after decision-aid use", "Qualtrics"),
]


TIMES = [
    ("B03", "EQ-HWB-9 proxy version", "recall-period", "seven days"),
    ("B05", "EQ-5D-5L", "report-time", "preoperative baseline"),
    ("B05", "EQ-5D-5L", "report-time", "six months after surgery"),
    ("B05", "EQ-5D-5L", "report-time", "12 months after surgery"),
    ("B07", "EQ-5D-3L", "report-time", "one week after injury"),
    ("B07", "EQ-5D-3L", "report-time", "three months after injury"),
    ("B07", "EQ-5D-3L", "report-time", "12 months after injury"),
    ("B07", "EQ-5D-3L", "reference-time", "earlier one-week or three-month health"),
    ("B16", "EQ-5D-5L", "valuation-duration", "ten years in cTTO"),
    ("B19", "EQ-5D-3L", "report-time", "baseline"),
    ("B19", "EQ-5D-3L", "report-time", "one-year follow-up"),
]


DERIVATIONS = [
    ("B04", 1, "reported medians and ranges", "estimate means and standard deviations", "meta-analysis inputs", "conversion uncertainty"),
    ("B04", 2, "study-level EQ-5D inputs", "random-effects pooling", "pooled EQ-5D estimates", "heterogeneity and sampling uncertainty"),
    ("B11", 1, "linked administrative and PROM predictors", "multiple imputation and Cox landmark modeling", "readmission predictions", "imputation and model uncertainty"),
    ("B13", 1, "health-state-value model covariance", "propagate variance through state calculation", "state-value standard error", "model-estimation uncertainty"),
]


def slug(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def section_bullets(text: str, heading: str) -> list[str]:
    match = re.search(
        rf"^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        return []
    bullets: list[str] = []
    current: list[str] = []
    for line in match.group(1).splitlines():
        if line.startswith("- "):
            if current:
                bullets.append(" ".join(current))
            current = [line[2:].strip()]
        elif current and line.startswith("  "):
            current.append(line.strip())
        elif current and not line.strip():
            continue
        elif current:
            bullets.append(" ".join(current))
            current = []
    if current:
        bullets.append(" ".join(current))
    return bullets


def load_semantic(
    connection: sqlite3.Connection,
    repo_root: Path,
    batch_rows: dict[str, dict[str, str]],
) -> None:
    instruments: dict[str, str] = {}
    for record_id, config in STUDIES.items():
        row = batch_rows[record_id]
        publication_id = f"doi:{row['doi'].lower()}"
        record_path = repo_root / "pilot" / "ontology-development-v3" / "broader" / "records" / f"{record_id}.md"
        record_text = record_path.read_text(encoding="utf-8")
        connection.execute(
            "INSERT INTO study "
            "(study_id, publication_id, title, eq_instrument_status, record_path, review_status, execution_status) "
            "VALUES (?, ?, ?, ?, ?, 'source-checked', ?)",
            (
                record_id,
                publication_id,
                config["title"],
                config["eq"],
                str(record_path.relative_to(repo_root)),
                config.get("status", "completed"),
            ),
        )
        connection.execute(
            "INSERT INTO study_publication VALUES (?, ?, 'primary report', ?)",
            (record_id, publication_id, "source-checked extraction record"),
        )
        for kind, labels in (("research-purpose", config["purposes"]), ("study-design", config["designs"])):
            connection.executemany(
                "INSERT INTO study_classification "
                "(study_id, classification_type, preferred_label, source_locator) VALUES (?, ?, ?, ?)",
                [(record_id, kind, label, "extraction record: Identity and study type") for label in labels],
            )
        connection.executemany(
            "INSERT INTO study_concept "
            "(study_id, preferred_label, source_term, review_status, source_locator) "
            "VALUES (?, ?, ?, 'accepted', ?)",
            [(record_id, label, label, "extraction record: Concepts and themes") for label in config["concepts"]],
        )
        population_bullets = section_bullets(record_text, "Population and samples")
        if population_bullets and not population_bullets[0].lower().startswith(
            ("no participant sample", "not applicable")
        ):
            connection.execute(
                "INSERT INTO population (study_id, label, role, source_locator) VALUES (?, ?, 'reported population', ?)",
                (record_id, population_bullets[0], "extraction record: Population and samples"),
            )
        for label, role in config["instruments"]:
            instrument_id = instruments.setdefault(label, slug(label))
            connection.execute(
                "INSERT OR IGNORE INTO instrument (instrument_id, preferred_label) VALUES (?, ?)",
                (instrument_id, label),
            )
            connection.execute(
                "INSERT INTO instrument_use "
                "(study_id, instrument_id, role, source_label, source_locator) VALUES (?, ?, ?, ?, ?)",
                (record_id, instrument_id, role, label, "extraction record: Instruments and administration"),
            )
        for label in config["methods"]:
            connection.execute(
                "INSERT INTO research_method "
                "(study_id, preferred_label, source_label, method_family, role, source_locator) "
                "VALUES (?, ?, ?, 'source-defined', 'research method', ?)",
                (record_id, label, label, "extraction record: Methods, protocol, and task design"),
            )
        for label in config["models"]:
            connection.execute(
                "INSERT INTO statistical_model "
                "(study_id, preferred_label, source_label, role, source_locator) VALUES (?, ?, ?, 'reported', ?)",
                (record_id, label, label, "extraction record: Analysis and statistical models"),
            )
        for label, product_type, status in config["products"]:
            connection.execute(
                "INSERT INTO research_product "
                "(study_id, label, product_type, status, source_locator) VALUES (?, ?, ?, ?, ?)",
                (record_id, label, product_type, status, "extraction record: Products"),
            )
        for sequence, statement in enumerate(
            section_bullets(record_text, "Principal findings and interpretation"), start=1
        ):
            connection.execute(
                "INSERT INTO finding (study_id, sequence, statement, source_locator) VALUES (?, ?, ?, ?)",
                (record_id, sequence, statement, "extraction record: Principal findings and interpretation"),
            )
        for sequence, statement in enumerate(
            section_bullets(record_text, "Limitations and source issues"), start=1
        ):
            connection.execute(
                "INSERT INTO limitation (study_id, sequence, statement, source_locator) VALUES (?, ?, ?, ?)",
                (record_id, sequence, statement, "extraction record: Limitations and source issues"),
            )
        for statement in section_bullets(record_text, "Outcomes or measurement properties"):
            connection.execute(
                "INSERT OR IGNORE INTO study_outcome "
                "(study_id, preferred_label, source_label, source_locator) VALUES (?, ?, ?, ?)",
                (record_id, statement, statement, "extraction record: Outcomes or measurement properties"),
            )

    for study_id, instrument_label, language, scoring_source, details in INSTRUMENT_DETAILS:
        connection.execute(
            "UPDATE instrument_use SET language = ?, scoring_source = ?, details = ? "
            "WHERE study_id = ? AND instrument_id = ?",
            (language, scoring_source, details, study_id, slug(instrument_label)),
        )
    for item in ADMINISTRATIONS:
        study_id, instrument_label, respondent, perspective, interaction, channel, setting, language, recall_period, timepoint, details = item
        connection.execute(
            "INSERT INTO administration "
            "(study_id, instrument_id, respondent, perspective, interaction, channel, setting, language, "
            "recall_period, timepoint, details, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                study_id,
                slug(instrument_label) if instrument_label else None,
                respondent,
                perspective,
                interaction,
                channel,
                setting,
                language,
                recall_period,
                timepoint,
                details,
                "extraction record: Instruments and administration",
            ),
        )

    for record_id, row in batch_rows.items():
        status, support_type, evidence = PROJECT_LINKS[record_id]
        connection.execute("INSERT OR IGNORE INTO project VALUES (?, NULL)", (row["project_id"],))
        connection.execute(
            "INSERT INTO project_publication "
            "(project_id, publication_id, link_status, support_type, evidence_class, evidence_locator, note) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                row["project_id"],
                f"doi:{row['doi'].lower()}",
                status,
                support_type,
                evidence,
                "SOURCE_QA.md",
                None if status == "accepted" else "Do not count as funded without authoritative portfolio evidence.",
            ),
        )

    for study_id, instrument_label, time_role, time_label in TIMES:
        connection.execute(
            "INSERT INTO measurement_time "
            "(study_id, instrument_id, time_role, time_label, source_locator) VALUES (?, ?, ?, ?, ?)",
            (study_id, slug(instrument_label), time_role, time_label, "source-checked extraction record"),
        )
    for study_id, sequence, input_label, transformation, output_label, uncertainty in DERIVATIONS:
        connection.execute(
            "INSERT INTO derivation_step "
            "(study_id, sequence, input_label, transformation, output_label, uncertainty_added, source_locator) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (study_id, sequence, input_label, transformation, output_label, uncertainty, "source-checked extraction record"),
        )

    connection.execute(
        "INSERT INTO source_conflict "
        "(study_id, fact_name, value_a, source_a, value_b, source_b, resolution) "
        "VALUES ('B09', 'statistical significance', ?, 'Abstract', ?, 'Results', ?)",
        (
            "not significant (p-values < .05)",
            "mother-father difference p = .023",
            "Retain both statements and flag the abstract wording as internally inconsistent.",
        ),
    )
