# youtube-automation-engine

A local-first YouTube automation engine for researching, scripting, metadata generation, publishing, and analytics feedback. It is designed to be developed locally, tested in a sandbox, and deployed to GitHub Actions for scheduled operation.

## Architecture

```text
research -> topic scoring -> script -> metadata -> thumbnail -> QA -> publish -> analytics
```

## Repository layout

```text
.
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── youtube-daily.yml
├── src/
│   ├── __init__.py
│   ├── analytics/
│   │   ├── __init__.py
│   │   └── reporter.py
│   ├── cli.py
│   ├── config.py
│   ├── content/
│   │   ├── __init__.py
│   │   └── script_builder.py
│   ├── pipeline.py
│   ├── research/
│   │   ├── __init__.py
│   │   └── idea_generator.py
│   ├── video/
│   │   ├── __init__.py
│   │   └── media_pipeline.py
│   └── youtube/
│       ├── __init__.py
│       └── client.py
├── tests/
│   ├── test_config.py
│   └── test_pipeline.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── .github/workflows/
```

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m src.cli research --topic "AI automation"
python -m src.cli script --topic "AI automation"
pytest
```

## Security model

Never commit real API keys to the repository. Keep them in a local `.env` file or in GitHub Secrets.

Example variables:

```bash
APP_NAME=youtube-automation-engine
ENVIRONMENT=development
YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
YOUTUBE_REFRESH_TOKEN=
YOUTUBE_CHANNEL_ID=
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
```

## Typical workflow

1. Research and score topic ideas
2. Generate a script and thumbnail brief
3. Run QA checks locally
4. Publish through the YouTube API
5. Pull analytics back into the content loop

## GitHub Actions

CI runs on push and pull request. A scheduled workflow is included for daily automation runs.

## License

MIT
