import json
import sys
import time
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.services.chat_service import find_faq_answer


EVALUATION_PATH = PROJECT_ROOT / "data" / "json" / "evaluation_queries.json"


def load_evaluation_queries() -> list[dict[str, str]]:
    with EVALUATION_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("queries", [])


def evaluate_system() -> dict[str, object]:
    queries = load_evaluation_queries()
    total_queries = len(queries)
    total_hits = 0
    total_time_ms = 0.0
    per_category: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "hits": 0})
    detailed_results: list[dict[str, object]] = []

    for item in queries:
        message = item["message"]
        expected_category = item["expected_category"]

        start_time = time.perf_counter()
        response = find_faq_answer(message)
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        is_hit = response.category == expected_category
        total_hits += int(is_hit)
        total_time_ms += elapsed_ms

        per_category[expected_category]["total"] += 1
        per_category[expected_category]["hits"] += int(is_hit)

        detailed_results.append(
            {
                "message": message,
                "expected_category": expected_category,
                "predicted_category": response.category,
                "source": response.source,
                "matched": response.matched,
                "hit": is_hit,
                "response_time_ms": round(elapsed_ms, 3),
            }
        )

    accuracy = (total_hits / total_queries * 100) if total_queries else 0.0
    average_time_ms = (total_time_ms / total_queries) if total_queries else 0.0

    per_category_summary = {}
    for category, values in sorted(per_category.items()):
        total = values["total"]
        hits = values["hits"]
        per_category_summary[category] = {
            "total": total,
            "hits": hits,
            "accuracy_percent": round((hits / total * 100), 2) if total else 0.0,
        }

    return {
        "total_queries": total_queries,
        "hits": total_hits,
        "global_accuracy_percent": round(accuracy, 2),
        "average_response_time_ms": round(average_time_ms, 3),
        "per_category": per_category_summary,
        "details": detailed_results,
    }


def print_report(report: dict[str, object]) -> None:
    print("=== SYSTEM EVALUATION REPORT ===")
    print(f"Total queries: {report['total_queries']}")
    print(f"Hits: {report['hits']}")
    print(f"Global accuracy (%): {report['global_accuracy_percent']}")
    print(f"Average response time (ms): {report['average_response_time_ms']}")
    print("")
    print("Per-category results:")

    for category, values in report["per_category"].items():
        print(
            f"- {category}: {values['hits']}/{values['total']} "
            f"({values['accuracy_percent']}%)"
        )

    print("")
    print("Detailed results:")
    for item in report["details"]:
        print(
            f"- message='{item['message']}' | expected={item['expected_category']} | "
            f"predicted={item['predicted_category']} | source={item['source']} | "
            f"hit={item['hit']} | time_ms={item['response_time_ms']}"
        )


if __name__ == "__main__":
    evaluation_report = evaluate_system()
    print_report(evaluation_report)
