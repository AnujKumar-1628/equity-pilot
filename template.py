import os
from pathlib import Path


def create_project_structure():
    # Updated to use the current directory instead of nesting a new folder
    project_root = Path(".")

    # List of all files to be created
    files = [
        "src/equity_pilot/__init__.py",
        "src/equity_pilot/__main__.py",
        "src/equity_pilot/cli.py",
        "src/equity_pilot/config.py",
        "src/equity_pilot/api/app.py",
        "src/equity_pilot/api/routes.py",
        "src/equity_pilot/api/schemas.py",
        "src/equity_pilot/agents/base.py",
        "src/equity_pilot/agents/supervisor.py",
        "src/equity_pilot/agents/financial_analyst.py",
        "src/equity_pilot/agents/market_researcher.py",
        "src/equity_pilot/agents/valuation_analyst.py",
        "src/equity_pilot/agents/risk_analyst.py",
        "src/equity_pilot/agents/verifier.py",
        "src/equity_pilot/agents/report_writer.py",
        "src/equity_pilot/graph/state.py",
        "src/equity_pilot/graph/nodes.py",
        "src/equity_pilot/graph/routing.py",
        "src/equity_pilot/graph/builder.py",
        "src/equity_pilot/graph/checkpointing.py",
        "src/equity_pilot/llm/client.py",
        "src/equity_pilot/llm/structured.py",
        "src/equity_pilot/prompts/__init__.py",
        "src/equity_pilot/prompts/loader.py",
        "src/equity_pilot/prompts/supervisor.md",
        "src/equity_pilot/prompts/financial_analyst.md",
        "src/equity_pilot/prompts/market_researcher.md",
        "src/equity_pilot/prompts/valuation_analyst.md",
        "src/equity_pilot/prompts/risk_analyst.md",
        "src/equity_pilot/prompts/verifier.md",
        "src/equity_pilot/prompts/report_writer.md",
        "src/equity_pilot/domain/models.py",
        "src/equity_pilot/domain/evidence.py",
        "src/equity_pilot/domain/metrics.py",
        "src/equity_pilot/domain/valuation.py",
        "src/equity_pilot/tools/registry.py",
        "src/equity_pilot/tools/market_data.py",
        "src/equity_pilot/tools/sec_filings.py",
        "src/equity_pilot/tools/web_search.py",
        "src/equity_pilot/tools/calculators.py",
        "src/equity_pilot/rag/ingestion.py",
        "src/equity_pilot/rag/chunking.py",
        "src/equity_pilot/rag/vector_store.py",
        "src/equity_pilot/rag/retriever.py",
        "src/equity_pilot/runtime/tool_executor.py",
        "src/equity_pilot/runtime/limits.py",
        "src/equity_pilot/runtime/errors.py",
        "src/equity_pilot/storage/database.py",
        "src/equity_pilot/storage/repositories.py",
        "src/equity_pilot/reporting/report_generator.py",
        "src/equity_pilot/reporting/charts.py",
        "src/equity_pilot/reporting/templates/report.md.j2",
        "src/equity_pilot/observability/tracing.py",
        "src/equity_pilot/observability/cost.py",
        "evals/datasets/golden_questions.jsonl",
        "evals/metrics.py",
        "evals/run_eval.py",
        "tests/conftest.py",
        "scripts/ingest_filings.py",
        "scripts/demo.py",
        "docs/architecture.md",
        "docs/evaluation.md",
        "docker/Dockerfile",
        "docker/docker-compose.yml",
        ".github/workflows/ci.yml",
        ".vscode/settings.json",
        ".env.example",
        ".gitignore",
        ".pre-commit-config.yaml",
        "Makefile",
        "pyproject.toml",
        "LICENSE",
        "README.md",
    ]

    # List of directories that need to be created but don't contain initial files
    empty_dirs = [
        "evals/results",
        "tests/unit",
        "tests/integration",
        "tests/fixtures",
        "data/raw",
        "data/processed",
        "data/vectorstore",
        "reports",
        "docs/examples",
    ]

    print(f"Creating project structure in current directory...")

    # Create files and their parent directories
    for file_path in files:
        full_path = project_root / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.touch(exist_ok=True)
        print(f"Created file: {full_path}")

    # Create empty directories
    for dir_path in empty_dirs:
        full_path = project_root / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {full_path}")

    print("\nProject structure generated successfully!")


if __name__ == "__main__":
    create_project_structure()
