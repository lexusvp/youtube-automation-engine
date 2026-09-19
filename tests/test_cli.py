def test_dry_run(monkeypatch,capsys):
    from src.cli import main
    monkeypatch.setattr("sys.argv",["cli","dry-run","--topic","AI automation"])
    main(); assert "DRY RUN" in capsys.readouterr().out
